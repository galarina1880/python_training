# -*- coding: utf-8 -*-
from model.group import Group


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="name mod", header="header mod", footer="footer mod"))
    app.session.logout()
