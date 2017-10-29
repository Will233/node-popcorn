# -*- coding: utf-8 -*-
import codecs
import sys

# @see 读取文件内容
def readFile(filename):
  content = ""
  try:
    fo = codecs.open(filename, 'r', "utf-8")
    print "读取文件名：", filename
    for line in fo.readlines():
      content += line.strip()
    print "字数：", len(content)
  except IOError as e:
    print "文件不存在或者文件读取失败"
    return ""
  else:
    fo.close()
    return content
# @see 写入文件内容（数组会使用writelines进行写入）codec.open实现
# @param toFile 文件名
#        content 内容
def writeFile(toFile, content):
  try:
    fo = codecs.open(toFile, 'wb', "utf-8")
    print "文件名：", toFile
    if type(content) == type([]):
      fo.writelines(content)
    else:
      fo.write(content)
  except IOError:
    print "没有找到文件或文件读取失败"
  else:
    print "文件写入成功"
    fo.close()

print "\n###### Analysis Start ######\n"
# 获取调用参数：
# print "name: ", sys.argv[0] # 脚本名
sourceFile = sys.argv[1]
targetFile = sys.argv[2]

# 词频统计和排序
wordList= []
wordCount= {}
wordItemArray= []

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
wf = codecs.open(targetFile,'w', "utf-8")
# 读取数据并分析
sourceData = readFile(sourceFile)
wordList = sourceData.split(' ')
for item in wordList:
  if item not in wordCount:
    wordCount[item] = 1
  else:
    wordCount[item] += 1

for key in wordCount:
  wordItemArray.append(wordItem(key, wordCount[key]))

wordItemArray.sort(reverse = True)

for item in wordItemArray:
  wf.write(item.label+' '+str(item.times) + '\n')
wf.close()
print "源文件", sourceFile
print "目标文件", targetFile
print "\n###### Analysis Finish ######"