from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from pydantic import BaseModel
from ai_engine import generate_question, evaluate_answer


class QuestionRequest(BaseModel):
    domain: str
    level: str


class AnswerRequest(BaseModel):
    question: str
    user_answer: str


@app.post("/generate-question")
def get_question(request: QuestionRequest):
    question = generate_question(request.domain, request.level)
    return {"question": question}


@app.post("/evaluate-answer")
def get_evaluation(request: AnswerRequest):
    feedback = evaluate_answer(request.question, request.user_answer)
    return {"feedback": feedback}