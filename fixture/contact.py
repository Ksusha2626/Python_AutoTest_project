from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.fill_form_value("home", contact.home_tel)
        self.fill_form_value("address", contact.address)
        self.fill_form_value("email", contact.email)
        self.fill_form_value("email2", contact.email2)
        self.fill_form_value("email3", contact.email3)
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
        self.contact_cache = None

    def edit_contact_form(self):
        self.edit_contact_form_by_index(0)

    def edit_contact_form_by_index(self, contact, index):
        wd = self.app.wd
        # open edit page
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # change contact form
        self.fill_form(contact)
        # submit changes
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def delete_first_group(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select random contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit_deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('[name ="entry"]'):
                cells = element.find_elements_by_tag_name("td")
                surname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                mails = cells[4].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(name=firstname, lastname=surname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_mails=mails))
        return list(self.contact_cache)

    def random_row(self, index, wd):
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        return row

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        row = self.random_row(index, wd)
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        row = self.random_row(index, wd)
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_xpath("//tr[@name='entry']/td/input[@value='%s']/../.." % id)
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        home_tel = wd.find_element_by_name('home').get_attribute('value')
        mobile_tel = wd.find_element_by_name('mobile').get_attribute('value')
        work_tel = wd.find_element_by_name('work').get_attribute('value')
        return Contact(name=name, lastname=lastname, id=id, home_tel=home_tel, mobile_tel=mobile_tel, work_tel=work_tel,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home_tel = re.search("H: (.*)", text).group(1)
        mobile_tel = re.search("M: (.*)", text).group(1)
        work_tel = re.search("W: (.*)", text).group(1)
        return Contact(home_tel=home_tel, mobile_tel=mobile_tel,  work_tel=work_tel)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit_deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_form_by_id(self, id, contact):
        wd = self.app.wd
        # open edit page
        self.open_contact_to_edit_by_id(id)
        # wd.find_elements_by_xpath("//img[@alt='Edit']")[id].click()
        # change contact form
        self.fill_form(contact)
        # submit changes
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None