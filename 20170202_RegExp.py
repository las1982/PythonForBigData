# \S - любой непробельный символ
# . - любой символ
# \d - десятичная цифра
# [фсв] - вхождение одного символа из списка в шаблоне
# [ф-в] - вхождение одного символа из списка в шаблоне
# \d{1,3}

# aa\sbb = 'aa bb' or 'aa \t bb'
# \s+?
# (...|...) alternative

import re

ip="241.1.1.11"
ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
aa = re.match(ValidIpAddressRegex,ip)
print aa.group()