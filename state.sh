DATAPATH=data

for file in `cat input`
do
a=`ls $DATAPATH/$file/*.html | wc -l`
b=`ls -l $DATAPATH/$file/*.html | awk '$5>0' | wc -l`
printf "%s\t%s\t%s\n" $a $b $file | awk -F"\t" '{print $1"\t"$2"\t"$2/$1"\t"$3}'
done

