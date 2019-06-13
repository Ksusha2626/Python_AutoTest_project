
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open group's page
        wd.find_element_by_link_text("groups").click()

    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

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
        # select first group
        wd.find_element_by_name("selected[]").click()
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
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit_deletion
        wd.find_element_by_name("delete").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        # return to group's page
        wd.find_element_by_link_text("group page").click()
