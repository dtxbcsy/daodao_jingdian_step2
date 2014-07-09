import os
import sys
import re

trim_pat_1=re.compile(r'[\n\r\t]',re.S|re.M)
trim_pat_2=re.compile(r'>[ ]*?<',re.S|re.M)

recommend_pat_1=re.compile(r'<div class="title"><a href="(/Attraction_Review.*?)" class="property_title" onclick="(.*?)">',re.S|re.M)

fi=open(sys.argv[1],"r")
text=fi.read(1024*1024)
fi.close()
text=trim_pat_1.sub('',text)
text=trim_pat_2.sub('><',text)

recommend_ret_1=recommend_pat_1.findall(text)

for r in recommend_ret_1:
	print r[0]+"\t"+r[1]
