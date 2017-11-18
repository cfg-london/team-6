import json
import requests
import prize

class Laureate(object):


    def __init__(self, data):
        switcher = {
                'physics': 10000,
                'chemistry': 20000,
                'medicine' : 30000,
                'peace'    : 40000,
                'literature': 50000,
                'economics': 60000,
                }
        self.id = int(data['id'])
        self.image_link = ""
        self.wiki_link = ""
        self.prize_list = {}
        for p in data['prizes']:
            try:
                return_id = int(p['year'])
                p_id = return_id + switcher[p['category']]
                self.prize_list[p_id] = p
            except:
                pass
        self.dob = data['born']
        self.dod = data['died']
        print(json.dumps(data, indent=4, sort_keys=True))
        try:
            self.firstname = data['firstname']
            self.gender = data['gender']
        except:
            self.firstname = ""
            self.gender = ""
        try:
            self.surname = data['surname']
            #self.born_city = data['bornCity']
            self.born_country = data['bornCountry']
        except:
            self.surname = ""
            self.born_city = ""
            self.born_country = ""
            #print("Exception!" + json.dumps(data, indent=4, sort_keys=True))

    def show(self):
        
        print(self.firstname + " " + self.surname + "has a laureate ID of " + str(self.id ) + " and was awarded the nobel prizes: " + str(self.prize_list.items()))

        
class Person(object):
    def __init__(self, firstname, lastname, dob, dod, gender):
        self.lastname = lastname
        self.firstname = firstname
        self.dob = dob
        self.dod = dod
        self.gender = gender

    def description(self):
        return self.firstname + " " + self.lastname + " was born " + self.dob

class Organization(object):

    def __init__(self, org_name):
        self.org_name = org_name 

    def description(self):
        return "The organization " + self.org_name

