from utils.jsondata import *
from pages.Organizations import Organizations
from pages.Boards import Boards
from pages.Lists import Lists
from pages.Cards import Cards
import requests
import time
import pytest


class TestCards(object):
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

    @pytest.fixture()
    def create_card(self,create_list_setup):
        global card
        card = Cards()
        query = create_card_data
        query["idList"] = list_obj.id
        card.create_a_new_card(query)


    # @pytest.mark.usefixtures("create_list_setup")
    # def test_create_card(self):
    #     card = Cards()
    #     query = create_card_data
    #     query["idList"] = list_obj.id
    #     response = card.create_a_new_card(query)
    #     assert response.status_code == requests.codes.ok
    #
    # @pytest.mark.usefixtures("create_list_setup")
    # def test_delete_card(self):
    #     card = Cards()
    #     query = create_card_data
    #     query["idList"] = list_obj.id
    #     card.create_a_new_card(query)
    #     response = card.delete_a_card()
    #     assert response.status_code == requests.codes.ok
    #
    # @pytest.mark.usefixtures("create_card")
    # def test_add_member_to_card(self):
    #     board.add_member_in_board(member1, data_add_member_in_board)
    #     query = data_add_member_in_card
    #     query["value"] = member1_id
    #     response = card.add_member_to_a_card(query)
    #     assert response.status_code == requests.codes.ok

    @pytest.mark.usefixtures("create_card")
    def test_remove_member_from_card(self):
        board.add_member_in_board(member1, data_add_member_in_board)
        query = data_add_member_in_card
        query["value"] = member1_id
        card.add_member_to_a_card(query)
        response = card.remove_member_from_card(member1_id)
        assert response.status_code == requests.codes.ok


