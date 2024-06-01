#!/usr/bin/env python
"""Example LangChain server exposes a retriever."""
from fastapi import FastAPI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings

from langserve import add_routes

# # OpenAI API key should only use env var: OPENAI_API_KEY
# embedding = OpenAIEmbeddings()

# Azure OpenAI API key should only use the following variables
azure_openai_api_type = "azure"
azure_openai_api_base = "https://" + <azure-ai-service-id> + ".openai.azure.com/openai/deployments/" + <azure-deployment> + "/"
azure_openai_api_key = <azure-openai-api-key>
azure_openai_api_version = "2024-02-15-preview"
embedding = AzureOpenAIEmbeddings(
    openai_api_type=azure_openai_api_type,
    openai_api_base=azure_openai_api_base,
    openai_api_key=azure_openai_api_key,
    openai_api_version=azure_openai_api_version,
)

vectorstore = FAISS.from_texts(
    ["cats like fish", "dogs like sticks"], embedding=embedding
)
retriever = vectorstore.as_retriever()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)
# Adds routes to the app for using the retriever under:
# /invoke
# /batch
# /stream
add_routes(app, retriever)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
