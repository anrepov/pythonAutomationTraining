class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_data(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("submit").click()

    def modify_first(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        self.app.navigation.accept_alert()
        self.app.navigation.return_to_home_page()
