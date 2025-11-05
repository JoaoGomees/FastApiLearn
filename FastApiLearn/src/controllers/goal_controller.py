from fastapi import APIRouter, FastAPI
from src.database.schemas.goal import Goal
from src.repository.goals_repository import GoalRepository

goal_router = APIRouter()
goal_repo = GoalRepository()

@goal_router.get("/get")
async def get_goals(id: str):
    goal = goal_repo.get_goal(id)
    return {
        "msg": "Goal retrieved successfully",
        "goal": goal
    }

@goal_router.post("/create")
async def create_goals(goal_model):
    new_goal = Goal(goal_model.description, goal_model.frequency)
    id =  goal_repo.add_goal(new_goal).inserted_id

    return {
        "msg": "New goal created successfully",
        "goal_id": str(id)
    }
