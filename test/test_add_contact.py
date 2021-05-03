# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("name", "middlename", "lastname"))
    app.navigation.return_to_home_page()
    app.session.logout()
