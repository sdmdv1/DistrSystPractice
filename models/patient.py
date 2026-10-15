from pydantic import BaseModel

class PatientIn(BaseModel):
    firstName: str
    middleName: str
    lastName: str
    sex: str
    birthDate: str
    age: int

class PatientOut(BaseModel):
    id: str
    firstName: str
    middleName: str
    lastName: str
    sex: str
    birthDate: str
    age: int

class PatientBase(BaseModel):
    id: str
    firstName: str
    middleName: str
    lastName: str
    sex: str
    birthDate: str
    age: int