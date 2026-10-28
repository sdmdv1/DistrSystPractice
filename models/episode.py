
from pydantic import BaseModel

class EpisodeIn(BaseModel):
    patientId: str
    timestamp: str
    vitals: Vitals
    symptoms: Symptoms

class EpisodeOut(BaseModel):
    episodeId: str
    timestamp: str
    vitals: Vitals
    symptoms: Symptoms

class EpisodeBase(BaseModel):
    episodeId: str
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
