# Author:ShiLU
import getpass
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")

#print (username,password)

_username = "shilu"
_password = "abc123"

if username == _username and password == _password:
    print("Welcome users_info {name} loggin..." .format (name = username))
else:
    print("invalid username or password !")
