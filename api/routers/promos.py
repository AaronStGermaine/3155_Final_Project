from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promos as controller
from ..schemas import promos as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Promos'],
    prefix="/promos"
)


@router.post("/", response_model=schema.Promo)
def create(request: schema.PromoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Promo])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{promo_id}", response_model=schema.Promo)
def read_one(promo_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, promo_id=promo_id)


@router.put("/{promo_id}", response_model=schema.Promo)
def update(promo_id: int, request: schema.PromoUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, promo_id=promo_id)


@router.delete("/{promo_id}")
def delete(promo_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, promo_id=promo_id)
