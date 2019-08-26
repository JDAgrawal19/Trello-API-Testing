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






