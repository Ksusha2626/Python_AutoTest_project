from model.contact import EditContact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact_form(EditContact(name="Jenia", middlename="Testovich", lastname="Testovskiy"))
    app.session.logout()