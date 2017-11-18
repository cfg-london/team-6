import requests
import json
from prize import Prize, calc_prize_id
from itertools import islice

from laureate_class import Laureate

class Caller(object):

    def __init__(self):
        self.url = "http://api.nobelprize.org/v1/"
        self.get_all_laureates()
        self.get_all_prizes()
        self.initialize_laureate_pool()
        self.initialize_prize_pool()

    def get_all_laureates(self):
        self.laureate_list = requests.get(self.url + "laureate.json?").json()['laureates']
        return self.laureate_list

    def get_all_prizes(self):
        self.prize_list = requests.get(self.url + "prize.json?").json()['prizes']
        return self.prize_list

    def initialize_laureate_pool(self):
        self.laureate_pool = {}
        ten_items = take(300, self.get_all_laureates())
        for data in ten_items:
            self.laureate_pool[int(data['id'])] = Laureate(data)


    def initialize_prize_pool(self):
         self.prize_pool = {}
         for prize_data in self.get_all_prizes():
             prize_key = calc_prize_id(prize_data)
             self.prize_pool[prize_key] = Prize(prize_data)
        
    def show_all_prizes(self):
        for id, p in self.prize_pool.items():
            p.show()

    def show_all_laureates(self):
        for id, l in self.laureate_pool.items():
            l.show()

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

#api = Caller()
#api.initialize_prize_pool()
#print(json.dumps(api.get_all_laureates(), indent=4, sort_keys=True))
#api.show_all_laureates()


 
 
 
 

