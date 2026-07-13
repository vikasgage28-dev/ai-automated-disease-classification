from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pipeline import classify_symptoms

app = FastAPI(title="Disease Classification API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SymptomRequest(BaseModel):
    symptoms: str

class DiseaseResult(BaseModel):
    disease: str
    confidence: float

class ClassificationResponse(BaseModel):
    results: list[DiseaseResult]


@app.post("/classify", response_model=ClassificationResponse)
def classify(request: SymptomRequest):
    raw_results = classify_symptoms(request.symptoms)
    results = [
        DiseaseResult(disease=d, confidence=round(s, 4))
        for d, s in raw_results
    ]
    return ClassificationResponse(results=results)


@app.get("/health")
def health():
    return {"status": "ok"}