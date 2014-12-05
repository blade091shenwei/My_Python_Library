#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     这是为方便建立的python读取文件常用的库函数
#     一般情况下函数输入的是文件名或文件路径
#     返回的是相应的数据格式
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

#读取停止词文件，返回停止词列表
def readStopWordList( path ):
    
    stopWords = []
    readStopWord = open(path,'r')
    for line in readStopWord.xreadlines():
        stopWord = line.replace('\n','').replace('\r','')
        if cmp(stopWord,'') == 0:
            pass
        else:
            stopWords.append(stopWord)
            
    return stopWords
    
    