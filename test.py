import requests

API_URL = "https://adamasaipriya--llama-resume-api-generate.modal.run"

prompt = """
You are an expert at writing honest, personalized LinkedIn recruiter messages.

Return ONLY the final message.
Do NOT include subject line.
Do NOT invent years, company names, job titles, metrics, or experience.
Use only the candidate details provided below.
Keep it between 60 and 90 words.
Stop after the message. Do not add instructions, explanations, notes, or alternatives.
Use "Hello" if recruiter name is unknown. Do not use placeholders like [Name].

Candidate:
Data Analyst with experience in Power BI, SQL, Python, ETL, Excel automation, dashboard reporting, and stakeholder communication.

Job:
Data Analyst role requiring SQL, Power BI, reporting, data cleaning, dashboard development, and business communication.

Write a LinkedIn message to a recruiter.
"""

response = requests.post(
    API_URL,
    json={"prompt": prompt},
    timeout=600
)

print("Status:", response.status_code)
print("Text:", response.text)