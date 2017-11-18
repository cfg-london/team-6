import requests
import json
from prize import Prize, calc_prize_id

from laureate_class import Laureate

class Caller(object):

    def __init__(self):
        self.url = "http://api.nobelprize.org/v1/"

    def get_all_laureates(self):
        self.laureate_list = requests.get(self.url + "laureate.json?").json()['laureates']
        return self.laureate_list

    def get_all_prizes(self):
        self.prize_list = requests.get(self.url + "prize.json?").json()['prizes']
        return self.prize_list

    def initialize_laureate_pool(self):
        self.laureate_pool = {}
        for data in self.get_all_laureates():
            self.laureate_pool[int(data['id'])] = Laureate(data)


    def initialize_prize_pool(self):
         self.prize_pool = {}
         for prize_data in self.get_all_prizes():
             prize_key = calc_prize_id(prize_data)
             self.prize_pool[prize_key] = Prize(prize_data)
        
    def show_all_prizes(self):
        for id, p in self.prize_pool.items():
            p.show()


api = Caller()
api.initialize_prize_pool()
print(json.dumps(api.get_all_laureates(), indent=4, sort_keys=True))


 
 
 
 

