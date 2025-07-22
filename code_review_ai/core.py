import os
import requests
from transformers import pipeline

USE_MODEL = os.getenv("USE_MODEL", "lmstudio")  # options: lmstudio, huggingface

if USE_MODEL == "huggingface":
    reviewer = pipeline("text-generation", model="sshleifer/tiny-gpt2")

def review_code(code: str) -> str:
    prompt = f"Review the following code:\n{code}"

    if USE_MODEL == "lmstudio":
        res = requests.post("http://localhost:1234/v1/completions", json={
            "model": "local-model",
            "prompt": prompt,
            "max_tokens": 500
        })
        return res.json()['choices'][0]['text']

    elif USE_MODEL == "huggingface":
        result = reviewer(prompt, max_new_tokens=300)[0]['generated_text']
        return result

    else:
        return "Invalid model configuration."
