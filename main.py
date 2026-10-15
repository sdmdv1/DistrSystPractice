from fastapi import FastAPI
from fastapi.responses import FileResponse
from routers.patient import router as patientRouter
app = FastAPI()
app.include_router(patientRouter)
@app.get("/")
def main():
    return FileResponse("html/welcome.html")


