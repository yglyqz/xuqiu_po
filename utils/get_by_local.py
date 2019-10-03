from appium.webdriver.webdriver import WebDriver

from utils.read_ini import ReadIni

class GetByLocal:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.read_ini = ReadIni()

    def get_element(self, key):
        local = self.read_ini.get_value(key)
        by = local.split('>')[0]
        local_by = local.split('>')[1]
        if by == "id":
            return self.driver.find_element_by_id(local_by)
        elif by == "class":
            return self.driver.find_element_by_class_name(local_by)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(local_by)