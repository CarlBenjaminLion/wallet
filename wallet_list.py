#coding=utf-8
import sys, os, urllib
import urllib2, json, codecs
import datetime, pyfiglet
class ListWords(object):
    def __init__(self):
        self.path = self.cur_file_dir()
        self.today = datetime.datetime.now().strftime('%Y.%m.%d')

    def cur_file_dir(self):
        # 获取脚本路径
        path = sys.path[0]
        # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

    def write_list_log(self, word):
        path = self.path+'/log/dayListLog/'+self.today+'.txt'
        file = open(path,'a')
        file.write(word + '\n')
        file.close()

    def write_view_words(self, word, mean1, mean2):

        num = len(word)
        path = self.path + '/listOfWords/' + self.today + "单词列表.txt"

        file = codecs.open(path, 'a', 'utf-8')
        file.write(word + (20 - num) * ' ' + mean1 + '  ' + mean2 + '\n')
        file.close()
    def write_mp3_words(self,mp3):
        path = self.path + '/mp3OfWords/' + self.today+ '.mp3'
        mp3file = open(path, 'ab')
        mp3file.write(urllib.urlopen(mp3).read())
        mp3file.close()


    def listWords(self):
        #为了做好数据的存储，我需要对这个函数做一个文件来记录自己背单词记录，返回一个值
        print '================================================================'
        print "如果推出请输入  ~quit"
        word = ''
        list = []
        while (word != "~quit"):
            try:

                url = 'http://xtk.azurewebsites.net/BingDictService.aspx?Word='
                word = raw_input("input           -----   ")
                if(word == '~quit'):
                    break
                api = url + word
                response = urllib2.urlopen(api + '&Samples=false')
                obj = response.read()
                en = json.loads(obj)
                mean1 = en['defs'][0]['pos'] + "---" + en['defs'][0]['def']
                mean2 = en['defs'][1]['pos'] + "---" + en['defs'][1]['def']
                print mean1
                print mean2
                pyfiglet.print_figlet(word)
                if word in list:
                    print '================================================================'
                    continue
                list.append(word)
                self.write_view_words(word, mean1, mean2)
                self.write_list_log(word)
                print '================================================================'
            except:
                print '-------------这个单词可能找不到，换一个再来----------------'
        return

    def listWordsMakeMp3(self):
        print '================================================================'
        print "如果推出请输入  ~quit"
        word = ''
        list = []
        while (word != "~quit"):
            try:

                url = 'http://xtk.azurewebsites.net/BingDictService.aspx?Word='
                word = raw_input("input           -----   ")
                if (word == '~quit'):
                    break
                api = url + word
                response = urllib2.urlopen(api + '&Samples=false')
                obj = response.read()
                en = json.loads(obj)
                mean1 = en['defs'][0]['pos'] + "---" + en['defs'][0]['def']
                mean2 = en['defs'][1]['pos'] + "---" + en['defs'][1]['def']
                mp3 = en['pronunciation']['AmEmp3']
                print mean1
                print mean2
                pyfiglet.print_figlet(word)
                if word in list:
                    print '================================================================'
                    continue
                list.append(word)
                self.write_view_words(word, mean1, mean2)
                self.write_list_log(word)
                self.write_mp3_words(mp3)
                print '================================================================'
            except:
                print '-----------------------------------------------'


if __name__ == '__main__':
    pass

'''
这个脚本还是很实用的，但是我需要一个华丽的输入和输出来提高用户体验 做好了
再接下来的两天内完成 额，其实拖了好多天
华丽输入输出 搞定
单词去重 搞定
加油 fighting！！
！！！！
！！！！
！！！！
！！！！
！！！！
'''
