import urllib2
import requests
class MyAuth(requests.auth.AuthBase):
     def __call__(self, r):
         # Implement my authentication
         return r
url = 'http://spotfire-wp-dev-hou.chevron.com/spotfire/wp/startPage#/libraryBrowser'
print requests.get(url, auth=MyAuth())

#***************************************************************************************************************************

import urllib2
wiki = 'http://chevron.com'
page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
print soup

#***************************************************************************************************************************

import requests
from requests.auth import HTTPBasicAuth
response = requests.get('http://spotfire-wp-dev-hou.chevron.com/spotfire/login.html')
if response.status_code == 401:    
    response = requests.get('http://spotfire-wp-dev-hou.chevron.com/spotfire/login.html', auth=HTTPBasicAuth('CT\dhql', ''))
if response.status_code != 200:
    print 'sss'
print 'qqq'

#***************************************************************************************************************************

import os
import urllib2
from ntlm import HTTPNtlmAuthHandler
user = '%s\%s' % ( os.environ["USERDOMAIN"], os.environ["USERNAME"] )
passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
print user
#passman.add_password(None, server, user, password)

#***************************************************************************************************************************

import requests

#USERNAME = 'DHQL@ct.chevrontexaco.net' # put correct usename here
USERNAME = 'CT\dhql' # put correct usename here
PASSWORD = '57831' # put correct password here

LOGINURL = 'http://spotfire-wp-dev-hou.chevron.com/spotfire/login.html'
DATAURL = 'http://spotfire-wp-dev-hou.chevron.com/spotfire/wp/startPage#/libraryBrowser?id=f650b861-60c9-4a3b-9156-ca3adba56a84'

session = requests.session()

req_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

formdata = {
    'UserName': USERNAME,
    'Password': PASSWORD,
    'LoginButton' : 'Login'
}

# Authenticate
r = session.post(LOGINURL, data=formdata, headers=req_headers, allow_redirects=False)
print r.headers
print r.status_code
print r.text

# Read data
r2 = session.get(DATAURL)
print "___________DATA____________"
print r2.headers
print r2.status_code
print r2.text

#***************************************************************************************************************************

import kerberos
import requests
r = requests.get("http://spotfire-wp-dev-hou.chevron.com/spotfire")
r.status_code

print r.headers["www-authenticate"]

def www_auth(response):
    auth_fields = {}
    for field in response.headers.get("www-authenticate", "").split(","):
        kind, __, details = field.strip().partition(" ")
        auth_fields[kind.lower()] = details.strip()
    return auth_fields
print www_auth(r)
#{'negotiate': '', 'basic': 'realm="GlobalSync: Kerberos Login"'}

r = requests.get("http://spotfire-wp-dev-hou.chevron.com/spotfire")
print r.status_code == 401 and www_auth(r).get('negotiate') == ''
#True
r = requests.get("http://spotfire-wp-dev-hou.chevron.com/spotfire")
print r
print r.status_code == 401 and www_auth(r).get('negotiate') == ''
#False

__, krb_context = kerberos.authGSSClientInit("HTTP//:spotfire-wp-dev-hou.chevron.com@spotfire-wp-dev-hou.chevron.com")
print krb_context
kerberos.authGSSClientStep(krb_context, "")
#0
negotiate_details = kerberos.authGSSClientResponse(krb_context)

headers = {"Authorization": "Negotiate " + negotiate_details}
r = requests.get("https://spotfire-wp-dev-hou.chevron.com/spotfire", headers=headers)
r.status_code
#200
r.json
#["example_data"]

#****************************************now we have logining and redirection, then nothing yet***********************************************************************************

import requests
from requests_ntlm import HttpNtlmAuth

session = requests.Session()
session.auth = HttpNtlmAuth('CT\\dhql','0912', session)
response = session.get('http://spotfire-wp-dev-hou.chevron.com')
cookies = response.cookies

print '1  ', response
print '2  ', dir(response)
print '3  ', response.headers
print '4  ', response.is_redirect
print '5  ', dir(response.cookies)
#response = session.get('http://spotfire-wp-dev-hou.chevron.com/spotfire/wp/OpenAnalysis?file=aa1fe76b-fda7-4589-8449-583a54eaea53', cookies=cookies)

#*******************************************Just open ne browser window********************************************************************************

import webbrowser

ie = webbrowser.get(webbrowser.iexplore)
ie.open('http://spotfire-wp-dev-hou.chevron.com/spotfire/wp/render/759032260797/analysis?file=/ITC/CS/CSRMAR/Analysis%20Files/PCN%20Vulnerability/PCN%20Vulnerability%20Analyst%20v0.0.018')

#***************************************************************************************************************************

import sys
sys.path.append("C:\Python Libs")
sys.path.append("C:\Python Libs\win32")
sys.path.append("C:\Python Libs\win32com")
import win32com
import IEC
import pywinauto
import win32com

# Creates a new IE Window
ie = IEC.IEController(window_num=0)

# Register application as an app for pywinauto
shell = win32com.client.Dispatch("WScript.Shell")
pwa_app = pywinauto.application.Application()
w_handle = pywinauto.findwindows.find_windows(title=u'<Title of the site - find it using SWAPY>', class_name='IEFrame')[0]
window = pwa_app.window_(handle=w_handle)
window.SetFocus()

# Click on the download link
ie.ClickLink('gdshfgdhf')

# Get the handle of the Open Save Cancel dialog
ctrl = window['2']

# You may need to adjust the coords here to make sure you hit the button you want
ctrl.ClickInput(button='left', coords=(495, 55), double=False, wheel_dist=0)

#***************************************************************************************************************************

import win32com
import IEC
import pywinauto
import win32com

w_handle = pywinauto.findwindows.find_windows(title=u'Untitled - Notepad')
print w_handle
app = pywinauto.application.Application().connect(handle = w_handle[0])
print app
window = app.window_(handle=w_handle[0])
print window
print window.SetFocus()
print dir(window)
print window.print_control_identifiers()
dlg = app.top_window_()
dialogs = app.windows_()
print app.dlg.control
print app['dlg']['control']
print app.dialog_msctls_statusbar32_ident.Click()


# # getting list of all windows
# app = pywinauto.application.Application().connect(process = 6980)
# handles = pywinauto.findwindows.find_windows()
# for w_handle in handles:
    # wind = app.window_(handle=w_handle)
    # print wind.Texts()
	
#****************************************************************************************************

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.binary_location = "C:\PortablePrograms\GoogleChromePortable\GoogleChromePortable.exe"
print dir(opts)
opts.add_argument("--test-type")
driver = webdriver.Chrome(chrome_options=opts, executable_path = "C:\Users\dhql\Downloads\chromedriver.exe")

#driver = webdriver.Ie()
#driver.implicitly_wait(10) # seconds
driver.get("https://www.Yahoo.com")
#print (dir(driver))
#print (driver.find_elements())
print (driver.title)
assert 'Yahoo' in driver.title
#print (driver.title)
#print (dir(driver))
#driver.implicitly_wait(20)
#print (driver.back())

driver.maximize_window()
myDynamicElement = driver.find_element_by_id("uh-search-box")
elem = driver.find_element_by_name("p")  # Find the search box
elem.send_keys("seleniumhq" + Keys.RETURN)

driver.quit()
