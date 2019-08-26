import requests
from utils.constants import *
from utils.jsondata import *


class Cards(object):
    def __init__(self):
        self.id = None

    def create_a_new_card(self):
        url = url_create_new_card
        response = requests.request("POST", url, params=OAUTH_DATA, data="idlist")

    def add_member_to_a_card(self):
        url = url_add_member_to_card.format(id=self.id, idMember ="member")
        response = requests.request("POST", url, params=OAUTH_DATA)

    def delete_a_card(self):
        url = url_delete_card.format(id=self.id)
        response = requests.request("DELETE", url, params=OAUTH_DATA)

    def remove_member_from_card(self, member):
        url = url_remove_member_from_card.format(id=self.id, idMember=member)
        response = requests.request("DELETE", url, params=OAUTH_DATA)

    def get_the_board_card_is_on(self, query):
        url = url_get_the_board_card_is_on.format(id=self.id)
        response = requests.request("GET", url, params=OAUTH_DATA, data=query)


