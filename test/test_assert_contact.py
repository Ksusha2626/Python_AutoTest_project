from model.contact import Contact
from random import randrange
import re


def test_assert_contact_info(app):
    if app.contact.count() == 0:
        app.contact.contact_form(
            Contact(name="Kseniya", middlename="ksu", lastname="Barkovskaya", mobile_tel="345", work_tel="678",
                    email="ksu2@mail.org", email2="123@mail.ru", address="Киевская", page="www.ksu.ru", bday="6",
                    bmonth="March", byear="1995"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_info_from_home_page = app.contact.get_contact_list()[index]
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_info_from_home_page.name == contact_info_from_edit_page.name
    assert contact_info_from_home_page.lastname == contact_info_from_edit_page.lastname
    assert contact_info_from_home_page.address == contact_info_from_edit_page.address
    assert contact_info_from_home_page.all_mails == merge_emails(contact_info_from_edit_page)
    assert contact_info_from_home_page.all_phones_from_home_page == merge_phones_on_home_page(
        contact_info_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.mobile_tel, contact.work_tel]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2]))))
