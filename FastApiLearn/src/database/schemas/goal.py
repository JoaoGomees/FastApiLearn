import datetime
from bson import ObjectId

class Goal():
    description: str
    startDate: datetime
    endDate: datetime
    status: bool
    frequency: ObjectId 

    def __init__(self, description: str, frequency_id: ObjectId):
        self.description = description
        self.startDate = datetime.datetime.now()
        self.status = False
        self.frequency = frequency_id

    def __str__(self):
        return f"Description: {self.description}, StartDate: {self.startDate}, Status: {self.status}"