from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rides = []

@app.get("/")
def home():
    return ("Uber_clone running")

@app.post("/book_ride")
def book_ride(pickup : str, drop : str):
    ride= {
        "id": len(rides)+1,
        "pickup" : pickup,
        "drop" : drop,
        "status" : "waiting"
    }
    rides.append(ride)
    return ride

@app.get("/rides")
def get_rides():
    return rides

@app.get("/driver_loc/{ride_id}")
def driver_loc(ride_id:int):
    return {
        "lat": 18.5204 + random.uniform(-0.01, 0.01),
        "lng": 73.8567 + random.uniform(-0.01, 0.01) 
    }