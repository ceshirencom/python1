from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login():
    opt = webdriver.ChromeOptions()
    opt.debugger_address_address  = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    # driver.get("http://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR,".ww_operationBar .js_add_member")
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(ele))
    while True:
        # ele = driver.find_element_by_css_selector(".ww_operationBar .js_add_member")
        # ele.click()
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id("username")
        if len(element) > 0:
            break
    driver.find_element_by_id("username").send_keys("七ds月")
    driver.find_element_by_id("memberAdd_english_name").send_keys("march")
    driver.find_element_by_id("memberAdd_mail").send_keys("2285d095@qq.com")
    driver.find_element_by_css_selector(".js_btn_save").click()
