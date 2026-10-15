from fastapi import FastAPI
from fastapi import APIRouter
from models.episode import EpisodeIn, EpisodeOut, EpisodeBase

router=APIRouter(prefix="episode")

@router.post("/")
def episodePOST(episode: EpisodeIn):
    return {
        
    }

@router.get("/")
def episodeGET(episode: EpisodeOut):
    return {
           
        }

@router.patch("/")
def episodePATCH(patient: EpisodeBase):
    return {
           
        }

@router.patch("/")
def episodeDELETE(patient: EpisodeBase):
    return {
           
        }