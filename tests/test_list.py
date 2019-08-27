from utils.jsondata import *
from pages.Organizations import Organizations
from pages.Boards import Boards
from pages.Lists import Lists
import requests
import time
import pytest

class TestList(object):
    @pytest.fixture()
    def setup(self):
        global board
        board = Boards()
        query_create = create_board_without_org_data
        board.create_a_board_without_org(query_create)
        yield
        board.delete_a_board()

    @pytest.fixture()
    def create_list_setup(self):
        global board
        board = Boards()
        query_create = create_board_without_org_data
        board.create_a_board_without_org(query_create)
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
        query["idBoard"] = board.id
        list_obj = Lists()
        response = list_obj.create_a_new_list_on_a_board(query)
        assert response.status_code == requests.codes.ok

    @pytest.mark.usefixtures("create_list_setup")
    def test_update_name_of_list(self):
        response = list_obj.update_fields_of_list(update_list_name_data)
        assert response.status_code == requests.codes.ok

    @pytest.mark.usefixtures("create_list_setup")
    def test_move_list_to_new_board(self):
        board2 = Boards()
        query_create = create_board_without_org_data
        board2.create_a_board_without_org(query_create)
        query = move_list_to_new_board_data
        query["value"] = board2.id
        response = list_obj.move_list_to_a_new_board(query)
        assert response.status_code == requests.codes.ok







