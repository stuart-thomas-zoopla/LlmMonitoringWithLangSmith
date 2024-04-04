import litellm
from langsmith import traceable

@traceable
def exceutePrompt(prompt: str):
    response = litellm.completion(
            model="ollama/llama2",
            messages = [{ "content": prompt,"role": "user"}],
            api_base="http://localhost:11434",
    )
    print(response)
    return response

exceutePrompt("Why is the sky blue?")