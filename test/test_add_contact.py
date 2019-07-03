# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(name="Kseniya", middlename="ksu", lastname="Barkovskaya", mobile_tel="345", work_tel="678",
                      email="ksu2@mail.org", email2="123@mail.ru", address="Киевская", page="www.ksu.ru", bday="6",
                      bmonth="March", byear="1995")
    app.contact.contact_form(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
