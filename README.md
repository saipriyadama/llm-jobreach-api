# 🚀 LLM JobReach API — Production-Style AI System

Deployed a fine-tuned **LLaMA 3.1 8B model** as a real-time API to generate personalized LinkedIn outreach messages from resume and job description inputs.

---

## 🎯 Why this project?

Most AI projects stop at prompting.

This system focuses on **real-world deployment**:

* Model hosting (Hugging Face)
* GPU inference (Modal)
* API layer (FastAPI)
* Output control (prompt + post-processing)

---

## 🧠 System Architecture

```
User Prompt → Hugging Face Model → Modal GPU Deployment → REST API → Clean Output
```

---

## ⚙️ Tech Stack

* Python
* Hugging Face Transformers
* LLaMA 3.1 (LoRA fine-tuned)
* Modal (GPU deployment)
* FastAPI

---

## 🤗 Model

Hugging Face Model:
https://huggingface.co/saipriyaadama/llama-3.1-8b-resume-outreach-v1

---

## 🔥 Key Features

* Generates personalized recruiter outreach messages
* Uses structured prompt engineering
* Removes hallucinated instructions and prompt leakage
* Live API endpoint for real-time usage

---

## 🚀 Live API

```python
import requests

API_URL = "https://adamasaipriya--llama-resume-api-generate.modal.run"

prompt = """
Write a concise LinkedIn message for a Data Analyst role.
Do not invent experience. Keep it under 90 words.
"""

response = requests.post(
    API_URL,
    json={"prompt": prompt},
    timeout=600
)

print(response.json()["response"])
```

---

## 💡 Challenges Solved

* Deploying a 16GB LLM with GPU inference
* Handling cold start latency in serverless environment
* Cleaning model output (removing repeated prompts + instructions)
* Controlling hallucination using prompt constraints

---

## 📈 Improvements over base model

* Better personalization for job outreach
* Reduced generic phrasing
* More structured and controlled outputs

---

## ⚠️ Limitations

* Response quality depends on input clarity
* May hallucinate if constraints are weak
* First request latency due to model loading

---

## 💼 Real-World Use Cases

* Automated job outreach generation
* Resume-to-job personalization tools
* Integration into AI job platforms

---

## 🛠️ Local Setup

```bash
pip install -r requirements.txt
modal deploy app.py
python test.py
```

---

## 👤 Author

Sai Priya Adama
