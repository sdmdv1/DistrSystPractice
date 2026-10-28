from pydantic import BaseModel

class PatientIn(BaseModel):
    firstName: str
    middleName: str
    lastName: str
    sex: str
    birthDate: str

class PatientOut(BaseModel):
    id: str
    firstName: str
    middleName: str
    lastName: str
    sex: str
    birthDate: str

class PatientBase(BaseModel):
    patientId: str
    firstName: str
    middleName: str
    lastName: str
    sex: str
    birthDate: str