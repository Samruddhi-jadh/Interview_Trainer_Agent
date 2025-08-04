import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("IBM_API_KEY")
INSTANCE_ID = os.getenv("IBM_INSTANCE_ID")
URL = os.getenv("IBM_URL")
DEPLOYMENT_ID = os.getenv("IBM_DEPLOYMENT_ID")

def query_granite(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": DEPLOYMENT_ID,
        "input": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7
        }
    }

    response = requests.post(
        f"{URL}/ml/v1/deployments/{DEPLOYMENT_ID}/predictions",
        json=payload,
        headers=headers
    )

    if response.status_code == 200:
        return response.json()["results"][0]["generated_text"]
    else:
        return f"⚠️ API Error {response.status_code}: {response.text}"
