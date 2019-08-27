from utils.jsondata import *
from utils.custom_logger import custom_logger
import logging
from pages.Organizations import Organizations
import requests
import time
import pytest


class TestOrg(object):

    log = custom_logger(logging.DEBUG)

    @pytest.fixture()
    def setup(self):
        global org
        org = Organizations()
        query_create = create_org_with_correct_name
        org.create_organization(query_create)
        yield
        org.delete_organization()

    @pytest.fixture()
    def setup_create_org(self):
        global org
        org = Organizations()
        query_create = create_org_with_correct_name
        org.create_organization(query_create)

    def test_create_organization(self):
        org = Organizations()
        query = create_org_with_correct_name
        response = org.create_organization(query)
        try:
            assert response.status_code == requests.codes.ok
            assert response.json()['name'] == query['name']
        except AssertionError:
            self.log.error("create organization failed")
        org.delete_organization()

    def test_create_organization_incorrect_name_uppercase_letters(self):
        org = Organizations()
        query = create_org_incorrect_name_uppercase_letter
        response = org.create_organization(query)
        try:
            assert response.status_code == requests.codes.ok
            assert response.json()['name'] == query['name'].lower()
        except AssertionError:
            self.log.error("something went wrong in create_organization_incorrect_name_uppercase ")
        org.delete_organization()

    def test_create_organization_incorrect_name_special_chars(self):
        org = Organizations()
        query = create_org_incorrect_name_special_char
        response = org.create_organization(query)
        try:
            assert response.status_code == requests.codes.ok
            assert response.json()['name'] != query['name']
        except AssertionError:
            self.log.error("something went wrong in create_organization_incorrect_name_special_chars")
        org.delete_organization()

    @pytest.mark.usefixtures("setup")
    def test_update_org_field_correct_display_name(self):
        query_update = update_org_correct_display_name
        response = org.update_fields_of_organization(query_update)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong in create_organization_incorrect_name_special_chars")

    @pytest.mark.usefixtures("setup")
    def test_update_org_field_display_name_ends_with_space(self):
        query_update = update_org_incorrect_display_name_ends_with_space
        response_update = org.update_fields_of_organization(query_update)
        try:
            assert response_update.status_code == requests.codes.bad_request
        except AssertionError:
            self.log.error("something went wrong in test_update_org_"
                           "field_display_name_ends_with_space")

    @pytest.mark.usefixtures("setup")
    def test_update_org_field_display_name_empty(self):
        query_update = update_org_incorrect_display_name_empty
        response_update = org.update_fields_of_organization(query_update)
        try:
            assert response_update.status_code == requests.codes.bad_request
        except AssertionError:
            self.log.error("something went wrong in test_update_org_field_display_name_empty")

    @pytest.mark.usefixtures("setup")
    def test_add_member_to_org(self):
        query_add_member = create_member_or_update_type
        member = member1
        response = org.add_member_to_organization_or_update_member_type(member, query_add_member)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong in test_add_member_to_org")

    @pytest.mark.usefixtures("setup")
    def test_update_member_type_in_org(self):
        query_add_member = create_member_or_update_type
        query_add_member["type"] = "admin"
        member = member1
        response = org.add_member_to_organization_or_update_member_type(member, query_add_member)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong in test_update_member_type_in_org")

    @pytest.mark.usefixtures("setup")
    def test_remove_member_from_org(self):
        query_add_member = create_member_or_update_type
        member = member1
        org.add_member_to_organization_or_update_member_type(member, query_add_member)
        response = org.remove_member_from_organization(member1)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong in test_remove_member_from_org")

    @pytest.mark.usefixtures("setup_create_org")
    def test_delete_organization(self):
        response = org.delete_organization()
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong in test_delete_organization")

    @pytest.mark.usefixtures("setup_create_org")
    def test_try_test_delete_organization_twice(self):
        org.delete_organization()
        response = org.delete_organization()
        try:
            assert response.status_code == requests.codes.not_found
        except AssertionError:
            self.log.error("something went wrong in test_try_test_delete_organization_twice")

    @pytest.mark.usefixtures("setup")
    def test_get_members_of_organization(self):
        query_add_member = create_member_or_update_type
        member = member1
        org.add_member_to_organization_or_update_member_type(member, query_add_member)
        response = org.get_members_of_organizations()
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong in test_get_members_of_organization")






