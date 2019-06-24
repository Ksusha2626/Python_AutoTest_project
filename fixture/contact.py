from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.fill_form_value("firstname", contact.name)
        self.fill_form_value("middlename", contact.middlename)
        self.fill_form_value("lastname", contact.lastname)
        self.fill_form_value("mobile", contact.mobile_tel)
        self.fill_form_value("work", contact.work_tel)
        self.fill_form_value("email", contact.email)
        self.fill_form_value("homepage", contact.page)

        self.fill_form_date("bday", contact.bday)
        self.fill_form_date("bmonth", contact.bmonth)
        self.fill_form_value("byear", contact.byear)

    def fill_form_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form_date(self, field_name, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(date)

    def contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def edit_contact_form(self, contact):
        wd = self.app.wd
        # open edit page
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # change contact form
        self.fill_form(contact)
        # submit changes
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit_deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contact = []
        for element in wd.find_elements_by_css_selector('[name ="entry"]'):
            cells = element.find_elements_by_tag_name("td")
            surname = cells[1].text
            firstname = cells[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contact.append(Contact(name=firstname, lastname=surname, id=id))
        return contact
