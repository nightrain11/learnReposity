
#upload file to server
sudo scp -i ~/.ssh/chuangwang ./cc-net-test:1.0  chuangwang@42.192.20.81:~

#find news string in file,and show line number
grep -n news ./cc-cn-hosts.txt.sort

sudo grep news ./cc-cn-hosts.txt.sort > filter_news.txt

# 100 <line<120
cat cc-cn-hosts.txt.sort |tail -n +100|head -n 20

#read file line count
wc -l cc-cn-hosts.txt.sort

#process in linux
ps x /ps a

#count host name,and sort host by count
time cat cc-cn-hosts.txt|sort|uniq -c|sort -k1 -n -r >cc-cn-hosts.txt.sort