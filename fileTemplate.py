# -*- coding: utf-8 -*-
__author__ = 'lwl'

import re

class FileTemplate(object):
    def __init__(self):
        self.TemplateName=''
        self.TargetPath=''

    def domain(self,itemsDict):
        try:
            fd = open(self.TemplateName,'r')
            buf = fd.read()
            checkPattern = re.compile("\{\{\s*(\w*?)\s*\}\}")
            checkResult = re.findall(checkPattern,buf)
            dropList = [i for i in checkResult if i not in itemsDict.keys()]
            if dropList:
                return (1,'params:%s has not item input'%(','.join(dropList)))
            for k,v in itemsDict.items():
                pattern = re.compile("\{\{\s*"+str(k)+"\s*\}\}")
                buf = pattern.sub(str(v),buf)
            fdWrite = open(self.TargetPath,'w')
            fdWrite.write(buf)
            return (0,'dealwith ok')
        except FileNotFoundError:
            return (2,'the file is not exist')
        except Exception as e:
            return (3,'the Exception %s'%e)
        finally:
            if 'fd' in locals():
                fd.close()
            if 'fdWrite' in locals():
                fd.close()

class FileDelBlock(object):
    def __init__(self):
        self.TemplateName=''
        self.TargetPath=''

    def domain(self,otemsList):
        try:
            fd = open(self.TemplateName,'r',encoding='utf-8')
            buf = fd.read()
            for i in otemsList:
                checkPattern = re.compile('\{\[\s*'+str(i)+'\s*\]\}.*\{\[\s*'+str(i)+'\s*\]\}',re.S)
                buf = checkPattern.sub('',buf)
            fdWrite = open(self.TargetPath,'w',encoding='utf-8')
            fdWrite.write(buf)
            return (0,'dealwith ok')
        except FileNotFoundError:
            return (2,'the file is not exist')
        except Exception as e:
            return (3,'the Exception %s'%e)
        finally:
            if 'fd' in locals():
                fd.close()
            if 'fdWrite' in locals():
                fd.close()

'''
file1=FileTemplate()
file1.TemplateName='config.xml'
file1.TargetPath='config1.xml'
file1.domain({'freeapp':'husanyiyuan','name':'你好'})

file2=FileDelBlock()
file2.TemplateName='tabs.html'
file2.TargetPath='tabs2.html'
file2.domain(['home'])
'''