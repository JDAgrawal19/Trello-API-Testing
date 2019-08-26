from utils.jsondata import *
from pages.Organizations import Organizations
import requests
import time

class TestTrello(object):
    # def test_create_organization(self):
    #     org = Organizations()
    #     query = create_org_with_correct_name
    #     response = org.create_organization(query)
    #     assert response.status_code == requests.codes.ok
    #     assert response.json()['name'] == query['name']
    #     org.delete_organization()
    #
    # def test_create_organization_incorrect_name_uppercase_letters(self):
    #     org = Organizations()
    #     query = create_org_incorrect_name_uppercase_letter
    #     response = org.create_organization(query)
    #     assert response.status_code == requests.codes.ok
    #     assert response.json()['name'] == query['name'].lower()
    #     org.delete_organization()
    #
    # def test_create_organization_incorrect_name_special_chars(self):
    #     org = Organizations()
    #     query = create_org_incorrect_name_special_char
    #     response = org.create_organization(query)
    #     assert response.status_code == requests.codes.ok
    #     assert response.json()['name'] != query['name']
    #     org.delete_organization()
    #
    # def test_update_org_field_correct_display_name(self):
    #     org = Organizations()
    #     query_create = create_org_with_correct_name
    #     org.create_organization(query_create)
    #     query_update = update_org_correct_display_name
    #     response = org.update_fields_of_organization(query_update)
    #     assert response.status_code == requests.codes.ok
    #     org.delete_organization()
    #
    # def test_update_org_field_display_name_ends_with_space(self):
    #     org = Organizations()
    #     query_create = create_org_with_correct_name
    #     response_create = org.create_organization(query_create)
    #     query_update = update_org_incorrect_display_name_ends_with_space
    #     response_update = org.update_fields_of_organization(query_update)
    #     assert response_update.status_code == requests.codes.bad_request
    #     org.delete_organization()
    #
    # def test_update_org_field_display_name_empty(self):
    #     org = Organizations()
    #     query_create = create_org_with_correct_name
    #     response_create = org.create_organization(query_create)
    #     query_update = update_org_incorrect_display_name_empty
    #     response_update = org.update_fields_of_organization(query_update)
    #     assert response_update.status_code == requests.codes.bad_request
    #     org.delete_organization()

    def test_add_member_to_org(self):
        org = Organizations()
        query_create = create_org_with_correct_name
        response_create = org.create_organization(query_create)
        query_add_member = create_member_or_update_type
        member = member1
        response = org.add_member_to_organization_or_update_member_type(member, query_add_member)
        assert response.status_code == requests.codes.ok
        org.delete_organization()





