import uuid
from fastapi import FastAPI
from fastapi import APIRouter
from models.patient import PatientIn, PatientOut, PatientBase

router=APIRouter(prefix="/patient")

@router.post("")
def patientPOST(patient: PatientIn):
    return PatientOut(
        id=str(uuid.uuid4()),
        firstName=patient.firstName,
        middleName=patient.middleName,
        lastName=patient.lastName,
        sex=patient.sex,
        birthDate=patient.birthDate,
        age=patient.age,
    )

@router.get("")
def patientGET(patient: PatientOut):
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