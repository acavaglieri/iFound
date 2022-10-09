from main import *
import os
from datetime import date
from fastapi import Body, Depends, HTTPException
from sqlalchemy.orm import Session
from .get_db import get_db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.schemas import payments as p_schemas
from src.schemas import status as s_schemas
from src.schemas import banks_schemas as b_schemas
from src.cruds import payments as p_cruds
from src.cruds import users as u_cruds
from src.schemas import users as u_schemas
from src.resources import authentication as auth


@app.post("/payments/list", tags=["Payments"], response_model=p_schemas.AllPayments, dependencies=[Depends(auth.valid_ability_user)])
def list_payments(db: Session = Depends(get_db), filter: p_schemas.PaymentsFilter = Body(..., embed=True)):
    payments, payments_total_count = p_cruds.get_payments(db, filter)
    response = {
        'payments_total_count': payments_total_count,
        'payments': jsonable_encoder(payments)
    }
    return JSONResponse(content=response)


@app.post("/payments/create", tags=["Payments"], response_model=s_schemas.StatusModel,  dependencies=[Depends(auth.valid_ability_user)])
def create_payment(db: Session = Depends(get_db), new_payment_data: p_schemas.PaymentCreateRequest = Body(..., embed=True)):
    p_cruds.create_payment(db, new_payment_data)
    return s_schemas.StatusModel(status="success", message="Pagamento criado com sucesso!")


@app.put("/payments/update/{payment_id}", tags=["Payments"], response_model=s_schemas.StatusModel,  dependencies=[Depends(auth.valid_ability_user)])
def update_payment(payment_id: int, db: Session = Depends(get_db), new_payment_data: p_schemas.PaymentUpdateRequest = Body(..., embed=True)):
    payment = p_cruds.get_payment_by_id(db, payment_id)
    if not payment:
        raise HTTPException(
            status_code=400, detail="Pagamento não encontrado!")
    p_cruds.update_payment(db, new_payment_data, payment_id)
    return s_schemas.StatusModel(status="success", message="Pagamento atualizado com sucesso!")


@app.get("/payments/pay/scheduled", tags=["Payments"])
def pay_scheduled_payments(current_user: u_schemas.User = Depends(auth.get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403, detail="Você não possui permissão para esse recurso!")
    return scheduled_payments


@app.put("/payments/{bank}/pay/{payment_id}", tags=["Payments"], response_model=s_schemas.StatusModel,  dependencies=[Depends(auth.valid_ability_user)])
def pay_payment(payment_id: int, bank: str, db: Session = Depends(get_db), current_user: u_schemas.User = Depends(auth.get_current_user), new_payment_data: p_schemas.PaymentUpdateRequest = Body(..., embed=True)):
    payment = p_cruds.get_payment_by_id(db, payment_id)
    receiver = u_cruds.get_user_by_id(db, payment.receiver_id)
    transaction_dict = {
        "amount": int(payment.amount),
        "to_or_from": payment.receiver_id,
        "credit_or_debit": "debit",
        "user_id": current_user.id,
        "date": date.today()
    }
    response = t_cruds.validate_transaction_data(transaction_dict)
    if response:
        if True:
            # Caso a transação dê certo, insere ela na tabela transactions:
            response = t_cruds.insert_transaction(db, transaction_dict)
            new_payment_data["paid"] = True
            p_cruds.update_payment(db, new_payment_data, payment_id)
            return s_schemas.StatusModel(status="success", message="Transferência realizada com sucesso!")
