# coding: utf-8
""" 如何将http的参数转换成 class 所需的参数，我需要一个像tornado或是flask的框架来帮我做这件事情 """


# 多个人修改一条记录，该如何记录?
# 如果新创建就生成一个新的mid, 如果是修改，则修改相应的mid

# 自动生成soundmark?  自动根据soundmark发音？( 进阶功能 )

class Item(object):
    def __init__(self, name, mid, meaning, user, soundmark, english_meaning):
        self.name = name
        self.record = {mid : [(meaning, user)]
        self.soundmark = soundmark
        self.english_meaning = english_meaning


        pass
