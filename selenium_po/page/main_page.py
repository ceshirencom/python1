from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_po.page.basepage import BasePage
from selenium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_contact_page(self):

        self.find(By.ID,"menu_contacts").click()
        return ContactPage(self.driver)