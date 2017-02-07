import re

str = " h.1.2.3.4 h k 1.2.33.5.36 jhk j"
# x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2(5[0-5]|[0-4]\d))'
# IpRegExp = "^(" + x + "\.){3}" + x + "$"
IpRegExp = "(" + x + "\.){3}" + x
aa = re.finditer(IpRegExp, str)
lst = []
print aa
for i in aa:
    lst.append(i.group())
print lst






