#coding=utf-8
import wallet_list, wallet_all
class Guider(object):
    def __init__(self):
        self.list = wallet_list.ListWords()
        self.showAll = wallet_all.ShowAllLog()
    def guide(self, option_tuple):
        #接收一个元组对象来判断用户的参数选项看，调用相应的功能
        #print option_tuple
        if option_tuple[0] and not option_tuple[1] and not option_tuple[2] and not option_tuple[3]:
            #-w --words
            #进入一个查询单词的循环，可以退出
            #退出 的功能还没有编写，推出后让用户选择是否需要将查询的单词文件写成mp3文件
            self.list.listWords()
            #这个函数在运行之后是一定会将单词写入你的每日单词列表文件中的
            self.showAll.process()
            return
        elif not option_tuple[0] and option_tuple[1] and not option_tuple[2] and not option_tuple[3]:
            #-a --all
            self.showAll.show()
            pass
        elif not option_tuple[0] and not option_tuple[1] and option_tuple[2] and not option_tuple[3]:
            #-l --log
            self.showAll.log()
        elif not option_tuple[0] and not option_tuple[1] and not option_tuple[2] and option_tuple[3]:
            #-m --mp3
            self.list.listWordsMakeMp3()
            self.showAll.process()
        elif option_tuple[0] and not option_tuple[1] and not option_tuple[2] and option_tuple[3]:
            # -wm --words --mp3
            self.list.listWordsMakeMp3()
            self.showAll.process()
        else:
            return
