from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.contact_form(Contact(name="test"))
    old_contact = db.get_contact_list()
    index = random.choice(range(len(old_contact)))
    id = old_contact[index].id
    contact = Contact(name="Jenia", middlename="Testovich", lastname="Testovskiy", id=id)
#    contact.id = old_contact[contact].id
    app.contact.edit_contact_form_by_id(id, contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, name=contact.name.rstrip())
        assert sorted(list(map(clean, new_contact)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                  key=Contact.id_or_max)
