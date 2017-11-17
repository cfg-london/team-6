import requests

class Caller(object):

    def __init__(self):
        self.url = "http://api.nobelprize.org/v1/"

    def get_laureates(self):
        laureate_list = requests.get()
