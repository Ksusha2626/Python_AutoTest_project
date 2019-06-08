# -*- coding: utf-8 -*-
import pytest
from fixture.app_contact import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.helper.add_new_contact()
    app.helper.contact_form(
            Contact(name="Kseniya", middlename="ksu", lastname="Barkovskaya", nickname="ksu26", title="wow",
                    company="fabr", address="Moscow", home_tel="123",
                    mobile_tel="345", work_tel="678", fax="909", email="ksu2@mail.org", page="www.ksu.ru", bday="6",
                    bmonth="March", byear="1995"))
    app.session.logout()
