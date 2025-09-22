
from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "YOUR_API_KEY"  # Replace with your API-Football key
BASE_URL = "https://v3.football.api-sports.io"

headers = {
    "x-apisports-key": API_KEY
}

@app.get("/prediction")
def get_prediction(fixture_id: int):
    url = f"{BASE_URL}/predictions"
    response = requests.get(url, headers=headers, params={"fixture": fixture_id})
    data = response.json()

    if "response" not in data or not data["response"]:
        return {"error": "No prediction found"}

    prediction = data["response"][0]["predictions"]
    teams = data["response"][0]["teams"]

    home = teams["home"]["name"]
    away = teams["away"]["name"]
    winner = prediction["winner"]["name"] if prediction["winner"] else "No clear favorite"
    advice = prediction["advice"]
    scores = prediction["goals"]

    return {
        "match": f"{home} vs {away}",
        "winner": winner,
        "advice": advice,
        "predicted_score": f"{scores['home']} - {scores['away']}"
    }
