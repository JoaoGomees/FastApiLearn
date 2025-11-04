from typing import NotRequired, TypedDict

class Frequency(TypedDict):
    days_of_week: list[int]
    monthly: bool

    def __init__(self, monthly: bool, days_of_week: list[int]):
        self.days_of_week = days_of_week
        self.monthly = monthly

    def __str__(self):
        return f"Monthly: {self.monthly}"