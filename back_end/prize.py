import json
import requests
from enum import Enum

class Prize(object):

    def __init__(self, data):
        self.id =  calc_prize_id(data)
        self.year =  int(data['year'])
        self.category = data['category']
        self.gen_laureates(data['laureates'])

    def gen_laureates(self, laureates):
        self.laureate_list = []
        for l in laureates:
            self.laureate_list.append(int(l['id']))

    def show(self):
        laureates = ""
        for i in self.laureate_list:
            laureates += str(i) + " "
        print(self.category + " prize in " + str(self.year) + " awarded to laureates: " + laureates)


def calc_prize_id(data):
    return_id = int(data['year'])
    switcher = {
            'physics': 10000,
            'chemistry': 20000,
            'medicine' : 30000,
            'peace'    : 40000,
            'literature': 50000,
            'economics': 60000,
            }
    return return_id + switcher[data['category']]





