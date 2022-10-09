from fastapi.responses import FileResponse
from main import *
from fastapi import Body, Depends, HTTPException
from sqlalchemy.orm import Session
from src.cruds import users as u_crud
from src.schemas import users as u_schemas
from src.schemas import status as s_schemas
from src.schemas import token as t_schemas
from src.services import email_sender, xlsx_generator
from src.resources import authentication as auth
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.routes.get_db import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
import os


@app.get("/user/token/{token}/", tags=["Users"], response_model=u_schemas.UserByToken)
def get_user_by_token(token: str, db: Session = Depends(get_db)):
    db_user = u_crud.get_user_email_by_token(db, token)
    if db_user:
        return u_schemas.UserByToken(status="success", email=db_user.email)
    else:
        raise HTTPException(status_code=400, detail="Token inválido!")

@app.get("/user/me/", tags=["Users"], response_model=u_schemas.User)
def read_users_me(current_user: u_schemas.User = Depends(auth.get_current_user)):
    return current_user

@app.post("/user/login", tags=["Users"], response_model=t_schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    ''' O Token de login expira em 60 minutos '''
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha incorretos!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]))
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    user_response = u_schemas.UserLoginResponse(role=user.role, email=user.email)
    return t_schemas.Token(access_token=access_token, token_type="bearer", status="success", message="Logado com sucesso", user=user_response)

@app.post("/user/xlsx/generate", tags=["Users"], dependencies=[Depends(auth.valid_ability_user)])
def create_user_xlsx_file(filter: u_schemas.UsersFilter, db: Session = Depends(get_db)):
    filename = xlsx_generator.create_xlsx_file_for_users(db, filter)
    return FileResponse('/tmp/{}'.format(filename), media_type='application/octet-stream', filename="usuarios.xlsx")

@app.post("/users/list", tags=["Users"], response_model= u_schemas.AllUsers, dependencies=[Depends(auth.valid_ability_user)])
def list_users(db: Session = Depends(get_db), filter: u_schemas.UsersFilter = Body(..., embed=True)):
    db_users, db_users_total_count = u_crud.get_users(db, filter)
    response = {
        'users_total_count': db_users_total_count,
        'users': jsonable_encoder(db_users)
    }
    return JSONResponse(content=response)

@app.post("/user/get/token", tags=["Users"], response_model=s_schemas.StatusModel)
def user_generate_reset_token(user_email: u_schemas.UserResetPassEmail, db: Session = Depends(get_db)):
    db_user = u_crud.get_user_by_email(db, user_email.email)
    if db_user:
        email_data = u_crud.generate_email_data(db_user, "reset")
        sent_email_status = email_sender.email_sender(db_user.email, email_data["message"], "Redefinição de Senha")
        if(sent_email_status == "success"):
            u_crud.insert_user_token(db, user_email.email, email_data["token"])
        return s_schemas.StatusModel(status="success", message="Email enviado! Cheque sua caixa de entrada e spam")
    if not db_user:
        raise HTTPException(status_code=400, detail="Não é possível enviar o email, cheque seus dados!")

@app.post("/user/register", tags=["Users"], response_model=s_schemas.StatusModel)
def register_user(user: u_schemas.UserCreate = Body(..., embed=True), db: Session = Depends(get_db)):
    db_user = u_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado!")
    db_user = u_crud.get_user_by_phone(db, phone=user.cellphone)
    if db_user:
        raise HTTPException(status_code=400, detail="Celular já cadastrado!")
    db_user = u_crud.get_user_by_federal_id(db, user.federal_id)
    if db_user:
        raise HTTPException(status_code=400, detail="CPF já cadastrado!")
    else:
        db_user = u_crud.register_user(db, user)
        if db_user:
            email_data = u_crud.generate_email_data(user, "register")
            # sent_email_status = email_sender.email_sender(user.email, email_data["message"], "Confirmação de Conta Paylog")
            # if sent_email_status == "success":            
            u_crud.insert_user_token(db, user.email, email_data["token"])
            added_user = u_crud.get_user_by_email(db, user.email)
            return s_schemas.StatusModel(status="success", message="Usuário adicionado com sucesso!")

