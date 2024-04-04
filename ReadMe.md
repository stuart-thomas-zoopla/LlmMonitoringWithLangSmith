# LLM monitoring with LangSmith
This repository contains an example integration of LangSmith in a python application. You can read the associated blog post on [The Quality Duck](Insert-link) website.

test.py contains the necessary code to provide a prompt to Ollama running a Llama 2 model and captures a trace that it will forward to LangSmith - You will need to set your envionment variables accordingly in order for this to work:

LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="<my-api-key>"
LANGCHAIN_PROJECT="LiteLLM"

eval.py contains an example of tests you can run against datasets in LangSmith.