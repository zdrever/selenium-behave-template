from selenium import webdriver
from context.config import settings


class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        if settings.browser == "chrome":
            self.driver = webdriver.Chrome()
        elif settings.browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise SeleniumDriverNotFound(
                "{settings.browser} not currently supported")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


driver = Driver.get_instance()
