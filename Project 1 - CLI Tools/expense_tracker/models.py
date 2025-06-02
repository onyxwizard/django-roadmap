# models.py
from dataclasses import dataclass
from datetime import date, time

@dataclass
class Expense:
    category: str
    description: str
    expense_date: date
    expense_time: time
    amount: float