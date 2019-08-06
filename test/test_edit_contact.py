from model.contact import Contact
import random
import pytest


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.contact_form(Contact(name="test"))
    with pytest.allure.step('Получение список контактов'):
        old_contact = db.get_contact_list()
    with pytest.allure.step('Выбираем рандомный контакт'):
        index = random.choice(range(len(old_contact)))
    id = old_contact[index].id
    contact = Contact(name="Jenia", middlename="Testovich", lastname="Testovskiy", id=id)
    #    contact.id = old_contact[contact].id
    with pytest.allure.step('Изменяем инфорамацию контакта'):
        app.contact.edit_contact_form_by_id(id, contact)
    with pytest.allure.step('Получение новый список контактов'):
        new_contact = db.get_contact_list()
    with pytest.allure.step('Проверяем соответствие списков'):
        assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, name=contact.name.rstrip())

        assert sorted(list(map(clean, new_contact)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                      key=Contact.id_or_max)
