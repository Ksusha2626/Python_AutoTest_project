# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="123", header="456", footer="789"))
    app.group.edit_group(Group(name="111", header="444", footer="777"))
    app.group.delete_first_group()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.delete_first_group()
    app.session.logout()
