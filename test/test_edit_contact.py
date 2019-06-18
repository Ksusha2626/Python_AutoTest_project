from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_contact_form(Contact(name="Jenia", middlename="Testovich", lastname="Testovskiy"))
