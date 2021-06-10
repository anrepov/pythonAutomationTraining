# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    if db.get_contacts_list() == 0:
        app.contact.create(Contact("test"))

    old_contacts = db.get_contacts_list()
    old_contact = random.choice(old_contacts)

    new_contact = Contact(id=old_contact.id, firstname=old_contact.firstname + "_mod",
                          lastname=old_contact.lastname + "lastname_mod")
    app.contact.modify_by_id(new_contact, old_contact.id)
    new_contacts = db.get_contacts_list()

    assert len(old_contacts) == len(new_contacts)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                     key=Contact.id_or_max)
