from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import src
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from random import randint

app = FastAPI(
    version="0.0.1",
    nome="iFound",
)

origins = [
    "*"
]

PETS = [
    {
        'id': randint(1, 1000000),
        'nome': 'Thor',
        'raca': 'Pastor Alemão',
        'vacinado': True
    },
    {
        'id': randint(1, 1000000),
        'nome': 'Kitty',
        'raca': 'Gato',
        'vacinado': True
    }
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.routes import users, payments, google_services 

@app.get("/", summary="", tags=["Default"])
def read_root():
    return {"iFound": "Backend"}



@app.get('/pets')
def all_pets():
    return jsonable_encoder({
        'status': 'success',
        'pets': PETS
    })


class Pet(BaseModel):
    nome: str
    raca: str
    vacinado: bool

@app.post('/pets')
def save_pets(pet: Pet):
    response_object = {'status': 'success'}
    PETS.append({
        'id': randint(1, 1000000),
        'nome': pet.nome,
        'raca': pet.raca,
        'vacinado': pet.vacinado
    })
    response_object['message'] = 'Pet added!'
    return jsonable_encoder(response_object)

@app.put('/pets/{pet_id}')
def update_pet(pet_id: int, pet: Pet):
    pet_for_update=[ pet for pet in PETS if pet['id'] == pet_id ][0]
    response_object = {'status': 'success'}
    pet_for_update['nome']=pet.nome
    pet_for_update['raca']=pet.raca
    pet_for_update['vacinado']=pet.vacinado
    response_object['message'] = 'Pet updated!'
    return response_object
    
@app.delete('/pets/{pet_id}')
def delete_pet(pet_id: int):
    response_object = {'status': 'success'}
    for pet in PETS:
        if pet['id'] == pet_id:
            PETS.remove(pet)

    response_object['message'] = 'Pet removed!'
    return response_object