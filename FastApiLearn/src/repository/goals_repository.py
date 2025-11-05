import pymongo
from src.repository.repository_config import Repository
from src.database.schemas.goal import Goal
from bson import ObjectId

class GoalsRepository(Repository):
    def __init__(self):
        super().__init__()
        self.collection = self.database["Goal"]

    def add_goal(self, goal: Goal):
        return self.collection.insert_one(goal.__dict__).inserted_id

    def get_goal(self, id: str):
        goal_data = self.collection.find_one({"_id": ObjectId(id)})
        if goal_data:
            return mapper.map_goal(goal_data)
        else:
            return {
                "message": "Goal not found"
            }
