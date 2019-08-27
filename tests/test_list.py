from utils.jsondata import *
from pages.Organizations import Organizations
from pages.Cards import Cards
from utils.custom_logger import custom_logger
import logging
from pages.Boards import Boards
from pages.Lists import Lists
import requests
import time
import pytest


class TestList(object):

    log = custom_logger(logging.ERROR)

    @pytest.fixture()
    def setup(self):
        global board2
        board2 = Boards()
        board2.create_a_board(create_board_without_org_data)
        yield
        board2.delete_a_board()

    @pytest.fixture()
    def create_list_setup(self):
        global board
        board = Boards()
        board.create_a_board(create_board_without_org_data)
        global list_obj
        list_obj = Lists()
        query = create_list_data
        query["idBoard"] = board.id
        list_obj.create_a_new_list_on_a_board(query)
        yield
        board.delete_a_board()

    @pytest.mark.usefixtures("setup")
    def test_create_list_on_board_without_org(self):
        query = create_list_data
        query["idBoard"] = board2.id
        list_obj = Lists()
        response = list_obj.create_a_new_list_on_a_board(query)
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong test_create_list_on_board_without_org")

    @pytest.mark.usefixtures("setup")
    def test_try_create_list_with_empty_name(self):
        query = create_list_data_with_empty_name
        query["idBoard"] = board2.id
        list_obj = Lists()
        response = list_obj.create_a_new_list_on_a_board(query)
        assert response.status_code == requests.codes.ok, \
            self.log.error("something went wrong test_create_list_on_board_without_org")

    @pytest.mark.usefixtures("create_list_setup")
    def test_update_name_of_list(self):
        response = list_obj.update_fields_of_list(update_list_name_data)
        assert response.status_code == requests.codes.ok, \
            self.log.error("something went wrong test_update_name_of_list")

    @pytest.mark.usefixtures("create_list_setup", "setup")
    def test_move_list_to_new_board(self):
        query = move_list_to_new_board_data
        query["value"] = board2.id
        response = list_obj.move_list_to_a_new_board(query)
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong test_move_list_to_new_board")

    @pytest.mark.usefixtures("create_list_setup")
    def test_get_board_details_list_is_present_on(self):
        response = list_obj.get_the_board_a_list_is_on()
        assert response.status_code == requests.codes.ok,\
            self.log.error("something went wrong test_get_board_details_list_is_present_on")

    @pytest.mark.usefixtures("create_list_setup")
    def test_list_is_archived_or_not(self):
        response = list_obj.archive_or_unarchive_a_list(data_archive_or_unarchive_a_list)
        assert response.status_code == requests.codes.ok, \
            self.log.error("something went wrong test_list_is_archived_or_not")

    @pytest.mark.usefixtures("create_list_setup")
    def test_list_is_subscribed_or_not(self):
        response = list_obj.subscribe_or_unsubscribe_a_list(data_susbscribe_or_unsubscribe_a_list)
        assert response.status_code == requests.codes.ok, \
            self.log.error("something went wrong test_list_is_archived_or_not")




