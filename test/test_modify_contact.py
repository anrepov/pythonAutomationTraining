# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("test"))
    app.contact.modify_first(Contact("name_mod", "middlename_mod", "lastname_mod"))
