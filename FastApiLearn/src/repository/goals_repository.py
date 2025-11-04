import pymongo
from src.repository.repository_config import Repository
from src.database.schemas.goal import Goal
from bson import ObjectId

class GoalsRepository(Repository):
    def __init__(self):
        super().__init__()
        self.collection = self.database["Goal"]

    def add_goal(self, goal: Goal):
        self.collection.insert_one(goal.__dict__)

        
