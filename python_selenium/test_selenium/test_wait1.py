from time import sleep

from selenium import webdriver


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def test_wait(self):
        # self.driver.find_element_by_xpath('//*[@id="ember406"]').click()
        sleep(3)
        print("hello world!")
