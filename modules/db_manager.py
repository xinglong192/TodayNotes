import re
import sys
from datetime import datetime
from pathlib import Path

# import pytz
from PySide6.QtSql import QSqlDatabase, QSqlQuery

from .setting import root_path
from .vdialog import VDialogType, VDialog

FORMAT_TIME_STR = '%Y-%m-%d %H:%M:%S'
FORMAT_DATE_STR = '%Y-%m-%d'


# def DecutcToLocalTime(date: str, flag: bool = True) -> str:
#     """ sqlite 以utc存储的时间 转换为本地时区时间 """
#     return datetime.strptime(date, FORMAT_TIME_STR).replace(tzinfo=pytz.utc if flag else None).astimezone(
#         tz=None if flag else pytz.utc).strftime(
#         FORMAT_TIME_STR)


def timeToDat(time: str) -> str:
    return datetime.strptime(time, FORMAT_TIME_STR).strftime(FORMAT_DATE_STR)


def html2text(html):
    """ 仅适用与本项目特例 """

    def format(t):
        t = re.sub(r'(\n)', "", t)
        # t = re.sub(r'(\t)', "", t)
        t = re.sub(r'(\r)', "", t)
        t = re.sub(r'<style.*</style>', "", t)
        t = re.sub(r'<img src=[^>]* />', "[图片]", t)
        t = re.sub(r'<p [^>]*>(.*)</p>', r"<p>\1</p>", t)
        t = re.sub(r'</?[^>]*>', "", t)
        # t = re.sub(r'(\s)', "", t)
        return t

    th = re.findall(r'(<p .*[^/]>.*</p>)', html)
    res = ''
    for t in th:
        res += format(t)
        res += '\n'
    return res


