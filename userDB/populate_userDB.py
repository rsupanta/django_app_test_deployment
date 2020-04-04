import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','userDB.settings')

import django
# Import settings
django.setup()

import random
from userDB_app.models import user
from faker import Faker

fakegen = Faker()


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()
        fake_uname = fakegen.last_name()

        # Create new Webpage Entry
        fname = user.objects.get_or_create(first_name=fake_first, last_name=fake_last, username=fake_uname, email=fake_email)[0]



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
