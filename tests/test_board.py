from utils.jsondata import *
from utils.custom_logger import custom_logger
import logging
from pages.Organizations import Organizations
from pages.Boards import Boards
import requests
import time
import pytest


class TestBoard(object):
    log = custom_logger(logging.ERROR)

    @pytest.fixture()
    def setup(self):
        global org
        org = Organizations()
        query_create = create_org_with_correct_name
        org.create_organization(query_create)
        yield
        org.delete_organization()

    @pytest.fixture()
    def setup_with_board(self):
        global org
        org = Organizations()
        query_create = create_org_with_correct_name
        org.create_organization(query_create)
        global board
        board = Boards()
        create_board_data["idOrganization"] = org.id
        board.create_a_board_in_organization(create_board_data)
        yield
        board.delete_a_board()
        org.delete_organization()

    @pytest.mark.usefixtures("setup")
    def test_create_board(self):
        board = Boards()
        create_board_data["idOrganization"] = org.id
        response = board.create_a_board_in_organization(create_board_data)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong with test_create_board")
        board.delete_a_board()

    @pytest.mark.usefixtures("setup")
    def test_delete_board(self):
        board = Boards()
        create_board_data["idOrganization"] = org.id
        board.create_a_board_in_organization(create_board_data)
        response = board.delete_a_board()
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong with test_delete_board")

    @pytest.mark.usefixtures("setup_with_board")
    def test_update_name_of_board(self):
        update_board_name["idOrganization"] = org.id
        response = board.update_fields_of_board(update_board_name)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong with test_update_name_of_board")

    @pytest.mark.usefixtures("setup_with_board")
    def test_update_board_name_where_name_is_empty(self):
        update_board_name_empty["idOrganization"] = org.id
        response = board.update_fields_of_board(update_board_name_empty)
        try:
            assert response.status_code == requests.codes.bad_request
        except AssertionError:
            self.log.error("something went wrong with test_update_board_name_where_name_is_empty")

    @pytest.mark.usefixtures("setup_with_board")
    def test_update_board_name_with_invalid_org_id(self):
        response = board.update_fields_of_board(update_board_name)
        try:
            assert response.status_code == requests.codes.unauthorized
        except AssertionError:
            self.log.error("something went wrong with test_update_board_name_with_invalid_org_id")

    @pytest.mark.usefixtures("setup_with_board")
    def test_add_member_to_board(self):
        response = board.add_member_in_board(member1, data_add_member_in_board)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong with test_add_member_to_board")

    @pytest.mark.usefixtures("setup_with_board")
    def test_remove_member_present_in_board(self):
        board.add_member_in_board(member1, data_add_member_in_board)
        response = board.remove_member_from_board(member1)
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong with test_remove_member_present_in_board")

    @pytest.mark.usefixtures("setup_with_board")
    def test_try_remove_member_not_present_in_board(self):
        board.add_member_in_board(member1, data_add_member_in_board)
        response = board.remove_member_from_board(member2)
        try:
            assert response.status_code == requests.codes.unauthorized
        except AssertionError:
            self.log.error("something went wrong with test_try_remove_member_not_present_in_board")

    @pytest.mark.usefixtures("setup_with_board")
    def test_get_members_of_board(self):
        board.add_member_in_board(member1, data_add_member_in_board)
        response = board.get_members_of_board()
        try:
            assert response.status_code == requests.codes.ok
        except AssertionError:
            self.log.error("something went wrong with test_get_members_of_board")


