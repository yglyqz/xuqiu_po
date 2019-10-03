import sys
from time import sleep
from appium import webdriver
from utils.read_ini import ReadIni
sys.path.append("/Users/liyang/liyang/xueqiu/xueqiu_po")

class TestBaseDriver:
    def setup(self):
        capabilities = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": True,
            "noReset": True,
            "automationName": "UiAutomator2",
            # "chromedriverExecutable": "/Users/liyang/liyang/chrome_driver/chrome_20",
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        self.driver.implicitly_wait(10)
        self.read_ini = ReadIni()
        # value = read_ini.get_value("login_mor")

    def teardown(self):
        self.driver.quit()

    def test_wrong_phone(self):
        self.driver.find_element_by_id(self.read_ini.get_value("profile_icon")).click()
        self.driver.find_element_by_id(self.read_ini.get_value("login_more")).click()
        self.driver.find_element_by_id(self.read_ini.get_value("username")).send_keys('123456')
        self.driver.find_element_by_id(self.read_ini.get_value("password")).send_keys('123456')
        self.driver.find_element_by_id(self.read_ini.get_value("login_button")).click()
        sleep(2)
        assert "手机号码填写错误" == self.driver.find_element_by_id("md_content").get_attribute("text")
