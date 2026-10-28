import uuid,sqlite3
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import HTTPException
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
            "(patient_id,first_name,middle_name,last_name,sex,birth_date) "
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
def patientGET(patientId: str):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM patients "
            "WHERE patient_id=?",(patientId,)
        )
        row=cursor.fetchone()
    finally:
        if row is None:
            raise HTTPException(404,"Пациент не найден в базе")
        conn.close()
    return {
          "firstName":row[1],
          "middleName":row[2],
          "lastName":row[3],
          "sex":row[4],
          "birthDate":row[5]
        }

@router.put("")
def patientPUT(p: PatientBase):
    conn=sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "UPDATE patients "
            "SET first_name=?,middle_name=?,last_name=?,sex=?,birth_date=? "
            "WHERE patient_id=?",
            (p.firstName,p.middleName,p.lastName,p.sex,p.birthDate,p.patientId),
        )
        conn.commit()
    finally:
        conn.close()
    return{
         "message":"Пациент успешно обновлен"
         }

@router.delete("")
def patientDELETE(id: str):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    try:
        conn.execute(
            "DELETE FROM patients "
            "WHERE patient_id=?",(id,)
            )
    finally:
        conn.commit()
        conn.close()
    return {
        "message":"Пациент успешно удален"
    }