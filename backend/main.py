from fastapi import FastAPI 
import requests

app = FastAPI()
BASE_URL = "https://anteaterapi.com/v2/rest"

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/majors")
def get_all_majors():
    #params = {"division": "Undergraduate"}
    response = requests.get(f"{BASE_URL}/programs/majors")
    return response.json()

@app.get("/major_requirements")
def get_major_requirements(programId: str):
    response = requests.get(f"{BASE_URL}/programs/major", params={"programId": programId})
    return response.json()