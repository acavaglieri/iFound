from datetime import datetime, date
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.sql.expression import asc, desc
from src.models import user as u_model
from src.cruds import users as u_crud
from src.models import payments as p_model
from src.schemas import payments as p_schemas


def get_payment_by_id(db: Session, payment_id: int):
    return db.query(p_model.Payments).filter(p_model.Payments.id == payment_id).first()


def get_payments(db: Session, filter: p_schemas.PaymentsFilter):
    conditions = []
    limit = None
    skip = filter.skip
    order = asc
    if filter.id:
        conditions.append(p_model.Payments.id == filter.id)
    if filter.receiver_federal_id:
        conditions.append(u_model.User.federal_id.like(
            f'%{filter.receiver_federal_id}%'))
    if filter.amount:
        conditions.append(p_model.Payments.amount == filter.amount)
    if filter.scheduled_date:
        conditions.append(p_model.Payments.scheduled_date ==
                          filter.scheduled_date)
    if filter.description:
        conditions.append(p_model.Payments.description.like(
            f'%{filter.description}%'))
    if filter.after_date:
        conditions.append(p_model.Payments.scheduled_date > filter.after_date)
    if filter.limit:
        limit = int(filter.limit)

    columns = [*p_model.Payments.__table__.columns,
               u_model.User.name.label("receiver_name")]
    db_query = db.query(
        *columns).where(p_model.Payments.approved == "waiting").join(u_model.User)

    for i in range(len(conditions)):
        db_query = db_query.filter(conditions[i])
    db_payments_total_count = db_query.count()

    if filter.sort:
        if filter.order == False:
            order = asc
        elif filter.order == True:
            order = desc
        db_query = db_query.order_by(
            order(filter.sort)).limit(limit).offset(skip)
        return db_query.all(), db_payments_total_count
    else:
        db_query = db_query.limit(limit).offset(skip)
        return db_query.all(), db_payments_total_count


def create_payment(db: Session, new_payment_data):
    receiver = u_crud.get_user_by_federal_id(
        db, new_payment_data.receiver_federal_id)
    new_payment_dict = new_payment_data.dict()
    del new_payment_dict["receiver_federal_id"]
    new_payment_dict["receiver_id"] = receiver.id
    new_payment_dict["created_at"] = datetime.today()
    new_payment_dict["updated_at"] = datetime.today()
    db_payment = p_model.Payments(**new_payment_dict, approved="waiting")
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def update_payment(db: Session, new_payment_data: p_schemas.PaymentUpdateRequest, payment_id: int):
    db_payment = update(p_model.Payments)\
        .where(p_model.Payments.id == payment_id)\
        .values(**new_payment_data.dict(exclude_unset=True), updated_at=datetime.today())
    db.execute(db_payment)
    db.commit()
