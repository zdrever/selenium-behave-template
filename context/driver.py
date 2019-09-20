from selenium import webdriver
from context.config import settings


class Driver(object):
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
            self.driver = webdriver.Chrome(
                executable_path=settings.chromedriver_path)
        elif settings.browser == "firefox":
            self.driver = webdriver.Firefox(
                executable_path=settings.geckodriver_path)
        else:
            raise SeleniumDriverNotFound(
                "{settings.browser} not currently supported")

    def get_driver(self):
        return self.driver

    def navigate(self, url):
        self.driver.get(url)


driver = Driver.get_instance()
