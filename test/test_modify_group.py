# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="name mod", header="header mod", footer="footer mod"))
    app.session.logout()
