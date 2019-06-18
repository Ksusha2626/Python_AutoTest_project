from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact_form(Contact(name="test"))
    app.contact.delete_first_contact()
