#coding=utf-8
import optparse
usage ='''
wallet -w --words 进入一个查询单词的循环
wallet -m --mp3   接受一个txt文件，一个mp3名称，制作mp3文件
wallet -l --log   查看背单词日志
wallet -h --help  查看帮助
wallet -a --all   查看你背记的全部的单词
'''


class Parse(object):
    def __init__(self):
        self.words = False
        self.mp3 = ''
        self.log = False
        self.all = False
    def parse(self):
        parser = optparse.OptionParser(usage=usage)
        parser.add_option('-w', '--words',dest='words', action='store_true', help = '开始查询单词汉语语义', default=False)
        parser.add_option('-m', '--mp3',  dest='mp3', help='接受一个txt文件，一个mp3名称，制作mp3文件', action='store_true', default=False)
        parser.add_option('-l', '--log', dest='log', help='查看背单词日志', action='store_true', default=False)
        parser.add_option('-a', '--all', dest='all', help='查看你背记的全部的单词', action='store_true', default=False)
        (options, args) = parser.parse_args()
        self.words = options.words
        self.all   = options.all
        self.log   = options.log
        self.mp3   = options.mp3
        a= (self.words, self.all, self.log, self.mp3, args)
        return a

if __name__ == '__main__':
    obj = Parse()
    obj.parse()
    print obj.words
    print obj.all
    print obj.log
    print obj.mp3
