# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("test"))

    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact("name_mod", "middlename_mod", "lastname_mod")
    contact.id = old_contacts[index].id
    app.contact.modify_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
