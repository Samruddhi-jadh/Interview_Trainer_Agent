import json

def get_questions_by_role(job_role: str) -> dict:
    with open("data/interview_questions.json", "r") as f:
        data = json.load(f)
    role = job_role.strip().title()
    return data.get(role, {"technical": [], "hr": []})
