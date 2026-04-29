import modal

image = modal.Image.debian_slim().pip_install(
    "fastapi[standard]",
    "pydantic",
    "transformers",
    "torch",
    "accelerate",
    "huggingface_hub"
)

app = modal.App("llama-resume-api")

MODEL_NAME = "saipriyaadama/llama-3.1-8b-resume-outreach-v1"

@app.function(image=image, gpu="A10G", timeout=600)
@modal.fastapi_endpoint(method="POST")
async def generate(payload: dict):
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch

    prompt = payload.get("prompt", "")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=120,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        repetition_penalty=1.15,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated_text = full_text.replace(prompt, "").strip()

    stop_phrases = [
        "If no name is available",
        "Copy and paste",
        "---",
        "Write a LinkedIn message",
        "Stop after the message",
        "Do not add"
    ]

    for phrase in stop_phrases:
        if phrase in generated_text:
            generated_text = generated_text.split(phrase)[0].strip()

    return {"response": generated_text}