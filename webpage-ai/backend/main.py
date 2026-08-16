from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_classic.output_parsers import PydanticOutputParser
import os


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

if not api_key:
    raise ValueError("HUGGINGFACEHUB_ACCESS_TOKEN is not set")

llm = HuggingFaceEndpoint(
    repo_id= "Qwen/Qwen2.5-7B-Instruct",
    task='text-generation',
    temperature=0.2,
    huggingfacehub_api_token= api_key,
    max_new_tokens=512
)
model = ChatHuggingFace(llm= llm)

# --------------------------------------------------
# Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Chat With Webpage API",
    description="Backend for chatting with the current webpage",
    version="1.0.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Request model
# --------------------------------------------------

class QuestionRequest(BaseModel):
    page_text: str
    question: str

parser = PydanticOutputParser(pydantic_object= QuestionRequest)
# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Chat With Webpage backend is running"
    }


# --------------------------------------------------
# Ask question
# --------------------------------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        page_text = request.page_text
        question = request.question

        prompt = f"""
    You are an AI assistant that answers questions about a webpage.

    Use ONLY the information provided in the webpage content.

    If the answer cannot be found in the webpage,
    say that the information is not available on the page.

    WEBPAGE CONTENT:
    ----------------
    {page_text}
    ----------------

    USER QUESTION:
    {question}

    Give a clear and concise answer.
    """
        response = model.invoke(prompt)

        return {
            "answer": response.content
        }

    except Exception as e :
        print("Error:",repr(e))

        return {
            'error':str(e)
        }