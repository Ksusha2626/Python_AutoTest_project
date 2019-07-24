from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm):

    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(name="111"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="123", header="456", footer="789"))
    contact_list = db.get_contact_list()
    contact_id = random.choice(contact_list).id
    group_list = db.get_group_list()
    group_id = random.choice(group_list).id
    app.contact.add_contact_to_group(contact_id, group_id)
