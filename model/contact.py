from sys import maxsize


class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, mobile_tel=None, work_tel=None, email=None, page=None,
                 bday=None, bmonth=None, byear=None, id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.email = email
        self.page = page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

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
