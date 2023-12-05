from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import payment_info as controller
from ..schemas import payment_info as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payment Info'],
    prefix="/payment_info"
)


@router.post("/", response_model=schema.PaymentInfo)
def create(request: schema.PaymentInfoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PaymentInfo])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{payment_id}", response_model=schema.PaymentInfo)
def read_one(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id=payment_id)


@router.put("/{payment_id}", response_model=schema.PaymentInfo)
def update(payment_id: int, request: schema.PaymentInfoUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, payment_id=payment_id)


@router.delete("/{payment_id}")
def delete(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, payment_id=payment_id)
