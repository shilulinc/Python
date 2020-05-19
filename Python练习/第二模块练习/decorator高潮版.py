# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"
"""
user, passwd = "alex", "abc123"
def auth(func):
    def wrapper(*args, **kwargs):
        username = input("username:").strip()
        password = input("password:").strip()
        if username == user and password == passwd:
            print("\033[32;1mUser has passd authtication!\033[0m")
            func(*args, **kwargs)
        else:
            print("\033[31;1mInvalid user or password!\033[0m")
    return wrapper

def index():
    print("welcome to index page!")

@auth
def home():
    print("welcome to home page!")
    return "from home"  # 此函数中没有返回结果
@auth
def bbs():
    print("welcome to bbs page!")
index()
print(home())
bbs()
user, passwd = "alex", "abc123"
def auth(func):
    def wrapper(*args, **kwargs):
        username = input("username:").strip()
        password = input("password:").strip()
        if username == user and password == passwd:
            print("\033[32;1mUser has passd authtication!\033[0m")
            func(*args, **kwargs)
        else:
            print("\033[31;1mInvalid user or password!\033[0m")
    return wrapper

def index():
    print("welcome to index page!")

@auth
def home():
    print("welcome to home page!")
    return "from home"  # 此函数中没有返回结果
@auth
def bbs():
    print("welcome to bbs page!")
index()
print(home())
bbs()
"""

user, passwd = "alex", "abc123"
def auth(auth_type):
    print("auth func:", auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input("username:").strip()
                password = input("password:").strip()
                if username == user and password == passwd:
                    print("\033[32;1mUser has passd authentication!\033[0m")
                    res = func(*args, **kwargs)  # 相当于"from home"
                    print("after authentication!".center(50, "-"))
                    return res
                else:
                    print("\033[31;1mInvalid user or password!\033[0m")
            elif auth_type == "ldap":
                print("ldap".center(50, "-"))
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page!")

@auth(auth_type = "local")  # home = wrapper()
def home():
    print("welcome to home page!")
    return "from home"

@auth(auth_type = "ldap")
def bbs():
    print("welcome to bbs page!")

index()
print(home())
bbs()
