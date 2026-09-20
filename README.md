# 🧠 AI Automated Disease Classification — POC

**Developer:** Vikas Gage &nbsp;|&nbsp; **Company:** Decos (Medical Device Division)  
**Sprint:** 2 weeks &nbsp;|&nbsp; **Status:** ✅ POC Complete

> **In plain English:** Type your symptoms into a browser. The AI reads them, understands the meaning, and returns the top 3 most likely conditions with a confidence score — all running locally on your machine, no cloud, no data sent anywhere.

---

## 🎯 What This POC Proves

| Question | Answer |
|----------|--------|
| Can AI classify disease from free-text symptoms? | ✅ Yes |
| Does it understand natural language (not just medical terms)? | ✅ Yes — "throwing up" = "vomiting" |
| Does it run 100% locally (GDPR compliant)? | ✅ Yes — no internet connection needed after setup |
| Can a .NET developer build a Python AI stack in 2 weeks? | ✅ Yes |

---

## 🖥️ Live Demo — What It Looks Like

```
User types:   "I feel very hot, my head hurts and body aches"

AI returns:
  🥇 Chicken pox      65%  ████████████████████
  🥈 Malaria          64%  ███████████████████
  🥉 Dengue           61%  ██████████████████

  ⚠️ Medical Disclaimer: For demonstration only. Consult a doctor.
```

---

## 🏗️ Architecture

```
 Browser (React UI)
       │  user types symptoms
       ▼
 FastAPI (Python REST API)   ← POST /classify
       │
       ▼
 AI Pipeline (pipeline.py)
  ├─ Sentence-Transformers model: all-MiniLM-L6-v2
  ├─ Converts symptoms text → 384-dimensional meaning vector
  ├─ Compares against 41 pre-computed disease vectors
  └─ Returns top 3 by cosine similarity score
       │
       ▼
 Kaggle Dataset (4,920 cases · 41 diseases · 17 symptom columns)
```

**Key point:** No keyword rules. No if/else matching. The AI understands the *meaning* of your text using embeddings — the same technology behind Google Search and ChatGPT.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| AI Model | `sentence-transformers/all-MiniLM-L6-v2` | Semantic symptom understanding |
| AI Framework | HuggingFace + PyTorch | Model loading and inference |
| Backend API | Python 3.13 + FastAPI | REST endpoint `/classify` |
| Frontend | React 19 + TypeScript + Tailwind CSS | User interface |
| Dataset | Kaggle — Disease Symptom Dataset | 41 diseases, 4,920 cases |
| Build Tool | Vite | Frontend dev server |

---

## ⚡ Quick Start — Run Locally

### Prerequisites
- Python 3.10+ installed
- Node.js 18+ installed
- ~500MB disk space (AI model downloads on first run)

### Step 1 — Clone the repository
```bash
git clone https://github.com/<your-username>/ai-automated-disease-classification.git
cd ai-automated-disease-classification
```

### Step 2 — Start the AI Backend
```bash
cd backend
python -m venv venv

# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

> ⏳ **First run only:** The AI model (~90MB) downloads automatically. Takes ~1 minute. After that, startup is instant.

You should see:
```
✅ Loaded 41 diseases from dataset
✅ Semantic model ready!
✅ Embeddings ready for 41 diseases
INFO: Application startup complete.
```

### Step 3 — Start the React Frontend
Open a **second terminal**:
```bash
cd frontend
npm install
npm run dev
```

### Step 4 — Open the App
```
http://localhost:5173
```

Both terminals must stay running at the same time.

---

## 📡 API Reference

The backend exposes a REST API at `http://127.0.0.1:8000`

### `POST /classify`
**Request:**
```json
{ "symptoms": "chest pain and shortness of breath" }
```
**Response:**
```json
{
  "results": [
    { "disease": "Heart attack",  "confidence": 0.72 },
    { "disease": "Hypertension",  "confidence": 0.65 },
    { "disease": "GERD",          "confidence": 0.58 }
  ]
}
```

### `GET /health`
Returns `{ "status": "ok" }` — use this to verify the backend is running.

Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`

---

## 🧠 How the AI Works (Non-Technical)

Imagine every disease has a "fingerprint" — a list of all its known symptoms. The AI converts both the user's typed text and each disease fingerprint into a set of numbers (called an **embedding**) that represents their *meaning* in mathematical form.

Diseases with similar symptoms produce similar numbers. When a user types symptoms, the AI finds which disease fingerprint is mathematically closest — that's the top result.

This means:
- **"I feel very hot"** matches **"fever"** — because they mean the same thing
- **"throwing up"** matches **"vomiting"** — no dictionary needed
- **A typo** still works if the meaning is close enough

---

## ⚠️ Known Limitations

| Limitation | Detail |
|-----------|--------|
| **Not a medical device** | Results are indicative only — not a clinical diagnosis |
| **41 diseases only** | Dataset covers common diseases; rare conditions not included |
| **No personalisation** | Does not consider age, gender, or medical history |
| **Common symptoms** | Fever + headache appear in many diseases — results may be ambiguous |
| **English only** | Model performs best with English symptom descriptions |

---

## 🗺️ Production Roadmap (Next Steps)

If this POC is approved, the production version would include:

1. **Fine-tuned medical model** — Train BioBERT or ClinicalBERT on the dataset for higher accuracy
2. **Azure deployment** — React → Azure Static Web App, FastAPI → Azure Container App
3. **Patient history integration** — Connect to EHR system for personalised results
4. **Human review workflow** — Low-confidence results flagged for clinician review
5. **Audit logging** — Full GDPR-compliant request/response log

---

## 📁 Project Structure

```
ai-automated-disease-classification/
├── README.md                    ← You are here
├── Progress.md                  ← Full sprint log + Q&A bank
│
├── backend/
│   ├── pipeline.py              ← AI engine (semantic similarity)
│   ├── main.py                  ← FastAPI REST API
│   ├── requirements.txt         ← Python dependencies
│   └── data/
│       └── symptoms_dataset.csv ← Kaggle dataset (41 diseases)
│
└── frontend/
    ├── src/
    │   ├── App.tsx              ← Root React component
    │   ├── components/          ← Header, SymptomInput, ResultCard
    │   └── services/api.ts      ← FastAPI client
    └── package.json
```

---

## 📄 License

MIT — built as an internal POC for Decos. Not intended for clinical use.

---

*Built by Vikas Gage · Decos · 2026 · Powered by HuggingFace Sentence-Transformers*
