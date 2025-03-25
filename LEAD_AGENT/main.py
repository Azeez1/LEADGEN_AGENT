from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from calendly import get_user_profile, get_scheduled_events

load_dotenv()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Lead Agent API is running"}

@app.post("/lead")
async def receive_lead(request: Request):
    data = await request.json()
    print("Received lead data:", data)
    return {"status": "success", "message": "Lead received!"}

@app.get("/calendly/user")
async def get_calendly_user():
    user_info = await get_user_profile()
    return user_info

@app.get("/calendly/events")
async def get_calendly_events():
    events = await get_scheduled_events()
    return events
