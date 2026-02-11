import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import Groqllm

import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

# os.environ["LANGSMIT_API_KEY"] = os.getenv("LANGSMIT_API_KEY")

@app.post("/blogs")
async def create_blog(request: Request):
    data = await request.json()
    topic = data["topic"]

    ##Get LLM
    groqllm = Groqllm()
    llm=groqllm.get_llm()

    ##Get graph
    graph_builder=GraphBuilder(llm)
    if topic:
        graph=graph_builder.setup_graph(usecase="blog_creation")
        state=graph.invoke({"topic":topic})

    return {"data":state}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
