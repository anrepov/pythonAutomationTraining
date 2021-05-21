# -*- coding: utf-8 -*-
import random
import string

import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    return prefix + "".join([random.choice(string.ascii_letters) for _ in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
