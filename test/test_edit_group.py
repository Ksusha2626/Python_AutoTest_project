from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="111", header="444", footer="777"))
    app.session.logout()
