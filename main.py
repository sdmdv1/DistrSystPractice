from fastapi import FastAPI
from fastapi.responses import FileResponse
from routers.patient import router as patientRouter
from base.sqlite import initDB
initDB()
app = FastAPI()
app.include_router(patientRouter)

@app.get("/")
def mainPage():
    return FileResponse("html/welcome.html")


