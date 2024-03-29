import requests
from utils.constants import *
from utils.jsondata import *


class Cards(object):
    def __init__(self):
        self.id = None
        self.response = None

    def create_a_new_card(self, query):
        url = url_create_new_card
        self.response = requests.request("POST", url, params=OAUTH_DATA, data=query)
        self.id = self.response.json()['id']
        return self.response

    def delete_a_card(self):
        url = url_delete_card.format(id=self.id)
        response = requests.request("DELETE", url, params=OAUTH_DATA)
        return response

    def add_member_to_a_card(self, query):
        url = url_add_member_to_card.format(id=self.id)
        response = requests.request("POST", url, params=OAUTH_DATA, data=query)
        return response

    def remove_member_from_card(self, member):
        url = url_remove_member_from_card.format(id=self.id, idMember=member)
        response = requests.request("DELETE", url, params=OAUTH_DATA)
        return response

    def get_the_board_card_is_on(self, query):
        url = url_get_the_board_card_is_on.format(id=self.id)
        response = requests.request("GET", url, params=OAUTH_DATA, data=query)
        return response

    def get_members_on_a_card(self, query):
        url = url_get_the_members_on_a_card.format(id=self.id)
        response = requests.request("GET", url, params=OAUTH_DATA, data=query)
        return response

    def add_comment_to_card(self, query):
        url = url_add_comment_to_card.format(id=self.id)
        response = requests.request("POST", url, params=OAUTH_DATA, data=query)
        return response

    def add_attachment_to_card(self,query):
        url = url_add_attachment_to_card.format(id=self.id)
        response = requests.request("POST", url, params = OAUTH_DATA, data=query)
        return response





