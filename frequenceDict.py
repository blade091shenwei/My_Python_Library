#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     产生词频字典，有2种情况：
#     1.  对一个文件夹下的所有文本文件进行词频统计（文件夹模式）
#             函数的输入是文件夹的路径
#     2.  对一段text进行词频统计（文本模式）
#             函数的输入是这段文本
#     函数在默认情况下是第二种情况
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

import re
import os

#函数返回一个dict对象
def getFrequenceDict(param, textModel = True):
    
    #文本模式，输入是文本
    if textModel == True:
        words = []
        #分割符号有：英文句号，问号，感叹号，逗号，空格，回车，Tab符号,单引号，双引号，冒号
        #正则表达式的反斜杠需不需要还不清楚
        text = re.split('\.|\?|\!|\,| |\n|\t|\'|\"|\:',param)
        for word in text:
            if cmp(word,'') == 0:
                pass
            else:
                words.append(word)
        
    #文件夹模式，输入是文件夹路径
    else:
        words = []
        files = os.listdir(param)
        for fileName in files:
            wordsInOneDoc = []
            filePath = param + fileName
            TEXT = open(filePath).read()
            text = re.split('\.|\?|\!|\,| |\n|\t|\'|\"|\:',TEXT)
            for word in text:
                if cmp(word,'') == 0:
                    pass
                else:
                    wordsInOneDoc.append(word)
            words.extend(wordsInOneDoc)
    #进行词频统计，并按照顺序进行排序
    Dict = {}
    for word in words:
        if Dict.get(word) == None:
            Dict.setdefault(word, 1)
        else:
            Dict.update({word:Dict.get(word)+1})
    Dict_sorted = sorted(Dict.iteritems(), \
                         key=lambda s:s[1], reverse = True)
    
    return Dict_sorted
    
    
    
    
    
    
    

