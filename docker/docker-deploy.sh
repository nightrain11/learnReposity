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
