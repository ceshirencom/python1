# Generated by Selenium IDE
import pytest
import time

import yamltest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDmeo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path =r"C:\Users\ASUS\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    self.driver.implicitly_wait(20)
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  # def test_dmeo(self):
  #   self.driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")
  #   self.driver.set_window_size(1382, 744)
  #   self.driver.find_element(By.ID, "kw").click()
  #   # time.sleep(3)
  #   self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
  #   self.driver.find_element(By.ID, "su").click()
  #   self.driver.close()




# def test_wework():
#   opt = webdriver.ChromeOptions()
#   opt.debugger_address = "127.0.0.1:9222"
#   driver = webdriver.Chrome(options=opt)
#   driver.implicitly_wait(10)
#   driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#   driver.find_element_by_id("menu_contacts").click()
#   time.sleep(3)
#   driver.quit()

  def test_get_cookie(self):
    self.driver.get("http://work.weixin.qq.com/")
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    self.driver = webdriver.Chrome(options=opt)
    # self.driver.implicitly_wait(10)
    cookies = self.driver.get_cookies()
    with open("data.yaml","w",encoding="utf-8") as f:
      yaml.dump(cookies,f)


  def test_login(self):
    # self.driver = webdriver.Chrome()
    self.driver.get("https://open.work.weixin.qq.com/wwopen/sso/qrConnect?appid=wwe1a7286ef7d960c6&agentid=1000003&redirect_uri=http://boss.city.qq.com/&state=boss")
    with open("data.yaml",encoding = "utf-8") as f:
      yaml_date = yaml.safe_load(f)
    # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'bDIOCR8QVEVXYub5dw4TJk_CRIX6i1JBGoH-gntKN_0q41Luv4vZE4shul4k_XxnsoDaoNjbUk8U5UbS9mUIArTHTGgZ_QCvZa7SmoT95-4Gm4Aw0IHpw_2re-xTt7qcDULPHSLQSisQXzp-oHXTo6kUEobpOvyl5tE6G9YfqP7SIdxvVqbharRdVjf3lm22WrG-j4lylYGi22Lglt_6xXqrvcOpWfjuWTeDdy2dCIwHLHU5xa12PCGeopQlt1wLe4pR8WSYOTcawMpuWMCYjw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'qLb8OlT6e1Ri4_kD0TojKVnjQYC8AUXXqW7GDRAY6Hv1ltTefr41XOrvmQHq0jI8'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8663481'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850890686615'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850890686615'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325134205473'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1608610423, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1377764470.1608472565'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608553437, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4douk4t'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '42684348053248232'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640008448, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1671596023, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.173000028.1608472565'}, {'domain': '.work.weixin.qq.com', 'expiry': 1611116026, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
    for cookie in yaml_date:
      self.driver.add_cookie(cookie)
    time.sleep(5)
    self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    self.driver.find_element_by_id("menu_contacts").click()
    self.driver.find_element_by_link_text("添加成员").click()
    self.driver.find_element_by_id("username").send_keys("七月")
    self.driver.find_element_by_id("memberAdd_english_name").send_keys("march")
    self.driver.find_element_by_id("memberAdd_acctid").send_keys("2285")
    self.driver.find_element_by_id("memberAdd_telephone").send_keys("029-44298")
    self.driver.find_element_by_id("memberAdd_mail").send_keys("2285095@qq.com")
    self.driver.find_element_by_id("memberEdit_address").send_keys("陕西省神木市")
    self.driver.find_element_by_id("memberAdd_title").send_keys("测试工程师")
    self.driver.find_element_by_link_text("保存").click()
    test_text= self.driver.find_element_by_id("js_tips").text
    try:
      assert test_text == "保存成功"
      print("添加成员成功了")
    except Exception as e:
      print(f"验证失败：{e}")


