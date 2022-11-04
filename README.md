# deepface_docker
使用deepface做的人脸对比api接口， docker容器内置运行deepface所需的环境，仅linux环境下使用

## 生成镜像
在`deepface_docker`的目录下运行，生成文件
```shell
docker build -t "deepface" .
```

## 生成容器
```shell
docker run --name deepface -d -p 5000:5000 deepface:latest
```

## 运行

- 测试验证接口

```shell
curl http://127.0.0.1:5000/face_verify
```

- 人脸对比api接口，传入参数img1、img2

```shell
curl -X POST -F 'img1=xxxxxx' -F 'img2=xxxx' http://127.0.0.1:5000/face_verify
```

## 代码许可

The MIT License (MIT).详情见 [License文件](https://rem.mit-license.org/).

