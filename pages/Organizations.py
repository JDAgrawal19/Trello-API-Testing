import requests
from utils.constants import *
from utils.jsondata import *


class Organizations(object):
    def __init__(self):
        self.id = None
        self.response = None

    def create_organization(self, query):
        self.response = requests.request("POST", url=url_create_organization, params=OAUTH_DATA, data=query)
        self.id = self.response.json()['id']
        return self.response

    def delete_organization(self):
        url = url_delete_organization.format(id=self.id)
        requests.request("DELETE", url=url, params=OAUTH_DATA)

    def update_fields_of_organization(self, query):
        url = url_update_organization.format(id=self.id)
        response = requests.request("PUT", url=url, params=OAUTH_DATA, data=query)
        return response

    def add_member_to_organization_or_update_member_type(self, member, query):
        url = url_add_memeber_in_organization.format(id=self.id, idMember=member)
        response = requests.request("PUT", url, params=OAUTH_DATA, data=query)
        return response








