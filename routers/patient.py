import uuid,sqlite3
from fastapi import FastAPI
from fastapi import APIRouter
from base.sqlite import DB_PATH
from models.patient import PatientIn, PatientOut, PatientBase

router=APIRouter(prefix="/patient")

@router.post("")
def patientPOST(p: PatientIn):
    conn=sqlite3.connect(DB_PATH)
    patientId=str(uuid.uuid4())
    try:
        conn.execute(
            "INSERT INTO patients "
            "(id,first_name,middle_name,last_name,sex,birth_date) "
            "VALUES (?,?,?,?,?,?)",
            (patientId,p.firstName,p.middleName,p.lastName,p.sex,p.birthDate)
        )
        conn.commit()
    finally:
        conn.close()
    return{
         "id":patientId,
         "message":"Пациент успешно создан"
         }

@router.get("")
def patientGET(p: PatientOut):

    return {
           
        }

@router.patch("")
def patientPATCH(patient: PatientBase):
    return {
           
        }

@router.delete("")
def patientDELETE(patient: PatientBase):
    return {
           
        }