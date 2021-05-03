# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first(Contact("name_mod", "middlename_mod", "lastname_mod"))
    app.navigation.return_to_home_page()
    app.session.logout()
