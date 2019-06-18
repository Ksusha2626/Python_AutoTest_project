from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.contact_form(Contact(name="test"))
    app.contact.edit_contact_form(Contact(name="Jenia", middlename="Testovich", lastname="Testovskiy"))
