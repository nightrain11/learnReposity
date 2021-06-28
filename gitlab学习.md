# **1.git常用命令学习**
+ df-h 查询硬盘容量  
--------
 **远程服务器**
+ ssh ci_tester@10.1.205.38 链接远程服务器
+ scp ci_tester@10.1.205.38:~/*.tar.gz 远程copy后缀为tar.gz的文件
+ scp -r *.tar.gz ci_tester@10.1.205.38:~将本目录下.tar.gz文件copy到远程服务器的home目录下
+ exit 退出远程服务器  
--------
**git log 和git reflog**  
+ git log 命令可以显示所有提交过的版本信息  
  
+ git reflog可以查看所有分支的所有操作记录（包括已经被删除的 commit 记录和 reset 的操作）例如执行 git reset --hard HEAD~1，退回到上一个版本，用git log则是看不出来被删除的commitid，用git reflog则可以看到被删除的commitid，我们就可以买后悔药，恢复到被删除的那个版本。
  
  

