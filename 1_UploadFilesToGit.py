from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import time

login = r''
password = r''
repository = [r'', r'']
folderWithFiles = r''

opts = webdriver.ChromeOptions()
opts.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=opts, executable_path = "C:\Users\fff\Downloads\chromedriver.exe")
driver.set_window_position(0, 0)
driver.get(r'https://github.com/login')
driver.find_element_by_id('login_field').send_keys(login)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('password').send_keys(Keys.ENTER)

driver.get(r'https://github.com/' + login + '/' + repository[1] + '/upload/master')

def wait():
    # print driver.find_element_by_css_selector('.repo-file-upload-meter.js-upload-meter').get_attribute('style')
    while True:
        try:
            # print driver.find_elements_by_class_name('repo-file-upload-meter js-upload-meter')[0]
            time.sleep(1)
            if driver.find_element_by_css_selector('.repo-file-upload-meter.js-upload-meter').get_attribute('style') == 'width: 100%;':
                break
        except:
            pass

addFile = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/form[2]/div[2]/p/input')
for file in glob.glob(folderWithFiles + '\*.py'):
    addFile.send_keys(file)
    wait()
    print 'added ' + file

driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/form/button').click()

time.sleep(2)
driver.close()
