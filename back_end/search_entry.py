import json
import requests

class Laureate(object):

    def __init__(self, ID, image_link, wiki_link, prize_list, *args):
        self.id = ID
        self.image_link = image_link
        self.wiki_link = wiki_link
        self.prize_list = prize_list
        if len(args) == 5:
            self.entity = Person(args[0], args[1], args[2], args[3], args[4],)
        elif len(args) == 1:
            self.entity = Organization(args[0])

    def display_laureate(self):
        print(self.entity.description() + "and has a laureate ID of " + self.id )

        
class Person(object):
    def __init__(self, firstname, lastname, dob, dod, gender):
        self.lastname = lastname
        self.firstname = firstname
        self.dob = dob
        self.dod = dod
        self.gender = gender

    def description(self):
        return self.firstname + " " + self.lastname + " was born " + dob

class Organization(object):

    def __init__(self, org_name):
        self.org_name = org_name 

    def description(self):
        return "The organization " + self.org_name

if __name__=="__main__":
    test_laureate = Laureate(2, image_link)
