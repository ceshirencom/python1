import pytest

from selenium_po.page.basepage import BasePage
from selenium_po.page.main_page import MainPage


class TestLogin():
    def setup(self):
        self.main = MainPage()
    def teardown(self):
        pass
    @pytest.mark.parametrize("name,id,mail",[("嬴政12","123331111","11185123333@qq.com")])
    def test_login(self,name,id,mail):
        # name = "与其秒1"
        # id= "1234441"
        # mail = "23455599@qq1.com"
        namelist = self.main.goto_contact_page().click_add_member().add_member(name,id,mail).get_member()
        print(namelist)
        assert "嬴政12" in namelist