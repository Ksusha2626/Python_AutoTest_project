from fixture.ORM import ORMfixture
from fixture.group import Group

db = ORMfixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = db.get_groups_with_contacts(Group(id='192'))
    # cursor.execute("select * from group_list")
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
