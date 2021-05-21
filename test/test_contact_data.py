from random import randrange

from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page


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
