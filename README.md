一、code目录下执行，Dockerfile生成新的镜像 

docker build -t jimmy_locust .


二、执行docker-compose.yml文件，worker跑4个，其他跑1个

docker-compose up --scale worker=4

三、配置试图
1.输入http://localhost:9090打开prometheus

2.prometheus中输入up再Execute

3.输入http://localhost:3000打开grafana

4.设置->Data Sources添加prometheus数据源

5.创建->Import，输入ID(12081为locust、11074为linux监控)，Load

6.数据选择prometheus后Import即可
