from selenium import webdriver

def gethtml(url):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Desktop\\chromedriver_win32\\chromedriver.exe")
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html
