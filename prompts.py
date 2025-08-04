EXTRACT_INFO_PROMPT = "Extract the job role and experience level from this resume:\n{text}"

GEN_QUESTIONS_PROMPT = """
Generate 5 technical and 5 HR questions for a candidate applying as a {job_role} with {experience_level} experience.
"""

GEN_ANSWERS_TIPS_PROMPT = """
For each of these questions, give:
1. A model answer
2. 3 improvement tips
Questions:\n{questions}
"""
