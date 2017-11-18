import json
import requests
import prize
import wikipedia as Wiki

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
            self.born_city = data['bornCity']
            self.born_country = data['bornCountry']
        except:
            self.surname = ""
            self.born_city = ""
            self.born_country = ""
            #print("Exception!" + json.dumps(data, indent=4, sort_keys=True))
        if self.firstname != "" and self.surname != "":
            self.description = Wiki.summary(self.firstname + " "+ self.surname)
            self.wiki_link= Wiki.page(self.firstname + " " + self.surname).url
        elif self.firstname != "":
            self.description = Wiki.summary(self.firstname)
            self.wiki_link= Wiki.page(self.firstname).url
        else:
            self.wiki_link = ""
            self.description = ""



    def show(self):
        print(self.firstname + " " + self.surname + "has a laureate ID of " + str(self.id ) + " and was awarded the nobel prizes: " + str(self.prize_list.items()))
        
