import re

str = "q 1.2.3.4 h k 1.2.3.5 jhk j"
x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
# x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2(5[0-5]|[0-4]\d))'
# IpRegExp = "^(" + x + "\.){3}" + x + "$"
IpRegExp = "(" + x + "\.){3}" + x
aa = re.finditer(IpRegExp, str)
for i in aa:
    print i.group()






