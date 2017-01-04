# this code counts difference between number of open and close brackets
# the same result, in two solutions

str = ']}}}}[dsfgdsf(sdfg{dfsg}dfg}dsfg(dsfgh)sdhgf}SDhgf}]sdhg[dsfg[dsfh}dshgf'
br = ['[', ']', '(', ')', '{', '}']
# first solution
a = 0
for i in str:
 if i in br[0::2]:
  a = a + 1
#  lst.append(i)
 if i in br[1::2]:
  a = a - 1
#  lst.pop()
print a

# second solution
b = sum(list(x in br[0::2] for x in str)) - sum(list(x in br[1::2] for x in str))
print b