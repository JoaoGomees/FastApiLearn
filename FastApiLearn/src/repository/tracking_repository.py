import pymongo
from repository.repository_config import Repository

class TrackingRepository(Repository):
    def __init__(self):
        self.collection = self.database["Tracking"]

    def add_tracking(self, tracking):
        self.collection.insert_one(tracking.__dict__)