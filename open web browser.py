#  -*- coding: utf-8 -*-

import sys
sys.path.append("C:\Python Libs")
sys.path.append("C:\Python Libs\win32\lib")
sys.path.append("C:\Python Libs\win32com")
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver


opts = webdriver.ChromeOptions()
opts.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
opts.add_argument("--test-type")
ie = webdriver.Chrome(chrome_options=opts, executable_path = "C:\Users\dhql\Downloads\chromedriver.exe")
ie.implicitly_wait(30)
ie.get("http://www.google.com")
#ie.get("http://spotfire-wp-dev-hou.chevron.com/spotfire/wp/render/759032260797/analysis?file=/ITC/CS/CSRMAR/Analysis%20Files/Cyber%20Scorecard/Cyber%20Scorecard%20v0.1.028")
#print ie.execute_script("/spotfire/wp/resources/min/webplayer-lib.js?3a2d6de")
html = ie.page_source

with open("newfile.txt", "w") as f:
    f.write(html.encode('utf-8'))

try:
    ie.switch_to_alert().text
except NoAlertPresentException:
    print ('Success!')
for i in ie.find_elements_by_tag_name('a'):
    try:
        print (i.text.encode('utf8'))
    except NoAlertPresentException:
        print ('no name')

#doesn't work yet
from selenium.webdriver.common.keys import Keys
#help(Keys)
ie.implicitly_wait(5)
el = ie.find_element_by_tag_name("a")
print 111, el.text, '********************'
ie.implicitly_wait(5)
el.send_keys(Keys.F1)
