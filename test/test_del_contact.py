from model.contact import Contact
import random
import pytest


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.contact_form(Contact(name="test"))
    with pytest.allure.step('Сравниваем список контактов'):
        old_contact = db.get_contact_list()
    with pytest.allure.step('Выбираем контакт'):
        contact = random.choice(old_contact)
    with pytest.allure.step('Удаляем контакт'):
        app.contact.delete_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    with pytest.allure.step('Проверяем отсутствие удаленного контакта'):
        assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, name=contact.name.rstrip())

        assert sorted(list(map(clean, new_contact)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                      key=Contact.id_or_max)