@app.post("/user/save", tags=["Users"], response_model=s_schemas.StatusModel, dependencies=[Depends(auth.valid_ability_user)])
def register_user(user: u_schemas.UserCreate = Body(..., embed=True), db: Session = Depends(get_db)):
    db_user = u_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado!")
    db_user = u_crud.get_user_by_phone(db, phone=user.cellphone)
    if db_user:
        raise HTTPException(status_code=400, detail="Celular já cadastrado!")
    db_user = u_crud.get_user_by_federal_id(db, user.federal_id)
    if db_user:
        raise HTTPException(status_code=400, detail="CPF já cadastrado!")
    db_user = u_crud.register_user(db, user)
    return s_schemas.StatusModel(status="success", message="Usuário adicionado com sucesso!")

@app.post("/user/confirm", tags=["Users"], response_model=s_schemas.StatusModel)
def user_confirm(token: u_schemas.UserToken, db: Session = Depends(get_db)):
    db_user = u_crud.get_user_email_by_token(db, token.token)
    if not db_user:
        raise HTTPException(status_code=400, detail="Token inválido!")
    else:
        u_crud.confirm_user(db, token)
        return s_schemas.StatusModel(status="success", message="Conta confirmada!")

@app.put("/user/reset/password", tags=["Users"], response_model=s_schemas.StatusModel)
def user_reset_pass(user: u_schemas.UserResetPass, token: u_schemas.UserToken, db: Session = Depends(get_db)):
    db_user = u_crud.get_user_email_by_token(db, token.token)
    if not db_user:
        raise HTTPException(status_code=400, detail="Token inválido!")
    if db_user.email != user.email:
        raise HTTPException(status_code=400, detail="Email inválido!")
    db_user = u_crud.user_reset_password(db, user, token)
    if db_user:
        return s_schemas.StatusModel(status="success", message="Senha alterada com sucesso!")
    else:
        raise HTTPException(status_code=400, detail="Não foi possível redefinir sua senha!")

@app.put("/user/update/{user_id}", tags=["Users"], response_model=s_schemas.StatusModel)
def update_user(user_id: int, user: u_schemas.UserUpdate = Body(..., embed=True), db: Session = Depends(get_db),
current_user: u_schemas.User = Depends(auth.get_current_active_user)):
    if current_user.id != user_id and current_user.role != 'admin':
        raise HTTPException(status_code=403, detail="Você não possui autorização para executar esta ação")
    db_user = u_crud.get_user_by_email(db, email=user.email)
    if db_user and db_user.id != user_id:
        raise HTTPException(status_code=400, detail="Email já cadastrado!")
    db_user = u_crud.get_user_by_phone(db, phone=user.cellphone)
    if db_user and db_user.id != user_id:
        raise HTTPException(status_code=400, detail="Celular já cadastrado!")
    db_user = u_crud.get_user_by_federal_id(db, user.federal_id)
    if db_user and db_user.id != user_id:
        raise HTTPException(status_code=400, detail="CPF já cadastrado!") 
    u_crud.update_user(db, user, user_id)
    return s_schemas.StatusModel(status="success", message="Usuário atualizado!")

@app.delete("/user/delete/{user_id}", tags=["Users"], response_model= s_schemas.StatusModel)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: u_schemas.User = Depends(auth.valid_ability_user)):
    db_user = u_crud.get_user_by_id(db, user_id)    
    if db_user.id == current_user.id:
        raise HTTPException(status_code=403, detail="Impossível excluir você mesmo!")
    if not db_user:
        raise HTTPException(status_code=404, message="Usuário não encontrado!")
    db_user = u_crud.delete_user(db, user_id)
    return s_schemas.StatusModel(status="success", message="Usuário deletado!")


