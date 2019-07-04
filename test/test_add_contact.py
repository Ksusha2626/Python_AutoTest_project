# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", middlename="", lastname="")] + [
    Contact(name=random_string("name", 10), middlename=random_string("middle", 10),
            lastname=random_string("111", 10), mobile_tel=random_string("123", 5),
            work_tel=random_string("567", 5), home_tel=random_string("098", 5),
            email=random_string("email", 10), email2=random_string("email2", 5),
            email3=random_string("email3", 5), address=random_string("address", 20),
            page=random_string("page", 10), bday="6", bmonth="March", byear=random_string("1", 4))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.contact_form(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
