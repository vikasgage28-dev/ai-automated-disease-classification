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
User types:   "chest pain and shortness of breath"

AI returns:
  🥇 Heart attack       84%  █████████████████
  🥈 Pneumonia           7%  █
  🥉 Bronchial Asthma    6%  █

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
  ├─ Sentence-Transformers model: BioBERT (medical)
  ├─ Converts symptoms text → 768-dimensional meaning vector
  ├─ Compares against 41 pre-computed disease vectors (cosine similarity)
  ├─ Converts similarities into probabilities across all 41 diseases (softmax)
  └─ Returns top 3 by probability
       │
       ▼
 Kaggle Dataset (4,920 cases · 41 diseases · 17 symptom columns)
```

**Key point:** No keyword rules. No if/else matching. The AI understands the *meaning* of your text using embeddings — the same technology behind Google Search and ChatGPT. The dataset's clinical symptom names are enriched with plain-English descriptions (e.g. "polyuria (frequent urination)") so the disease profiles read like everyday language.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| AI Model | `pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb` | Medical semantic symptom understanding |
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
- ~1GB disk space (AI model downloads on first run)

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

> ⏳ **First run only:** The BioBERT model (~430MB) downloads automatically into `backend/models_cache/`. Takes 5-10 minutes. After that, it loads from disk in seconds.

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
    { "disease": "Heart attack",     "confidence": 0.8445, "similarity": 0.8472 },
    { "disease": "Pneumonia",        "confidence": 0.0724, "similarity": 0.7243 },
    { "disease": "Bronchial Asthma", "confidence": 0.0599, "similarity": 0.7149 }
  ]
}
```
- `confidence` — probability across all 41 diseases (all 41 add up to 1.0)
- `similarity` — raw cosine similarity between the input and the disease profile (0 to 1)

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

The raw similarity scores are then converted into **probabilities** that add up to 100% across all 41 diseases. A clear winner stands out (e.g. Heart attack 84%, Pneumonia 7%), and when the top two are close the UI shows a hint to add more symptoms.

---

## 📊 Accuracy

Measured with `backend/evaluate.py` against 85 plain-English test cases (`backend/data/eval_cases.csv`, 2+ cases per disease):

| Metric | Result |
|--------|--------|
| Top-1 accuracy (correct disease ranked #1) | **87.1%** (74/85) |
| Top-3 accuracy (correct disease in top 3) | **95.3%** (81/85) |

Run it yourself:
```bash
cd backend
venv\Scripts\activate
python evaluate.py
```

---

## ⚠️ Known Limitations

| Limitation | Detail |
|-----------|--------|
| **Not a medical device** | Results are indicative only — not a clinical diagnosis |
| **41 diseases only** | Dataset covers common diseases; rare conditions not included |
| **No personalisation** | Does not consider age, gender, or medical history |
| **Common symptoms** | Fever + headache appear in many diseases — results may be ambiguous |
| **Single-symptom input** | One vague symptom (e.g. "fever") gives unreliable results |
| **Overlapping profiles** | Diseases with similar symptom lists (e.g. Hepatitis D vs Jaundice) can swap places |
| **Gibberish input** | Nonsense text above the 0.1 similarity cut-off still returns results |
| **English only** | Model performs best with English symptom descriptions |

---

## 🗺️ Production Roadmap (Next Steps)

If this POC is approved, the production version would include:

1. **Fine-tuned medical model** — Fine-tune the BioBERT model on a richer clinical dataset (e.g. DDXPlus, SNOMED CT) for higher accuracy
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
│   ├── pipeline.py              ← AI engine (BioBERT similarity + softmax)
│   ├── main.py                  ← FastAPI REST API
│   ├── evaluate.py              ← Accuracy test harness (Top-1 / Top-3)
│   ├── requirements.txt         ← Python dependencies
│   └── data/
│       ├── symptoms_dataset.csv ← Kaggle dataset (41 diseases)
│       └── eval_cases.csv       ← 85 plain-English test cases
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
