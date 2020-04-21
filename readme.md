# this is a demo for device manager
  ## application 
   application layer is for users to post device data to add to the system
   and communicate with the mock controller
  ## mock controller
   a mock controller for testing the application
   
#module
```lua
demo
├── api -- 用于编写 http-request-handler
├── base -- 基础包 包含基础的数据模型，http客户端的封装，以及自定义的Application
├── db-- 数据库连接配置及基础方法 
├── mock -- 用于测试的虚拟controller服务器[8081]
├── model -- 数据模型
├── script -- 脚本 目前仅有数据库生成脚本
├── swagger -- swagger 文件目录
├── huey -- 通过huey实现异步队列机制，实现异步消息通知 [huey](https://huey.readthedocs.io/en/latest/)
└── 
```
## 程序入口为
   ##API
    main.py 
   ##MOCK_SERVER
    mock/main.py
   ##client
    client/mock_client
   ##huey
    huey_consumer -w 16 huey_app.huey

## 数据库配置
   db __init__.py
  
## 