from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized type of browser - %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
            wd.get(self.base_url)

    def stop(self):
        self.wd.quit()

    def contacts_in_group_page(self, id_group):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/?group=%s" % id_group
                and len(wd.find_element_by_name("remove")) > 0):
            wd.get("http://localhost/addressbook/?group=%s" % id_group)
