awk -F"\t" '{print "http://www.daodao.com"$1}' data/*/*.output > release
