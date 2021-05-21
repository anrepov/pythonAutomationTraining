import re

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
        self.contacts_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first(self, contact):
        self.modify_by_index(contact, 0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def open_edit_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_xpath("//*[@title='Edit']")[index].click()

    def open_view_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_xpath("//*[@title='Details']")[index].click()

    def modify_by_index(self, contact, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.open_edit_contact_by_index(index)
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_home_page()
        self.contacts_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        self.app.navigation.accept_alert()
        self.app.navigation.open_home_page()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page()
            self.contacts_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                emails = cells[4].text
                all_phones = cells[5].text

                self.contacts_cache.append(
                    Contact(id=id, lastname=lastname, firstname=firstname, address=address, emails=emails,
                            all_phones_from_home_page=all_phones))

        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_contact_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")

        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")

        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       email1=email1, email2=email2, email3=email3,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_contact_by_index(index)
        text = wd.find_element_by_id("content").text

        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)

        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email1, contact.email2, contact.email3])))


def clear(s):
    return re.sub("[() -]", "", s)
