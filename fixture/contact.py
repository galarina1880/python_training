from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_value("bday", contact.bday)
        self.select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_value("aday", contact.aday)
        self.select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def submit_form_create(self):
        wd = self.app.wd
        wd.find_elements_by_xpath("(//input[@value='Enter'])")[1].click()

    def submit_form_modify(self):
        wd = self.app.wd
        wd.find_elements_by_xpath("(//input[@value='Update'])")[1].click()

    contact_cache = None

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.submit_form_create()
        self.app.go_to_hp()
        self.contact_cache = None

    def delete(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()
        self.app.go_to_hp()
        self.contact_cache = None

    def modify(self, contact):
        wd = self.app.wd
        # open contact for modification
        self.app.go_to_hp()
        # text = 'edit'
        wd.find_elements_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]/a')[0].click()
        # modify contact
        self.fill_contact_form(contact)
        self.submit_form_modify()
        self.app.go_to_hp()
        self.contact_cache = None

    def modify_by_index(self, index, contact):
        wd = self.app.wd
        # open contact for modification
        self.app.go_to_hp()
        wd.find_elements_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]/a')[index].click()
        # modify contact
        self.fill_contact_form(contact)
        self.submit_form_modify()
        self.app.go_to_hp()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.go_to_hp()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.go_to_hp()
        wd.find_element_by_id("search_count")
        self.contact_cache = []
        for element in wd.find_elements_by_name("entry"):
            value = element.find_element_by_name("selected[]").get_attribute("value")
            id = element.find_element_by_name("selected[]").get_attribute("id")
            self.contact_cache.append(Contact(value=value, id=id))
        return list(self.contact_cache)
