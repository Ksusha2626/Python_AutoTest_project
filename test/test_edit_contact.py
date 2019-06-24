from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.contact_form(Contact(name="test"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(name="Jenia", middlename="Testovich", lastname="Testovskiy")
    contact.id = old_contact[0].id
    app.contact.edit_contact_form(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)