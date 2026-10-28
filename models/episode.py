
from pydantic import BaseModel

class EpisodeIn(BaseModel):
    patientId: str
    timestamp: str
    vitals: Vitals
    symptoms: Symptoms

class EpisodeOut(BaseModel):
    id: str
    timestamp: str
    vitals: Vitals
    symptoms: Symptoms

class EpisodeBase(BaseModel):
    id: str
    timestamp: str
    vitals: Vitals
    symptoms: Symptoms

class Vitals(BaseModel):
    heartRateBmp: int
    bloodPressureSystolic: int
    bloodPressureDiastolic: int
    oxygenSaturation: int

class Symptoms(BaseModel):
    chestPainLevel: int
    dyspneaLevel: int
