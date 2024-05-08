from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama

from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
# Langsmith tracking
# os.environ['LANGCHAIN_TRACING_V2'] = "true"
# os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
# os.environ["LANGCHAIN_ENDPOINT"] = "https://api.langchain.plus"
# os.environ["LANGCHAIN_PROJECT"] = os.getenv('LANGCHAIN_PROJECT2') 

app = FastAPI(
  title="Langchain Server",
  version="1.0",
  description="A simple API server"
)

add_routes(
  app,
  ChatOpenAI(),
  path='/openai'
)

model = ChatOpenAI()

llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about a {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about a {topic} with 100 words")

add_routes(
  app,
  prompt1|model,
  path="/essay"
)
add_routes(
  app,
  prompt2|llm,
  path="/poem"
)

if __name__ == "__main__":
  uvicorn.run(app, host="localhost", port=8000)