import sys
from time import sleep
from appium import webdriver
from utils.read_ini import ReadIni
from utils.get_by_local import GetByLocal
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
        self.get_by_local = GetByLocal(self.driver)
        # value = read_ini.get_value("login_mor")

    def teardown(self):
        self.driver.quit()

    def test_wrong_phone(self):
        self.get_by_local.get_element("profile_icon").click()
        self.get_by_local.get_element("login_more").click()
        self.get_by_local.get_element("username").send_keys("123456")
        self.get_by_local.get_element("password").send_keys("123456")
        self.get_by_local.get_element("login_button").click()
        sleep(2)
        assert "手机号码填写错误" == self.driver.find_element_by_id("md_content").get_attribute("text")
