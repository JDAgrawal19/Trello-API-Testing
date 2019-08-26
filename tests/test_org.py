from utils.jsondata import *
from pages.Organizations import Organizations
import requests


class TestTrello(object):
    def test_create_organization(self):
        org = Organizations()
        query = create_org_with_correct_name
        response = org.create_organization(query)
        assert response.status_code == requests.codes.ok
        assert response.json()['name'] == query['name']
        org.delete_organization()


    def test_create_organization_incorrect_name_uppercase_letters(self):
        org = Organizations()
        query = create_org_incorrect_name_uppercase_letter
        response = org.create_organization(query)
        assert response.status_code == requests.codes.ok
        assert response.json()['name'] == query['name'].lower()
        org.delete_organization()

    def test_create_organization_incorrect_name_special_chars(self):
        org = Organizations()
        query = create_org_incorrect_name_special_char
        response = org.create_organization(query)
        assert response.status_code == requests.codes.ok
        assert response.json()['name'] != query['name']
        org.delete_organization()



