from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_data(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("submit").click()
        self.app.navigation.open_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        self.app.navigation.accept_alert()
        self.app.navigation.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name = 'entry']/."):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            lastname = element.find_element_by_xpath(
                "//input[@name = 'selected[]'][@value = '%s']/../..//td[2]" % id).text
            firstname = element.find_element_by_xpath(
                "//input[@name = 'selected[]'][@value = '%s']/../..//td[3]" % id).text
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts
