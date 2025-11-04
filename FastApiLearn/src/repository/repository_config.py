import pymongo

class Repository:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.database = self.client["GoalsDB"]

        