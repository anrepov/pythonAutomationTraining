class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def accept_alert(self):
        wd = self.app.wd
        wd.switch_to_alert().accept()
