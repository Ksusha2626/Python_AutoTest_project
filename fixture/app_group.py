from selenium import webdriver
from fixture.session import SessionHelper
from fixture.helper import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.helper = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        # home page
        wd.get("http://localhost/addressbook/")

    def stop(self):
        self.wd.quit()
