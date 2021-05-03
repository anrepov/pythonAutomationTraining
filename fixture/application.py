from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome("../drivers/chromedriver.exe")
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)

    def destroy(self):
        self.wd.quit()
