from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

groq_api_key = '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'
os.environ["TAVILY_API_KEY"] = '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'

MODEL_NAMES = [
    "llama3-70b-8192",
    "distil-whisper-large-v3-en",
    "gemma2-9b-it",
    "mixtral-8x7b-32768"
]

tavily_tool = TavilySearchResults(max_results=2)

tools = [tavily_tool]

app = FastAPI(title='AI Agent LangGraph Chatbot')

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]



@app.post("/chat")
# To process asynchronously without blocking other request we can use async and await.
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with LangGraph Chatbot
    """


    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name, Please select a valid model name"}
    
    llm = ChatGroq(groq_api_key=groq_api_key, model_name=request.model_name)

    agent = create_react_agent(llm, tools=tools, state_modifier=request.system_prompt)

    state = {"messages": request.messages}

    result = agent.invoke(state)

    return result


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)


