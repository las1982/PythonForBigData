import re

str = "q 1.2.3.4 h k 1.2.3.5 jhk j"
x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
# x = '([0-9]|[1-9][0-9]|1[0-9]{2}|2(5[0-5]|[0-4]\d))'
# ValidIpAddressRegex = "^(" + x + "\.){3}" + x + "$"
IpRegExp = "(" + x + "\.){3}" + x
# ValidIpAddressRegex = "(.+\s+)(" + x + "\.){3}" + x + "\s+.+$"
# ValidIpAddressRegex = "(" + x + "\.){3}" + x + "$"
# ValidIpAddressRegex = '([12]{0,1}\d{1,2}(\.|$|\S+)){4}'
# ValidIpAddressRegex = '\d{1,2}|1\d{2}|2(5[0-5]|[0-4]\d)'
# aa = re.match(ValidIpAddressRegex, ip)
aa = re.search(IpRegExp, str)
print aa.group()

# print aa.group()
#
# aaa = re.findall(ValidIpAddressRegex,ip)
# print aaa
#
# s= "a a a"
# s = 'aa a'
# d = re.search('.+? ',s)
# d = re.search('a\s*a', s)
# print d.group(0)





