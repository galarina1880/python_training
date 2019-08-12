# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname mod', middlename='middlename mod', lastname='lastname mod', nickname='nick mod', title='title mod', company='company mod', address='address mod', home='home phone mod', mobile='mobile mod', work='work phone mod', fax='fax mod', email='email 1 mod', email2='email 2 mod', email3='email 3 mod', homepage='homepage mod', bday='7', bmonth='September', byear='1988', aday='10', amonth='February', ayear='2010', address2='Address 2 mod', phone2='phone 2 mod', notes='notes mod')
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.session.logout()
