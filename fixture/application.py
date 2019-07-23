from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_login_pg(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def go_to_hp(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()