# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.contact_form(
        Contact(name="Kseniya", middlename="ksu", lastname="Barkovskaya", mobile_tel="345", work_tel="678",
                email="ksu2@mail.org", page="www.ksu.ru", bday="6", bmonth="March", byear="1995"))
    app.contact.edit_contact_form(
       Contact(name="Jenia", middlename="Testovich", lastname="Testovskiy", bday="8", bmonth="March", byear="1997"))
#    app.contact.delete_first_contact()
