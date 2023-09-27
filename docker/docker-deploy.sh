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
mysql -h 150.158.169.158 -P 23306 -uroot -p

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