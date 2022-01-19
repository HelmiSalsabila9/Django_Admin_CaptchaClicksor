import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','captcha_clicksor_1194018.settings')

import django

django.setup()

#faker script
from appcaptcha_1194018.models import Captcha_Clicksor

from faker import Faker

fakegen = Faker()


def populate(N = 3):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_email = fakegen.email()
        fake_address = fakegen.address()

        captcha_clicksor = Captcha_Clicksor.objects.get_or_create(name = fake_first_name,
                                          email = fake_email, address = fake_address)[0]


if __name__== '__main__':
    print("Populating the database........Please Wait!")
    populate(3)
    print("Populating Complete")