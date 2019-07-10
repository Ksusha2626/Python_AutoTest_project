from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 3
f = 'data/contacts.json'

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", middlename="", lastname="")] + [
    Contact(name=random_string("name", 10), middlename=random_string("middle", 10),
            lastname=random_string("111", 10), mobile_tel=random_string("123", 5),
            work_tel=random_string("567", 5), home_tel=random_string("098", 5),
            email=random_string("email", 10), email2=random_string("email2", 5),
            email3=random_string("email3", 5), address=random_string("address", 20),
            page=random_string("page", 10), bday="6", bmonth="March", byear=random_string("1", 4))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
