
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open group's page
        wd.find_element_by_link_text("groups").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # group creation
        wd.find_element_by_name("new").click()
        # fill_info
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open_edition_page
        wd.find_element_by_name("edit").click()
        # change_info
        self.fill_form(group)
        # submit_edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit_deletion
        wd.find_element_by_name("delete").click()
        self.return_to_home_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        # return to group's page
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
