from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas import order_details as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)


@router.post("/", response_model=schema.OrderDetail)
def create(request: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{orderDetail_id}", response_model=schema.OrderDetail)
def read_one(orderDetail_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, orderDetail_id=orderDetail_id)


@router.put("/{orderDetail_id}", response_model=schema.OrderDetail)
def update(orderDetail_id: int, request: schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, orderDetail_id=orderDetail_id)


@router.delete("/{orderDetail_id}")
def delete(orderDetail_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, orderDetail_id=orderDetail_id)
