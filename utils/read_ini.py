

import configparser

# read_ini = configparser.ConfigParser()
# read_ini.read("/Users/liyang/liyang/xueqiu/xueqiu_po/config/Localelement.ini")
# print(read_ini.get("db", "db_host"))

class ReadIni:
    def __init__(self, file_path=None):
        if not file_path:
            self.file_path = "/Users/liyang/liyang/xueqiu/xueqiu_po/config/Localelement.ini"
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_value(self, key, section=None):
        if not section:
            section = "login_element"
        try:
            value = self.data.get(section, key)
        except Exception as e:
            value = e
        return value

if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value("login_mor"))
