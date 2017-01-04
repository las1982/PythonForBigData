str = '[sdf]sdf)SDf {Sdf}s sdf]sdf]{sd f]sdf{sd} sf {'
br = ['[', ']', '(', ')', '{', '}']

a = sum(x in br[0::2] for x in str) - sum(x in br[1::2] for x in str)
print a
