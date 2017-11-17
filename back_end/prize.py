import json
import requests
#import Category as Category
from enum import Enum

class Category(Enum):
    PHYSICS   = 10000
    CHEMISTRY = 20000
    MEDICINE  = 30000
    PEACE     = 40000
    ECONOMICS = 50000

class Prize(object):
    def __init__(self, year, category, laureate_list):
        self.id =  category.value + year
        self.year =  year
        self.category = category
        self.laureate_list = laureate_list

prize = Prize(1998, Category.PHYSICS, [1,2])
print(str(prize.id))




