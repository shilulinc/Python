## README  
#### 介绍  
这是一个模拟购物车的简易程序  
- Author: Shi Lu  
- Date: 2017-12-17  
- Funtion  
此程序分为用户入口和商家入口  
用户入口：  
一.用户登陆部分：  
用户输入后判断是否为首次登陆，如果用户在已有文件中则欢迎登陆，否则视为首次登陆，并把用户信息写入文件中。  
二.购买商品部分：  
1.如果用户查询已购买商品，如果首次登陆则为空，否则显示已购商品，并提示继续购买，最后打印余额和所购商品。  
2.如果用户输入的内容为商品编号，则商品加入购物车，并打印余额，否则，提示商品不存在。  
3.有退出等功能。   
商家入口：  
1.输入A增加商品，写入商品信息文件。  
2.输入C修改商品价格，并重新生成商品信息文件。  
3.有退出等功能。  
#### 环境依赖  
- Python 3.0+  
#### 关于移植  
- 此程序可以在安装有Python 3.0+的Linux、Windows、macOS上互相移植  
#### 作业特性  
- 函数调用  
- 代码嵌套  
- 数据类型转换  
- 循环  
### 重要的Python文件  
- 已有的用户信息文件：users_info  
- 已有的用户已购商品信息文件：shopping_info  
- 可购买的商品信息文件：goods_info  
- 项目介绍文件：README.md
- 代码文件：shopping.py  
#### 如何执行  
- 在命令行中直接用`Python3 shopping.py`执行此程序  
#### 个人感想  
1.构思各功能  
2.画出流程图  
3.用代码实现  
#### 个人博客和GitHub地址  
- [博客园地址](http://www.cnblogs.com/shilu/)  
- [GitHub代码和README](https://github.com/shilulinc/Python/tree/master/)  
