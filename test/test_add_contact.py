# -*- coding: utf-8 -*-
# import pytest
from model.contact import Contact
# from fixture.application import Application
#
#
# @pytest.fixture
# def app(request):
#     fixture = Application()
#     request.addfinalizer(fixture.destroy)
#     return fixture


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.add_contact(Contact(firstname='firstname', middlename='middlename', lastname='lastname', nickname='nick', title='title', company='company', address='address', home='home phone', mobile='mobile', work='work phone', fax='fax', email='email 1', email2='email 2', email3='email 3', homepage='homepage', bday='6', bmonth='August', byear='1980', aday='8', amonth='January', ayear='2000', address2='Address 2', phone2='phone 2', notes='notes'))
    app.go_to_hp()
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.add_contact(Contact(firstname='', middlename='', lastname='', nickname='', title='', company='', address='', home='', mobile='', work='', fax='', email='', email2='', email3='', homepage='', bday='', bmonth='-', byear='', aday='', amonth='-', ayear='', address2='', phone2='', notes=''))
    app.go_to_hp()
    app.session.logout()
