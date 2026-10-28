import uuid,sqlite3
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import HTTPException
from models.episode import EpisodeIn, EpisodeOut, EpisodeBase
from base.sqlite import DB_PATH


router=APIRouter(prefix="/episode")

@router.post("")
def episodePOST(e: EpisodeIn):
    conn=sqlite3.connect(DB_PATH)
    episodeId=str(uuid.uuid4())
    try:
        conn.execute(
            "INSERT INTO episodes "
            "(patient_id,episode_id,time_stamp,heart_rate_bpm,blood_pressure_systolic,blood_pressure_diastolic," \
            "oxygen_saturation,chest_pain_level,dyspnea_level) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            (   
                e.patientId,
                episodeId,
                e.timestamp,
                e.vitals.heartRateBmp,
                e.vitals.bloodPressureSystolic,
                e.vitals.bloodPressureDiastolic,
                e.vitals.oxygenSaturation,
                e.symptoms.chestPainLevel,
                e.symptoms.dyspneaLevel
            ),
        )
        conn.commit()
    finally:
        conn.close()
    return {
        "episodeId":episodeId,
        "message": "Эпизод успешно создан"
    }

@router.get("")
def episodeGET(episodeId: str):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM episodes "
            "WHERE episode_id=?",(episodeId,)
        )
        row=cursor.fetchone()
    finally:
        if row is None:
            raise HTTPException(404,"Эпизод не найден в базе")
        conn.close()
    return {
           "patientId":row[1],
           "timestamp":row[2],
           "heartRateBpm":row[3],
           "bloodPressureSystolic":row[4],
           "bloodPressureDiastolic":row[5],
           "oxygenSaturation":row[6],
           "chestPainLevel":row[7],
           "dyspneaLevel":row[8]
        }

@router.patch("")
def episodePATCH(patient: EpisodeBase):
    return {
           
        }

@router.delete("")
def episodeDELETE(id: str):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    try:
        conn.execute(
            "DELETE FROM episodes "
            "WHERE episode_id=?",(id,)
        )
        row=cursor.fetchone()
        if row is None:
            raise HTTPException(404,"Эпизод не найден в базе")
    finally:
        conn.commit()
        conn.close()
    return {
        "message":"Эпизод успешно удален"
    }