from selenium import webdriver

browser = webdriver.Chrome()
if __name__ =='__main__':
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')

