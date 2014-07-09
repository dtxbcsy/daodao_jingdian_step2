import os
import sys
import re

trim_pat_1=re.compile(r'[\n\r\t]',re.S|re.M)
trim_pat_2=re.compile(r'>[ ]*?<',re.S|re.M)

recommend_pat_1=re.compile(r'<span class="pgDetail">(.*?)<b>1</b>/(.*?)</span>',re.S|re.M)

fi=open(sys.argv[1],"r")
text=fi.read(1024*1024)
fi.close()
text=trim_pat_1.sub('',text)
text=trim_pat_2.sub('><',text)

recommend_ret_1=recommend_pat_1.findall(text)

if len(recommend_ret_1)!=1:
	sys.exit(0)
else:
	val=recommend_ret_1[0][1][:-3]
	if len(val)==0:sys.exit(-1)
	try:
		val=int(val)
	except:
		val=0

	url=sys.argv[2]

	idx=url.find("-",7)
	if idx==-1:sys.exit(-2)
	url1=url[:idx]
	url2=url[idx:]

	for idx in range(1,val):
		#print "http://www.daodao.com/"+url1+"-oa"+str(idx*15)+url2
		print url1+"-oa"+str(idx*15)+url2
