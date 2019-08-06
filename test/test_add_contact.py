# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Получаем список контактов'):
        old_contact = db.get_contact_list()
    with pytest.allure.step('Добавляем контакт'):
        app.contact.contact_form(contact)
    new_contact = db.get_contact_list()
    with pytest.allure.step('Сравниваем списки'):
        assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, name=contact.name.rstrip())

        assert sorted(list(map(clean, new_contact)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                      key=Contact.id_or_max)
