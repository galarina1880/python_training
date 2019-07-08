# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_login_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def add_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("first name")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys("middle name")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys("last name")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys("nick")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys("home phone")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys("mobile")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys("work phone")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys("fax")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys("email 1")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys("email 2")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys("email 3")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys("HP")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("6")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("1988")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("7")
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("December")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys("sec address")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys("sec home")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys("notes")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def go_to_hp(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd

        self.open_login_page(wd)
        self.add_contact(wd)
        self.go_to_hp(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
