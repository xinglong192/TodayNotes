class CusMsgBus:
    """ 简易的消息总线 """
    __all_topic = {}  # 话题及关注者列表

    @staticmethod
    def send(topic, *msg):
        """ 调用接收者方法 """
        for o in CusMsgBus.__all_topic.get(topic, []):
            getattr(o, topic)(*msg)

    @staticmethod
    def append(topic, o):
        """ 加入列表 """
        CusMsgBus.__all_topic.setdefault(topic, []).append(o)

    @staticmethod
    def quit(topic, o):
        """ 退出列表 """
        tp = CusMsgBus.__all_topic.get(topic, [])
        if tp and o in tp:
            tp.remove(o)
