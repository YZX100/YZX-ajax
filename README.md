# YZX-ajax
公众号无限回调系统SQL注入批量检测脚本

![image](https://github.com/user-attachments/assets/5e4f5fae-dda1-4f6d-abe9-c62593eeee5f)

```shell
某信公众平台无限回调系统 /user/ajax.php 接口存在SQL注入漏洞，未经身份验证的远程攻击者除了可以利用 SQL 注入漏洞获取数据库中的信息（例如，管理员后台密码、站点的用户个人信息）之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。

FOFA语句：
body="mb-5 web-font-desc"
使用说明：
-u 指定URL检测单个URL
-f 批量检测
-h 帮助信息
注意：
python3解析器
检测时需要http/https协议
```
