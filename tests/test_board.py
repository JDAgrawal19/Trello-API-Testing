from utils.jsondata import *
from pages.Organizations import Organizations
from pages.Boards import Boards
import requests
import time
import pytest


class TestBoard(object):
    @pytest.fixture()
    def setup(self):
        global org
        org = Organizations()
        query_create = create_org_with_correct_name
        org.create_organization(query_create)
        yield
        org.delete_organization()

    @pytest.mark.usefixtures("setup")
    def test_create_board(self):
        board = Boards()
        create_board_data["idOrganization"] = org.id
        response = board.create_a_board_in_organization(create_board_data)
        assert response.status_code == requests.codes.ok
        board.delete_a_board()

    @pytest.mark.usefixtures("setup")
    def test_delete_board(self):
        board = Boards()
        create_board_data["idOrganization"] = org.id
        board.create_a_board_in_organization(create_board_data)
        response = board.delete_a_board()
        assert response.status_code == requests.codes.ok
