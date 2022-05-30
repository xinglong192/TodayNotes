import configparser
import os

default_close_flag = '0'  # 关闭按钮的标识(0:无/1:关闭程序/2:最小化到托盘)
default_sball_flag = '0'  # 最小化至托盘后是否显示悬浮球 (0:无-未设置/1:手动显示/2:自动显示)
confFile = 'data/conf.ini'
con = configparser.ConfigParser()

root_path = 'data/'  # 程序文件存储根路径，sqlite文件和临时文件
use_cus_view = '0'  # 是否使用本程序的查看器，默认不用，使用系统自带的


def update_conf(sec: str, opt: str, val: str) -> None:
    """ 更新配置文件中键值 """
    if os.path.exists(confFile) and con.has_section(sec):
        con.read(confFile)
        con.set(sec, opt, val)
        con.write(open(file=confFile, mode='r+', encoding='utf8'))
        return
    con.add_section(sec)
    con.set(sec, opt, val)
    con.write(open(file=confFile, mode='a', encoding='utf8'))


print('----读取配置文件----')
# 读取配置文件
if os.path.exists(confFile):
    con.read(confFile, 'utf-8')
    # 读按钮标识配置
    if con.has_option('base', 'default_close_flag'):
        baseItems = dict(con.items('base'))
        default_close_flag = baseItems.get('default_close_flag', '0')
    else:
        update_conf('base', 'default_close_flag', '0')
    # 读悬浮球标识配置
    if con.has_option('base', 'default_sball_flag'):
        baseItems = dict(con.items('base'))
        default_sball_flag = baseItems.get('default_sball_flag', '0')
    else:
        update_conf('base', 'default_sball_flag', '0')
    # 读取配置文件中存储根路径
    if con.has_option('base', 'root_path'):
        baseItems = dict(con.items('base'))
        root_path = baseItems.get('root_path', root_path)
    # 读取配置文件中 是否使用本程序的查看器标识
    if con.has_option('base', 'use_cus_view'):
        baseItems = dict(con.items('base'))
        use_cus_view = baseItems.get('use_cus_view', '0')

else:
    if not os.path.exists('data'):
        os.makedirs('data')
    update_conf('base', 'default_close_flag', '0')
    update_conf('base', 'default_sball_flag', '0')

# 存放临时图片，用于预览时生成
temp_path_images = root_path + 'temp/images'
if not os.path.exists(temp_path_images):
    os.makedirs(temp_path_images)
