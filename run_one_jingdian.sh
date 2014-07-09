url="http://www.daodao.com/$1"
DATAPATH=/search/zf/bh2_3/data/$1
page=$DATAPATH/$1
mkdir $DATAPATH

##get first page
for((t=0;t<10;t++))
do
	sh /search/zf/proxy/wget.sh $url $page
	python getDetail.py $page 1> $page.output
	##get pagination url
	python getPaginationUrls.py $page $1 > $page.paginations
	
	if [ -s $page.output ]
	then
		break
	fi
done
##get paginations page
for key in `cat $page.paginations`
do
url="http://www.daodao.com/$key"
page=$DATAPATH/$key
for((t=0;t<10;t++))
do
	sh /search/zf/proxy/wget.sh $url $page
	python getDetail.py $page 1> $page.output

	if [ -s $page.output ]
	then
		break
	fi
done
done
