from model.contact import Contact
from model.group import Group
import random
import pytest


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(name="111"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="123", header="456", footer="789"))
    with pytest.allure.step('Сравниваем список контактов'):
        contact_list = db.get_contact_list()
    with pytest.allure.step('Выбираем контакт'):
        contact_id = random.choice(contact_list).id
    group_list = db.get_group_list()
    with pytest.allure.step('Выбираем группу'):
        group_id = random.choice(group_list).id
    with pytest.allure.step('Добавляем контакт в группу'):
        app.contact.add_contact_to_group(contact_id, group_id)
    assert db.get_all_contact_list(contact_id) in orm.get_contacts_in_group(Group(id=group_id))
