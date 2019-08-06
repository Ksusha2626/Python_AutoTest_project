from model.contact import Contact
from model.group import Group
import random
import pytest


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(name="111"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="123", header="456", footer="789"))
    if len(db.get_groups_with_contacts()) == 0:
        contact_id = random.choice(db.get_contact_list()).id
        group_id = random.choice(db.get_group_list()).id
        app.contact.add_contact_to_group(contact_id, group_id)
    with pytest.allure.step('Выбираем группу'):
        group_id = random.choice(db.get_groups_with_contacts()).id
    with pytest.allure.step('Выбираем контакт'):
        contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    with pytest.allure.step('Удаляем контакт из группы'):
        app.contact.delete_contact_from_group(group_id)
    assert db.get_all_contact_list(contact_id) not in orm.get_contacts_in_group(Group(id=group_id))
