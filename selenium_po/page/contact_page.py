import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_po.page.basepage import BasePage


class ContactPage(BasePage):
    def click_add_member(self):

        from selenium_po.page.add_member_page import AddMemberPage
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # 显示等待，等待元素是可点击状态
        self.wait_for_click(ele,5)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        # 解决点击无效问题；设置死循环多次点击，直到目标元素出现后，跳出死循环
        while True:
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            element = self.finds(By.ID,"username")
            if len(element) > 0:
                break
        return AddMemberPage(self.driver)
    def get_member(self):

        time.sleep(3)
        eles = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in eles:
            # 获取元素属性title的值，存入list内
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        # 断言目标名字是否在列表内
        return name_list