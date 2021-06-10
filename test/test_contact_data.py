from random import randrange

from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page, as_ui
from model.contact import Contact


def test_home_and_view_pages_data_equality(app):
    contacts = app.contact.get_contacts_list()
    index = randrange(len(contacts))

    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.emails == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == \
           merge_phones_like_on_home_page(contact_from_edit_page)


def test_homepage_and_database_contacts_data_equality(app, db):
    ui_contacts = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contacts_list(), key=Contact.id_or_max)
    assert len(ui_contacts) == len(db_contacts)

    for i in range(len(ui_contacts)):
        db_contacts[i] = as_ui(db_contacts[i])

        assert ui_contacts[i].id == db_contacts[i].id
        assert ui_contacts[i].firstname == db_contacts[i].firstname
        assert ui_contacts[i].lastname == db_contacts[i].lastname
        assert ui_contacts[i].address == db_contacts[i].address
        assert ui_contacts[i].all_phones_from_home_page == db_contacts[i].all_phones_from_home_page
        assert ui_contacts[i].emails == db_contacts[i].emails
