import django
from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse
import os




def test():

    setup_test_environment()
    client=Client()
    response=client.get("account/loginorlogout")
    response.status_code
    if response.status_code==200:
        return 0

test()