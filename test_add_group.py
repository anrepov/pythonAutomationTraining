import unittest

from selenium import webdriver


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome("drivers/chromedriver.exe")
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()

        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys("na")
        wd.find_element_by_name("group_header").send_keys("he")
        wd.find_element_by_name("group_footer").send_keys("fo")

        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

    def tearDown(self):
        self.wd.quit()
