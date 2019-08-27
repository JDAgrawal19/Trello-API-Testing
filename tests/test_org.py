from utils.jsondata import *
from utils.custom_logger import custom_logger
import logging
from pages.Organizations import Organizations
import requests
import time
import pytest


class TestOrg(object):

    log = custom_logger(logging.ERROR)

    @pytest.fixture()
    def setup(self):
        global org
        org = Organizations()
        org.create_organization(create_org_with_correct_name)
        yield
        org.delete_organization()

    @pytest.fixture()
    def setup_create_org(self):
        global org
        org = Organizations()
        org.create_organization(create_org_with_correct_name)

    def test_create_organization(self):
        org = Organizations()
        response = org.create_organization(create_org_with_correct_name)
        assert response.status_code == requests.codes.ok
        assert response.json()['name'] == create_org_with_correct_name['name'], \
            self.log.error("create organization failed")
        org.delete_organization()

    def test_create_organization_incorrect_name_uppercase_letters(self):
        org = Organizations()
        response = org.create_organization(create_org_incorrect_name_uppercase_letter)
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong in create_organization_incorrect_name_uppercase ")
        assert response.json()['name'] == create_org_incorrect_name_uppercase_letter['name'].lower()
        org.delete_organization()

    def test_create_organization_incorrect_name_special_chars(self):
        org = Organizations()
        response = org.create_organization(create_org_incorrect_name_special_char)
        assert response.status_code == requests.codes.ok, \
            self.log.error("something went wrong in create_organization_incorrect_name_special_chars")
        assert response.json()['name'] != create_org_incorrect_name_special_char['name']
        org.delete_organization()

    @pytest.mark.usefixtures("setup")
    def test_update_org_field_correct_display_name(self):
        response = org.update_fields_of_organization(update_org_correct_display_name)
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong in create_organization_incorrect_name_special_chars")

    @pytest.mark.usefixtures("setup")
    def test_update_org_field_display_name_ends_with_space(self):
        response_update = org.update_fields_of_organization(update_org_incorrect_display_name_ends_with_space)
        assert response_update.status_code == requests.codes.bad_request,\
            self.log.error("something went wrong in test_update_org_"
                           "field_display_name_ends_with_space")

    @pytest.mark.usefixtures("setup")
    def test_update_org_field_display_name_empty(self):
        response_update = org.update_fields_of_organization(update_org_incorrect_display_name_empty)
        assert response_update.status_code == requests.codes.bad_request,\
            self.log.error("something went wrong in test_update_org_field_display_name_empty")

    @pytest.mark.usefixtures("setup")
    def test_add_member_to_org(self):
        query_add_member = create_member_or_update_type
        member = member1
        response = org.add_member_to_organization_or_update_member_type(member, query_add_member)
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong in test_add_member_to_org")

    @pytest.mark.usefixtures("setup")
    def test_try_add_member_with_no_type(self):
        create_member_or_update_type["type"] = ""
        member = member1
        response = org.add_member_to_organization_or_update_member_type(member, create_member_or_update_type)
        assert response.status_code == requests.codes.bad_request, \
            self.log.error("something went wrong in test_add_member_with_no_type")

    @pytest.mark.usefixtures("setup")
    def test_update_member_type_in_org(self):
        create_member_or_update_type["type"] = "admin"
        response = org.add_member_to_organization_or_update_member_type(member1,
                                                                        create_member_or_update_type)
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong in test_update_member_type_in_org")

    @pytest.mark.usefixtures("setup")
    def test_remove_member_from_org(self):
        org.add_member_to_organization_or_update_member_type(member1,
                                                             create_member_or_update_type)
        response = org.remove_member_from_organization(member1)
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong in test_remove_member_from_org")

    @pytest.mark.usefixtures("setup_create_org")
    def test_delete_organization(self):
        response = org.delete_organization()
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong in test_delete_organization")

    @pytest.mark.usefixtures("setup_create_org")
    def test_try_test_delete_organization_twice(self):
        org.delete_organization()
        response = org.delete_organization()
        assert response.status_code == requests.codes.not_found,\
            self.log.error("something went wrong in test_try_test_delete_organization_twice")

    @pytest.mark.usefixtures("setup")
    def test_get_members_of_organization(self):
        org.add_member_to_organization_or_update_member_type(member1, create_member_or_update_type)
        response = org.get_members_of_organizations()
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong in test_get_members_of_organization")
