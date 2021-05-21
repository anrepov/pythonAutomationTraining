# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact("test")
    if app.contact.count() == 0:
        app.contact.create(contact)
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
