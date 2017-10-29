# -*- coding: utf-8 -*-
import jieba
import thulac
import codecs
import sys

print "\n###### Segment Start ######"
# 获取调用参数：
# print "name: ", sys.argv[0]
# for i in range(1, len(sys.argv)):#这里参数从1开始
#     print "param", i, sys.argv[i]
# fileNo = sys.argv[1]
sourceFile = sys.argv[1]
targetFile = sys.argv[2]
engine =  sys.argv[3]
dictionary = sys.argv[4]
# @see 读取文件内容
def readFile(filename):
  content = ""
  try:
    fo = open(filename)
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
rawContent = readFile(sourceFile)
if (engine == 'jieba'):  # 结巴分词
  jieba.load_userdict(dictionary)
  seg_list = jieba.cut(rawContent, cut_all=False)
  writeFile(targetFile, " ".join(seg_list))
elif (engine == 'thulac'):
  # 分词
  thu1 = thulac.thulac(user_dict=dictionary, seg_only=True)
  thu1.cut_f(sourceFile, targetFile) # 文本文件分词
else:
  print "分词引擎不存在:" + dictionary 

print "###### Segment Finish ######"
