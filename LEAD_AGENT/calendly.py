import os
import httpx
from dotenv import load_dotenv
import json
load_dotenv()

BASE_URL = "https://api.calendly.com"
ACCESS_TOKEN = os.getenv("CALENDLY_ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

async def get_user_profile():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/users/me", headers=HEADERS)
        return res.json()

async def get_scheduled_events():
    # First, get the current user's URI (you need this for event queries)
    user_data = await get_user_profile()
    user_uri = user_data.get("resource", {}).get("uri")

    if not user_uri:
        return {"error": "User URI not found"}

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BASE_URL}/scheduled_events?user={user_uri}",
            headers=HEADERS
        )
        return res.json()


def get_mock_events():
    with open("mock_data/calendly_events.json", "r") as f:
        return json.load(f)
