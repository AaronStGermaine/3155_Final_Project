from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import foods as controller
from ..schemas import foods as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Foods'],
    prefix="/foods"
)


@router.post("/", response_model=schema.Food)
def create(request: schema.FoodCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Food])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{food_id}", response_model=schema.Food)
def read_one(food_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, food_id=food_id)


@router.put("/{food_id}", response_model=schema.Food)
def update(food_id: int, request: schema.FoodUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, food_id=food_id)


@router.delete("/{food_id}")
def delete(food_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, food_id=food_id)
