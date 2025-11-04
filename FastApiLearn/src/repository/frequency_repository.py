import pymongo
from repository.repository_config import Repository

class FrequencyRepository(Repository):
    def __init__(self):
        super().__init__()
        self.collection = self.database["Frequency"]

    def add_frequency(self, frequency):
        self.collection.insert_one(frequency.__dict__)