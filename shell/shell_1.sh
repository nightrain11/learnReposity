
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

#vim指定要删除的行范围
.（当前行）
$（文件中的最后一行）
%（所有行）

:10,45d- 从第 10 行删除到第 45 行
:.,$d- 从当前行删除到最后一行
:.,1d- 从当前行删除到文件开头
:dgg- 从当前行删除到文件开头
#删除第9行到第200行的内容(先用200G转到第200行) 
:9,.d 

#vim转到文件结尾
G  
#或转到第9行
9G

# stress 命令会创建一个进程并通过 malloc 函数分配内存
stress --vm 1 --vm-bytes 500M