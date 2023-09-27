# Normal Command Collect
- upload file to server
```shell
 sudo scp -i ~/.ssh/chuangwang ./cc-net-test:1.0  chuangwang@42.192.20.81:~
```

- download file from server(现代文学名著)
```shell
sudo scp -i ~/.ssh/chuangwang chuangwang@42.192.20.81:/mnt/nfs/dev-aigc-6/data3/feihao/src/cbook/open/book数据集/借鉴书籍/现代文学名著/* ~/cbook
```

- 连接远程电脑
```shell
ssh bat@10.1.202.117
```

- find news string in file,and show line number
```shell
grep -n news ./cc-cn-hosts.txt.sort

grep news ./cc-cn-hosts.txt.sort > filter_news.txt
```
- 100 <line<120
```shell
cat cc-cn-hosts.txt.sort |tail -n +100|head -n 20
```
- read file line count
```shell
wc -l cc-cn-hosts.txt.sort
```
- process in linux
```shell
ps x /ps a
```
- count host name,and sort host by count
```shell
time cat cc-cn-hosts.txt|sort|uniq -c|sort -k1 -n -r >cc-cn-hosts.txt.sort
```

- extract title field from json
```shell
sudo cat output/*.json|jq ".title" > clean_titles.txt
```

extract title and find in json
```shell
cat clean_titles.txt |awk '{print $2}' | xargs -i grep '"title": *"{}"' *.json
```

#delete the title in txt, 

```shell
sudo cat filter_title.txt | awk -F'"' '{print $2}' | xargs -t -i sudo sed -i '/"title": *"{}"/d' ./text.txt
```

- change folder owner
```shell
sudo chown -R chuangwang:chuangwang /mnt/nfs/dev-aigc-20/data1/chuangwang
```

- calcutate the folder size and sort
```shell
du -sh *|sort -n
```

- 分割大文件zhihu.log，40000行一个文件，名称以zhihu_开头，序号是四位数字
```shell
split -l 40000 ../zhihu.log -d -a 4 zhihu_
```
- 批量改名

```shell
for name in `ls *.json`;do mv $name ${name#*_*_*_};done
```

```shell
for name in `ls cbook_pdf/*.pdf`;do pdftotext name ./cbook_text/${name}.txt;done
```

```shell
Ctrl+a 可以使光标移到最前面 Ctrl+e 可以使光标移到最后面 
```

- 以“为分割符号分割字符串，并取第二个字段。
```shell
cat ./book_title.sort | cut -d'"' -f2 > book_title.sort

```

- 更改git默认的编辑器为vi
```shell
git config --global core.editor vi
```
- 提交代码
```shell
git push origin HEAD:refs/for/master
```