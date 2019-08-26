import requests
from utils.constants import *
from utils.jsondata import *


class Boards(object):
    def __init__(self):
        self.id = None
        self.response = None

    def create_a_board_in_organization(self):
        url = url_create_board
        self.response = requests.request("POST", url, params=OAUTH_DATA, data=create_board_data)
        self.id = self.response.json()['id']
        return self.response

    def delete_a_board_in_oraganization(self):
        url = url_delete_board.format(id=self.id)
        response = requests.request("DELETE", url, params=OAUTH_DATA)

    def update_field_of_board_in_organization(self):
        url = url_update_board_field(id=self.id)
        response = requests.request("PUT", url, params=OAUTH_DATA)

    def add_member_in_board(self, member, query):
        url = url_add_member_in_board.format(id=self.id, idMember=member)
        response = requests.request("PUT", url, params=OAUTH_DATA, data=query)

    def remove_member_from_board(self, member, query):
        url = url_remove_member_from_board.format(id=self.id, idMember=member)
        response = requests.request("DELETE", url, params=OAUTH_DATA, data=query)

    def get_members_of_board(self):
        url = url_get_members_from_board.format(id=self.id)
        response = requests.request("GET", url, params=OAUTH_DATA)




