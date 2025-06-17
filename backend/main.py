from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Sapiora backend running"}

@app.post("/generate-content/")
async def generate_content(request: Request):
    data = await request.json()
    print("Received data:", data)
    topic = data.get("topic")
    profile = data.get("profile")

    notes = f"Here's a beginner explanation of '{topic}' for a {profile['age']} year old who learns best through {profile['style']}."
    roadmap = [
        "Understand the basics of the concept",
        "See a few practical examples",
        "Try a hands-on activity"
    ]
    quiz = [
        {
            "question": f"What is {topic} mostly used for?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        }
    ]

    return {
        "notes": notes,
        "roadmap": roadmap,
        "quiz": quiz
    }