class DBManager:
    print('------------check database-----------')
    # 创建存储文件路径
    dbPath = root_path
    Path(dbPath).mkdir(parents=True, exist_ok=True)

    # 链接数据库
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(dbPath + 'notes.sqlite')
    ok = db.open()
    if not ok:
        VDialog.doSomething(VDialogType.Error, '创建数据文件失败,前检查文件夹权限')
        # 退出
        sys.exit('创建数据文件失败')

    query = QSqlQuery()
    # 查询records表是否存在
    if query.exec("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='RECORDS'"):
        query.next()
        if query.value(0) < 1:
            f = query.exec("""
            CREATE TABLE IF NOT EXISTS RECORDS(
               rid INTEGER PRIMARY KEY AUTOINCREMENT,
               content TEXT NULL,
               indate TIMESTAMP NOT NULL,
               status INTEGER DEFAULT 0
            );
            """)
            # 新建一条欢迎笔记
            csql = 'INSERT INTO RECORDS (rid,content,indate) VALUES (1, :content , :indate )'
            query.prepare(csql)
            query.bindValue(':content',
                            u"欢迎使用笔记本：\n"
                            " - 首页可查看今日笔记，仅展示当天的记录\n"
                            " - 首页右上角[...]按钮查看其他日期记录\n"
                            " - 首页左上角[+]按钮可新建记录\n"
                            " - 点击首页记录条目可查看具体内容及标签等信息\n"
                            " - 笔记详细页面可修改信息\n"
                            " - 标签可通过编辑页面[+]按钮添加,拖动标签可调整顺序，右键可删除标签")

            query.bindValue(':indate', datetime.now().strftime(FORMAT_TIME_STR))
            query.exec()

            print('------------create table records-----------' + str(f))

    # 查询tags表是否存在
    if query.exec("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='TAGS'"):
        query.next()
        if query.value(0) < 1:
            f = query.exec("""
            CREATE TABLE IF NOT EXISTS TAGS(
               tid INTEGER PRIMARY KEY AUTOINCREMENT,
               text VARCHAR (10) NULL,
               type INTEGER DEFAULT 0
            );
            """)
            query.exec("CREATE INDEX IF NOT EXISTS idx_text ON TAGS (text);")
            query.prepare('INSERT INTO TAGS (tid,text) VALUES ( 1 ,"初始笔记" )')
            query.exec()

            print('------------create table tags-----------' + str(f))
    # 查询rtrel表是否存在
    if query.exec("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='RTREL'"):
        query.next()
        if query.value(0) < 1:
            f = query.exec("""
               CREATE TABLE IF NOT EXISTS RTREL(
                   uid INTEGER PRIMARY KEY AUTOINCREMENT,
                   rid INTEGER NOT NULL,
                   tid INTEGER NOT NULL,
                   sort INTEGER DEFAULT 0
                );
               """)
            query.exec("CREATE INDEX IF NOT EXISTS idx_rid ON RTREL (rid);")
            query.exec("CREATE INDEX IF NOT EXISTS idx_tid ON RTREL (tid);")
            query.prepare("INSERT INTO RTREL (rid,tid,sort)VALUES (1,1,0)")
            query.exec()

            print('------------create table RTREL-----------' + str(f))

    # 查询attachfile表是否存在
    if query.exec("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='ATTACHFILE'"):
        query.next()
        if query.value(0) < 1:
            f = query.exec(
                """CREATE TABLE IF NOT EXISTS ATTACHFILE(
                   fid VARCHAR(32) PRIMARY KEY,
                   rid INTEGER NOT NULL,
                   file BLOB NOT NULL,
                   suffix VARCHAR(10) DEFAULT 'PNG'
                );""")
            query.exec("CREATE INDEX IF NOT EXISTS idx_rid ON ATTACHFILE (rid);")
            query.exec()

            print('------------create table RTREL-----------' + str(f))

    print('------------check end-----------')

    @staticmethod
    def getDayNotes(date: str = None) -> list[list]:
        """ 按天获取记录信息 """
        q = DBManager.query
        if not date:
            date = datetime.now().strftime(FORMAT_DATE_STR)
        else:
            date = timeToDat(date)
        q.prepare('SELECT * FROM RECORDS WHERE indate Like :indate ORDER BY indate DESC')
        q.bindValue(':indate', date + '%')
        if not q.exec():
            # 查询不成功
            VDialog.doSomething(VDialogType.Error, f'数据记录表不存在,重启试试\n 详情:-{q.lastError().text()}')
        res = []
        cols = q.record().count()
        while q.next():
            res.append([q.value(i) for i in range(cols)])
        return res

    @staticmethod
    def getNoteById(rid: str | int) -> dict:
        """ 获取指定id的记录内容 和对于标签 """
        res = {}
        if rid is None:
            return res
        q = DBManager.query
        # 查内容
        q.prepare('SELECT * FROM RECORDS WHERE rid = :rid')
        q.bindValue(':rid', rid)
        q.exec()
        qs = q.record()
        cols = [qs.fieldName(i) for i in range(qs.count())]

        while q.next():
            res.update({n: q.value(n) for n in cols})
        # 查标签
        q.prepare(
            'SELECT TAGS.*,RTREL.sort sort FROM TAGS JOIN RTREL ON TAGS.tid=RTREL.tid AND RTREL.rid= :rid ORDER BY sort')
        q.bindValue(':rid', rid)
        q.exec()
        qs = q.record()
        cols = [qs.fieldName(i) for i in range(qs.count())]
        res['tags'] = []
        while q.next():
            res['tags'].append({n: q.value(n) for n in cols})

        return res

    @staticmethod
    def addNote(con: dict) -> int:
        """ 添加记录 及标签关系 """
        if not con or not con['content']:
            VDialog.doSomething(VDialogType.Error, '内容不能为空')
            return 0
        if not con['indate']:
            con['indate'] = datetime.now().strftime(FORMAT_TIME_STR)
        q = DBManager.query
        # 插入数据
        csql = 'INSERT INTO RECORDS (content,indate) VALUES ( :content , :indate )'
        q.prepare(csql)
        q.bindValue(':content', con['content'])
        q.bindValue(':indate', con['indate'])
        f = q.exec()
        if not f:
            VDialog.doSomething(VDialogType.Error, '添加失败' + q.lastError().text())
            return 0
        q.exec('select last_insert_rowid()')
        rid = 0
        while q.next():
            rid = q.value(0)
        # 加入标签关系
        DBManager.setTagsRel(rid, con['tags'])
        return rid

    @staticmethod
    def modifyNote(rid: int | str, con: dict) -> bool:
        """ 根据记录id 修改内容 和标签关系"""
        if not rid:
            VDialog.doSomething(VDialogType.Error, '未收到内容id')
            return False
        if not con or not con['content']:
            VDialog.doSomething(VDialogType.Error, '内容不能为空')
            return False
        q = DBManager.query
        # 修改数据
        csql = 'UPDATE RECORDS SET content = :content '
        if con['indate']:
            csql += ', indate= :indate '
        csql += ' WHERE rid = :rid'
        q.prepare(csql)
        q.bindValue(':content', con['content'])
        q.bindValue(':rid', rid)
        if con['indate']:
            q.bindValue(':indate', con['indate'])

        if not q.exec():
            VDialog.doSomething(VDialogType.Error, '修改内容失败')
            return False
        # 修改标签
        DBManager.setTagsRel(rid, con['tags'])
        return True

    @staticmethod
    def delNote(rid: str | int) -> bool:
        """ 删除记录 """
        if rid is None:
            return False
        q = DBManager.query
        q.prepare('DELETE FROM RECORDS WHERE rid= :rid')
        q.bindValue(':rid', rid)
        f = q.exec()

        q.prepare('DELETE FROM RTREL WHERE rid= :rid')
        q.bindValue(':rid', rid)
        q.exec()

        return f

    @staticmethod
    def setTagsRel(rid: str, tags: list) -> None:
        """ 添加标签和记录关系"""
        q = DBManager.query
        q.prepare('DELETE FROM RTREL WHERE rid= :rid')
        q.bindValue(':rid', rid)
        q.exec()
        if tags:
            q.prepare(f"INSERT INTO RTREL (rid,tid,sort)VALUES ({rid},?,?)")
            tsn = [i for i in range(len(tags))]
            q.addBindValue(tags)
            q.addBindValue(tsn)
            q.execBatch()

    @staticmethod
    def queryTags(tids: list) -> dict:
        q = DBManager.query
        q.prepare(
            f'SELECT * FROM TAGS WHERE tid IN ( {str(tids)[1:-1]} )')
        q.exec()
        qs = q.record()
        cols = [qs.fieldName(i) for i in range(qs.count())]
        res = {}
        while q.next():
            res[q.value(0)] = {n: q.value(n) for n in cols}
        return res

    @staticmethod
    def addTag(text: str) -> int | None:
        """ 添加标签并返回主键tid """
        if not text:
            VDialog.doSomething(VDialogType.Error, '内容不能为空')
            return None
        q = DBManager.query
        # 查询是否有该标签
        q.prepare("SELECT tid FROM TAGS WHERE text= :text LIMIT 1")
        q.bindValue(':text', text)
        q.exec()
        tid = None
        while q.next():
            tid = q.value(0)
        if tid is not None:
            return tid
        # 插入数据
        csql = 'INSERT INTO TAGS (text) VALUES ( :text )'
        q.prepare(csql)
        q.bindValue(':text', text)
        f = q.exec()
        if not f:
            VDialog.doSomething(VDialogType.Error, '添加标签失败' + q.lastError().text())
            return None
        q.exec('select last_insert_rowid()')
        while q.next():
            tid = q.value(0)
        return tid

    @staticmethod
    def delTag(text: str) -> int | None:
        """ 删除标签 """
        # FIXME 删除标签sql 因为表结构设计问题，暂时还没有删除的页面操作
        pass

    @staticmethod
    def queryForNotesList(condition: dict):
        res = []
        sql = 'SELECT * FROM RECORDS WHERE 1=1 '
        sql += DBManager.__transition_condition(condition)
        sql += ' ORDER BY indate DESC'

        q = DBManager.query
        q.prepare(sql)
        q.exec()
        cols = q.record().count()
        while q.next():
            res.append([q.value(i) for i in range(cols)])
        return res

    @staticmethod
    def __transition_condition(condition: dict):
        # 查询器输入文本
        conQuery = condition.get('conQuery', '')
        conQuery.strip()
        # 时间控件值
        today = datetime.now().strftime(FORMAT_DATE_STR)
        indate = condition.get('indate', [today, today])
        # 是否使用时间筛选
        usedate = condition.get('usedate', True)
        sql = ''
        # 无@符号 或者都转义了 则认为是 查询笔记内容
        if conQuery:
            if all([(item[-1] == '\\') if len(item) > 0 else False for item in conQuery.split('@')[:-1]]):
                if conQuery == '图片':
                    sql += r"AND (content LIKE '%图片%' OR content LIKE '%<img %')"
                else:
                    sql += f"AND content LIKE '%{conQuery}%'"
            elif conQuery.find('@note:') > 0 or conQuery.find('@tag:') > 0:
                ni = conQuery.find('@note:')
                ti = conQuery.find('@tag:')
                if ni == -1:
                    ni = len(conQuery)
                if ti == -1:
                    ti = len(conQuery)
                ti = conQuery[:min(ni, ti)]
                ti = ti.strip()
                if ti.upper().endswith('OR') or ti.upper().endswith('AND'):
                    ti = ti[:-2 if ti.upper().endswith('OR') else -3].strip()

                if ti == '图片':
                    sql += r"AND (content LIKE '%图片%' OR content LIKE '%<img %')"
                else:
                    sql += f"AND content LIKE '%{ti}%'"

            if '@note:' in conQuery:
                # e.g.
                # @note:[content like '%玩游戏%']
                # @note:[(content='上午在学作业' and indate like '2022-05-05%') or (content='新闻联播结束' and and indate='2022-05-06 19:30:00')]
                nsp = conQuery.find('@note:') + 6
                nep = conQuery.find(']', nsp + 1)
                if nep != -1:
                    tts = conQuery[max(0, conQuery[:nsp].rfind(']')):nsp].upper()
                    a_o = 'OR' if 'OR' in tts else 'AND'
                    text = conQuery[nsp + 1:nep]
                    sql += f"{a_o} {text}"
            if '@tag:' in conQuery:
                # e.g.
                # @tag:日常
                # @tag:[text='日常']
                # @tag:[(text='日常' and sort=1) or (text='学习' and sort=3)]
                tsp = conQuery.find('@tag:') + 5
                tep = conQuery.find(']', tsp + 1)
                tts = conQuery[max(0, conQuery[:tsp].rfind(']')):tsp].upper()
                a_o = 'OR' if 'OR' in tts else 'AND'
                if tep != -1:
                    text = conQuery[tsp + 1:tep]
                    sql += f" {a_o} rid IN (SELECT rid FROM RTREL JOIN TAGS ON RTREL.tid = TAGS.tid WHERE 1=1 AND {text} )"
                elif conQuery.find('[', tsp - 1) == -1:
                    text = conQuery[tsp:]
                    sql += f" {a_o} rid IN (SELECT rid FROM RTREL JOIN TAGS ON RTREL.tid = TAGS.tid WHERE 1=1 AND text like '%{text}%' )"

        if usedate:
            # XXX 手动加入时分秒
            sql += f"AND indate BETWEEN '{indate[0] + ' 00:00:00'}' AND '{indate[1] + ' 23:59:59'}'"

        return sql

    @staticmethod
    def getFileByRid(rid):
        q = DBManager.query
        q.prepare('SELECT fid,rid,file,suffix FROM ATTACHFILE WHERE rid= :rid')
        q.bindValue(':rid', rid)
        q.exec()
        res = []
        cols = q.record().count()
        while q.next():
            res.append([q.value(i) for i in range(cols)])
        return res

    @staticmethod
    def saveFile(data: list):
        """
        保存附件
        data:[[fid,rid,file,suffix],[...]]
        """
        if not data:
            return False
        q = DBManager.query
        q.prepare('INSERT INTO ATTACHFILE (fid,rid,file,suffix) VALUES(?,?,?,?)')
        q.addBindValue([d[0] for d in data])
        q.addBindValue([d[1] for d in data])
        q.addBindValue([d[2] for d in data])
        q.addBindValue([d[3] for d in data])
        return q.execBatch()

    @staticmethod
    def delFileByRid(rid):
        q = DBManager.query
        q.prepare('DELETE FROM ATTACHFILE WHERE rid= :rid')
        q.bindValue(':rid', rid)
        q.exec()
