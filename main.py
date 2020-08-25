from typing import List
from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI()


class Food(BaseModel):
    name: str
    ingredients: List[str] = []


@app.post("/v1/food/")
def prepare_food(orders: List[Food]):
    all_ingredients = []
    for food in orders:
        for ingredient in food.ingredients:
            all_ingredients.append(ingredient.lower())
    return {"ingredients": all_ingredients}


@app.post("/v2/food/")
def prepare_food_v2(
    food: Food,
    delivery: bool = Query(False, description="Pack for delevery"),
):
    return {"mssage": f"preparing: {food.name}", "delivery": delivery}


@app.post("/v3/food/")
def prepare_food_v3(
    food: Food,
    quantity: int = Query(...,  gt=0, lt=50),
    delivery: bool = Query(False, description="Pack for delevery"),
):
    return {"mssage": f"preparing: {quantity} for {food.name}", "delivery": delivery}