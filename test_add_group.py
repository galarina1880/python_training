# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group
from application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="test", header="headr", footer="footr"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()


if __name__ == "__main__":
    unittest.main()
