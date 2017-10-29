# -*- coding: utf-8 -*-
import codecs
import sys

print "\n###### Analysis Start ######\n"
# 获取调用参数：
# print "name: ", sys.argv[0] # 脚本名
sourceFile = sys.argv[1]
targetFile = sys.argv[2]

# 词频统计和排序
word_lst= []
word_dict= {}
word_items= []

# 定义wordItem 类
class wordItem:
  label = ''
  times = 0
  def __init__(self, l, t):
    self.label = l
    self.times = t
  def __lt__(self, other):
    return self.times < other.times

# 读取数据并分析
with codecs.open(sourceFile, 'r', "utf-8") as wf, codecs.open(targetFile,'w', "utf-8") as wf2:

  for word in wf:  
        word_lst.append(word.split(' ')) 
        for item in word_lst:  
             for item2 in item:  
                if item2 not in word_dict:
                    word_dict[item2] = 1  
                else:  
                    word_dict[item2] += 1  

  for key in word_dict:  
      word_items.append(wordItem(key, word_dict[key]))

  word_items.sort(reverse = True)
  for item in word_items:
      wf2.write(item.label+' '+str(item.times) + '\n')

print "源文件", sourceFile
print "目标文件", targetFile
print "\n###### Analysis Finish ######"