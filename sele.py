from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class UseSele:
    def __init__(self,url):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Desktop\\chromedriver_win32\\chromedriver.exe")
        try:
            self.driver.get(url)
        except:
            self.driver.close()

    def gethtml(self):
        html = self.driver.page_source
        self.driver.close()
        return html.encode("utf-8")

    #for this proj the csss=span.item-link.name__copytext
    def waitEleme(self,csss):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,csss ))
        )
            html = self.driver.page_source
            return html.encode("utf-8")

        except:
            return "Error in the wait Elem func"
