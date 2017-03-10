#coding=utf-8
import sys, os
import pyfiglet
from colorama import init, Fore
init(autoreset=True)
class ShowAllLog(object):
    def __init__(self):
        self.log_date = []
        self.log_words = set()
        self.filelist = []
        self.path = self.cur_file_dir()
        self.allWordsLogPath = self.path + '/log/logOfAll/log.txt'
        self.allDaysLogPath  = self.path + '/log/dayListLog/'                  # 用于统计我的log，写入log
        self.type = ['txt']
        pass

    def getFile(self, path):
        #这个函数将所有的位于path中的txt格式的文件
        filelist = []
        type = ['txt']
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                ext = filename.split('.')[-1]
                if ext in type:
                    filelist.append(os.path.join(parent, filename))
        return filelist
    def countWords(self,fname):
        #计算并返回没一个文件的单词数量
        count = 0
        for file_line in open(fname).xreadlines():
            if file_line != '' and file_line != '\n':
                count += 1
        return count

    def cur_file_dir(self):
        # 获取脚本路径
        path = sys.path[0]
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)
        #
        #
        #
    def process(self):
        filelist = self.getFile(self.allDaysLogPath)
        logFile = open(self.allWordsLogPath, 'w')
        for day in filelist:
            count =self.countWords(day)
            dayName = day.split('/')[-1].strip('.txt')
            logFile.write(dayName + '  ----  ' + str(count)+'\n')
        logFile.close()#这个处理是没有任何显示的，仅仅是对log写入而已



    def get_word(self,fname):
        word = set()
        file = open(fname, 'r')
        for i in file.xreadlines():
            if i == '' and i == ' ' and i =='\n':
                continue
            i = i.strip('\n')
            word.add(i)
        file.close()
        return word

    def show(self):#我要一个非常壮观的输出
        color = {0: Fore.RED, 1: Fore.LIGHTRED_EX, 2: Fore.YELLOW, 3: Fore.LIGHTGREEN_EX, 4: Fore.GREEN}
        filelist = self.getFile(self.allDaysLogPath)#~/wallet/log/dayListLog/
        words = set()
        num = 25

        for file in filelist:
            word = self.get_word(file)
            words = word | words

        a = list(words)
        i = 0
        k = 0
        while i < len(a):
            try:
                print(color[(k + 0) % 5] + a[i]   + ' ' * (num - len(a[i]  )) +
                      color[(k + 1) % 5] + a[i+1] + ' ' * (num - len(a[i+1])) +
                      color[(k + 2) % 5] + a[i+2] + ' ' * (num - len(a[i+2])) +
                      color[(k + 3) % 5] + a[i+3] + ' ' * (num - len(a[i+3])) +
                      color[(k + 4) % 5] + a[i+4] )
                i += 5
                k += 1
            except:
                i += 5
                continue
        pyfiglet.print_figlet("Wallet : "+ str(len(words)))



    def log(self):
        filelist = self.getFile(self.allDaysLogPath)
        #省去所有文件读写的内容
        total = 0
        for day in filelist:
            count = self.countWords(day)
            dayName = day.split('/')[-1].strip('.txt')
            print dayName + '  ------------------------------  ' + str(count)
            total += count
        pyfiglet.print_figlet("Wallet   :   "+ str(total))



if __name__ == '__main__':
    obj = ShowAllLog()
    obj.show()


