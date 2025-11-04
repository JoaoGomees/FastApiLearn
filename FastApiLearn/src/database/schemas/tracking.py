import datetime
from bson import ObjectId

class Tracking():
    goal: ObjectId
    day: datetime

    def __init__(self, goal_id: ObjectId, day: datetime):
        self.goal = goal_id
        self.day = day

    def __str__(self):
        return f"Day: {self.day}"