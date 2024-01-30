#host server link to mysql docker
1.sudo docker run -itd --name=mysql156 --restart=always -p 23306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:latest
2.docker exec -it mysql156 bash
3.mysql -u root -p
4.use mysql;
update user set host='%' where user='root';
select user,host from user;
flush privileges;
5.find bridge id between host and docker:ifconfig //find first ip
6.sudo docker network ls  //find all network
7.sudo docker network inspect bridge //find docker ip:172.17.0.4
8.mysql -h 172.17.0.4 -u root -p

#docker link to mysql docker
//first method(not comment,for when docker restart,ip will change)
1.sudo docker network inspect bridge //find docker ip
2.mycli -h 172.17.0.4 -uroot -p 123456 //enter into
//second method(use docker name to link docker)
1.docker network create my_net
2.docker network ls //check is create success
3.docker run --netwrok my-net //start new docker
4. or docker netwok connet my_net dockerName//old docker add net
5.docker inspect my_net //check whether add to docker success
6.mycli -h mysql156 -uroot -p 123456

#login to server mysql
mysql -h150.158.169.158 -P23306 -uroot -p123456

#deploy minio

1. docker pull minio/minio
2. sudo docker run -p 9000:9000 -p 9001:9001 \
    --name psy_minio -e "MINIO_ACCESS_KEY=minioButool"
    -e "MINIO_SECRET_KEY=minioButool" \
    -e "MINIO_ROOT_USER=adminMinio" \
    -e "MINIO_ROOT_PASSWORD=adminMinio"  \
    -v /mnt/nfs/dev-aigc-20/data1/chuangwang/server_data/minio/data/:/data \
    -v /mnt/nfs/dev-aigc-20/data1/chuangwang/server_data/minio/config/:/root/.minio \
    -d minio/minio server --console-address ':9001' -address ":9000" /data

--console-address 指定客户端端口

3. http://150.158.169.158:9000

#这里的9001端口指的是minio的客户端端口。虽然设置9001，但是我们在访问9000的时候，他也会自动跳到9001。
#9000端口是minio的服务端端口，我们程序在连接minio的时候，就是通过这个端口来连接的。

# 打开防火墙端口
firewall-cmd --zone=public --add-port=9000/tcp --permanent
firewall-cmd --zone=public --add-port=9090/tcp --permanent
firewall-cmd --reload

ip:9000
用户名：adminMinio
密码：adminMinio


#deploy redis
sudo docker run --name redis \
    -p 6379:6379 -\
    -restart always \
    -v /redis/data:/data \
    -v /redis/conf/redis.conf:/etc/redis/redis.conf \
    -d redis:latest \
    redis-server /etc/redis/redis.conf --appendonly yes #redis save data to local
#reload redis.conf
redis-cli config rewrite

#登录redis
redis-cli -h 150.158.169.158 -p 6379
#redis learn
#https://blog.csdn.net/u014723137/article/details/125658176


#redis 部署
#1.低版本部署
sudo docker run -itd --name=myredis11 -p 8289:6379  -v ~/redis:/data -d redis:3.0.6 redis-server
#2.高版本部署
wget http://download.redis.io/redis-stable/redis.conf
chmod 777 redis.conf
vi /docker-data/redis/redis.conf
#redis.conf
bind 127.0.0.1 # 这行要注释掉，解除本地连接限制
protected-mode no # 默认yes，如果设置为yes，则只允许在本机的回环连接，其他机器无法连接。
daemonize no # 默认no 为不守护进程模式，docker部署不需要改为yes，docker run -d本身就是后台启动，不然会冲突
requirepass 123456 # 设置密码
appendonly yes # 持久化
sudo docker run -itd --name=myredis4 -p 8288:6379  -v ~/redis/redis.conf:/etc/redis/redis.conf -v ~/redis:/data -d redis redis-server /etc/redis/redis.conf --appendonly yes
#
#redis迁移(重点，redis版本必须保持一致，否则不会生效)
#1.导出rdb文件
redis-cli --rdb /path/to/dump.rdb
#2.将rdb文件放在redis的/data文件夹下
docker cp /path/to/dump.rdb redis:/data/dump.rdb
#3.重启docker
docker exec -it redis redis-cli shutdown
docker start redis

#部署后状态检查
#1.链接容器并执行命令
sudo docker exec -it bcf6f8e71a redis-cli ping
#2.检查容器日志
docker logs bcf6f8e71a
#3.直接命令行检查
redis-cli -h <ip> -p <port> ping

#链接容器并执行命令
sudo docker exec -it 9a80e455b0bc bash -c ls -a
#链接上容器，并在命令行查看实时日志
docker attach 9a80e455b0bc


