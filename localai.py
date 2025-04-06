import traceback
import ollama

def localai_process_text(text, task, model_name):
    if not text:
        print("Error: No text provided.")
        return ""

    prompt = f"""
{task}

Input test:
---
{text}
---"""
    try:
        print(f"Sending request to Ollama using model '{model_name}' ...")
        response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        print(f"Error during Ollama call: {e}")
        traceback.print_exc()
        return ""

def trim_localai_response(localai_response):
    think_tag_end = localai_response.find('</think>')
    if think_tag_end != -1:
        return localai_response[think_tag_end + len('</think>'):].strip()
    return localai_response.strip()
