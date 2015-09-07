import os
import sys
import jieba.posseg as pseg
reload(sys)
sys.setdefaultencoding("utf-8")
def read_path(folder_path):
	namelist = os.listdir(folder_path)
	pathlist=[]
	for i in range(len(namelist)):
		strs = folder_path + namelist[i]
		pathlist.append(strs)
	return pathlist,namelist

def write_output(writepath,output):
	files=open(writepath,'a+')
	for i in range(len(output)):
		files.write(str(output[i]))
		files.write('\t')
	files.close()


def read_txt(path):
	files=open(path)
	raw = files.readlines()
	files.close()
	for i in range(2,len(raw)):
		raw[i]=raw[i].strip('\n')
	content = ''.join(raw)
	return content

def fenci(content):
	wp=pseg.cut(content)
	wd=[]
	cha=[]
	for word,flag in wp:
		wd.append(word)
		cha.append(flag)
	noun =[]
	for i in range(len(wd)):
		if cha[i][0]=='n':
			noun.append(wd[i])
	return noun




folder_path ='/tmp/Normal-Data/normal-cn/'
path,namelist = read_path(folder_path)
for i in range(len(path)):
	print i
	content = read_txt(path[i])
	noun = fenci(content)
	writepath = '/tmp/result/'+namelist[i]
	write_output(writepath,noun)



