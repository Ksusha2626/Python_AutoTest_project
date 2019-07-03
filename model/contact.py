from sys import maxsize


class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, mobile_tel=None, work_tel=None, email=None,
                 email2=None, page=None, address=None, bday=None, bmonth=None, byear=None, id=None,
                 all_phones_from_home_page=None, all_mails=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.email = email
        self.email2 = email2
        self.address = address
        self.page = page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_mails = all_mails
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
