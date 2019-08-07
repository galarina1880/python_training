# -*- coding: utf-8 -*-
from model.contact import Contact
import time


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='firstname', middlename='middlename', lastname='lastname', nickname='nick', title='title', company='company', address='address', home='home phone', mobile='mobile', work='work phone', fax='fax', email='email 1', email2='email 2', email3='email 3', homepage='homepage', bday='6', bmonth='August', byear='1980', aday='8', amonth='January', ayear='2000', address2='Address 2', phone2='phone 2', notes='notes')
    app.contact.create(contact)
    app.wd.implicitly_wait(5)
    app.go_to_hp()
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    # assert len(old_contacts) + 1 == len(new_contacts)
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     app.contact.create(Contact(firstname='', middlename='', lastname='', nickname='', title='', company='', address='', home='', mobile='', work='', fax='', email='', email2='', email3='', homepage='', bday='', bmonth='-', byear='', aday='', amonth='-', ayear='', address2='', phone2='', notes=''))
