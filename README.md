## 本系统采用 Python + Django + Django Channels + bootstrap + Redis 搭建。

### 说明 ###

* Django == 4.0.3
* Channels == 3.0.4
* Redis == 5.0.14
* sqlite3 可改换为 MySQL（见相关注释）

### 关于报错 ###

1. > TypeError: __call__() missing 1 required positional argument: 'send'


    将 *.../compatibility.py* 中的 

    ```python
    async def new_application(scope, receive, send):
        instance = application(scope)
        return await instance(receive, send)
    ```

    改为

    ```python
    async def new_application(scope, receive, send):
        instance = application()
        return await instance(scope,receive, send)
    ```
2. > ConnectionRefusedError: [Errno 10061] Connect call failed ('127.0.0.1', 6379)
    
    * 下载并安装Redis-x64-5.0.14.msi，地址：https://github.com/tporadowski/redis/releases
    * 安装完成后，启动服务（先运行redis-server.exe，再运行redis-cli.exe）
      * 注：程序运行时需保持此服务运行。

3. > 其他报错请自行解决

### 实现功能

 - 用户注册
 - 用户登录验证
 - 查看用户信息和修改当前登录用户的密码
 - 显示所有在线用户和离线用户
 - 用户进入和离开聊天室时发送广播通知
 - 创建临时聊天室并进行实时通信

### test

 * test
   * a@mail 
   * a
 * test1
   * 1@1    
   * 1
 * test2
   * 2@2    
   * 2
 * test3
   * 3@3    
   * 3
