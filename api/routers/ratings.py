from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import ratings as controller
from ..schemas import ratings as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Ratings'],
    prefix="/ratings"
)


@router.post("/", response_model=schema.Rating)
def create(request: schema.RatingCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Rating])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{rating_id}", response_model=schema.Rating)
def read_one(rating_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, rating_id=rating_id)


@router.put("/{rating_id}", response_model=schema.Rating)
def update(rating_id: int, request: schema.RatingUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, rating_id=rating_id)


@router.delete("/{rating_id}")
def delete(rating_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, rating_id=rating_id)
