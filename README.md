\# LLM JobReach API



Deployed a fine-tuned LLaMA 3.1 model as a REST API using Modal.



\## 🚀 Features

\- Generates LinkedIn recruiter messages

\- Uses Hugging Face model

\- Real-time API



\## ▶️ Usage



```python

import requests



API\_URL = "https://adamasaipriya--llama-resume-api-generate.modal.run"



response = requests.post(

&#x20;   API\_URL,

&#x20;   json={"prompt": "Write a LinkedIn message for a Data Analyst role."}

)



print(response.json())

