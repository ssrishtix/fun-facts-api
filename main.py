from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import random
from facts import facts

app = FastAPI()

# Pydantic model for POST requests
class Fact(BaseModel):
    text: str
    category: Optional[str] = "general"

@app.get("/")
def home():
    return {"message": "Welcome to the Upgraded Fast Facts API!"}

@app.get("/fact")
def get_random_fact():
    return random.choice(facts)

@app.get("/facts", response_model=List[dict])
def get_all_facts():
    return facts

@app.post("/facts")
def add_fact(new_fact: Fact):
    new_id = max(f["id"] for f in facts) + 1 if facts else 1
    fact_dict = {
        "id": new_id,
        "text": new_fact.text,
        "category": new_fact.category
    }
    facts.append(fact_dict)
    return {"message": "Fact added!", "fact": fact_dict}
