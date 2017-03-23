import re
from bs4 import BeautifulSoup as BS


html = ''
with open('111.html') as f:
    for line in f:
        html += line

f = re.findall("<.*>Color by:.*<span.*span>", html, flags=re.DOTALL)
f = re.findall("<.|\n*>", html)
f = re.findall("(Color by:){1}(\n|.)*(<span.*span>)*", html)
f = re.findall("((Color by:)((\n|.){0,100})(<span.*span>))", html)


# f = re.findall("<.+>Color by:[.\t\n\r]*<span.*span>", html)
# f = re.findall("<.+>Color by:<span.*span>", html)
print len(f)
print len(f[0])
print f

# print len(f)
# for i in f:
#     print i


# controls = []
# for el in f:
#     c = el.strip().split('\n')
#     soup = BS(c[0], "html.parser")
#     name = soup.text
#     soup = BS(c[1], "html.parser")
#     id = soup('span', id=True)[0]['id']
#     controls.append((name, id))
#     print name, id

