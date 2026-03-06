from fastapi import FastAPI
from fastapi.middleware.cors import CORSMMiddleware
app = FatAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from ai_engine import generate_question, evaluate_answer

domain = "Data Structures"
level = "Beginner"

question = generate_question(domain, level)
print("QUESTION:")
print(question)

user_answer = input("Your Answer: ")

feedback = evaluate_answer(question, user_answer)

print("\nFEEDBACK:")
print(feedback)