import requests
from utils.constants import *
from utils.jsondata import *


class Lists(object):
    def __init__(self):
        self.id = None
        self.response = None

    def create_a_new_list_on_a_board(self, query):
        url = url_create_list_on_board
        self.response = requests.request("POST", url, params=OAUTH_DATA, data=query)
        self.id = self.response.json()['id']
        return self.response

    def update_fields_of_list(self, query):
        url = url_update_list_field.format(id=self.id)
        response = requests.request("PUT", url, params=OAUTH_DATA, data=query)
        return response

    def rename_a_list(self):
        url = url_rename_a_list.format(id=self.id)
        response = requests.request("PUT", url, params = OAUTH_DATA)

    def move_list_to_a_new_board(self, board_id):
        url = url_move_list_to_new_board.format(id=self.id, idBoard=board_id)
        response = requests.request("PUT", url, params=OAUTH_DATA)

    def get_the_board_a_list_is_on(self):
        url = url_get_cards_in_list.format(id=self.id)
        response = requests.request("GET", url, params=OAUTH_DATA)

    def set_a_soft_limit_of_cards_in_list(self,query):
        url = url_set_soft_limit_number_of_cards.format(id=self.id)
        response = requests.request("PUT", url, params= OAUTH_DATA, data=query)



