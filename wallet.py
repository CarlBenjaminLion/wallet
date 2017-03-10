#!/usr/bin/env python
#coding=utf-8
from colorama import init, Fore
import wallet_all
import wallet_guider
import wallet_list
import wallet_mp3
import wallet_parser
init(autoreset=True) #与颜色输出有关
class Wallet():
    def __init__(self):
        self.option = ()
        self.guider = wallet_guider.Guider()
        self.parser = wallet_parser.Parse()
    def main(self):
        self.option = self.parser.parse()#这个函数返回的是一个数组对象，是用户的选项self.words,self.all,self.log,self.mp3
        self.guider.guide(self.option)#这个方法接受选项元组来判断用户需要的功能来实现，并返回必要的日志数据
        #print type(self.option)
        #print self.option[0]
        #print self.option[1]
        #print self.option[2]
        #print self.option[3]
        #上面的废弃语句是用来测试代码运行的具体情况，测试我的代码是否返回了顺序与值都正确的布尔变量



if __name__ == '__main__':
    print(Fore.RED +         '|            __      ____ _| | | ___| |_                       |\n' +
          Fore.LIGHTRED_EX + '|            \ \ /\ / / _` | | |/ _ \ __|                      |\n' +
          Fore.GREEN +       '|             \ V  V / (_| | | |  __/ |_                       |\n' +
          Fore.YELLOW +      '|              \_/\_/ \__,_|_|_|\___|\__|                      |\n' +
          Fore.WHITE +       '|                                                              |\n' +
          Fore.WHITE +       '|                    help you to catch english words day by day|\n' +
          Fore.CYAN +        '|                    version 1.0.1                             |\n' +
          Fore.YELLOW +      '|                                           by PTU CarlBenjamin|\n' +
          Fore.BLACK +       '|________________________________东北电力大学理学院软件研发中心|\n')
    obj = Wallet()
    obj.main()
