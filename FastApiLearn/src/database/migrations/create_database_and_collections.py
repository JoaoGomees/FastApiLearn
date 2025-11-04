from database.schemas.frequency import Frequency
from database.schemas.goal import Goal
from database.schemas.tracking import Tracking
import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient("localhost", 27017)

#database creation called GoalsDB
database = client["GoalsDB"] 

#collections creation 
database.create_collection("Goal")
database.create_collection("Frequency")
database.create_collection("Tracking")