# -*- coding: utf-8 -*-
from model.contact import Contact
from model.contact import EditContact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact()
    app.contact.contact_form(
            Contact(name="Kseniya", middlename="ksu", lastname="Barkovskaya", nickname="ksu26", title="wow",
                    company="fabr", address="Moscow", home_tel="123",
                    mobile_tel="345", work_tel="678", fax="909", email="ksu2@mail.org", page="www.ksu.ru", bday="6",
                    bmonth="March", byear="1995"))
    app.contact.edit_contact_form(EditContact(name="Jenia", middlename="Testovich", lastname="Testovskiy"))
    app.contact.delete_first_contact()
    app.session.logout()
