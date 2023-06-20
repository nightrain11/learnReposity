# Normal Command Collect
- upload file to server
```shell
 sudo scp -i ~/.ssh/chuangwang ./cc-net-test:1.0  chuangwang@42.192.20.81:~
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