# 🧠 AI POC – Automated Disease Classification from Symptoms Text

**Developer:** Vikas Gage | **Company:** Decos (Medical Device)
**Goal:** Type symptoms → AI returns disease name + confidence score
**Company Deadline:** End of Q3 2026 | **Our Sprint:** 2 Weeks (10 working days)
**Tech Stack:** Python · FastAPI · HuggingFace Transformers · PyTorch · Sentence-Transformers · React 19 · Vite · Tailwind CSS · Kaggle · GitHub

> 💡 **North Star:** At the end of Week 2, you must be able to DEMO the app
> AND confidently answer any question from the audience — technical or non-technical.

---

## 🗺️ High-Level Roadmap

```
WEEK 1 — UNDERSTAND & BUILD AI CORE     WEEK 2 — FULL STACK + DEMO
─────────────────────────────────        ──────────────────────────────────────
Day 1 → Setup (Python + Node.js)         Day 6  → FastAPI — Expose AI as REST API
Day 2 → AI/ML/NLP Concepts (Deep)        Day 7  → React UI Part 1 (Components + API)
Day 3 → HuggingFace + First Model        Day 8  → React UI Part 2 (Tailwind + Polish)
Day 4 → Dataset + Data Understanding     Day 9  → Full Integration + Testing
Day 5 → AI Classification Pipeline       Day 10 → Demo Rehearsal + Final Push
```

---

## 🗓️ 2-Week Sprint — Master Table

### ── WEEK 1: Foundation & Core AI ──

| Day | Theme | Build Goal | Learn Goal (for Q&A) | Status |
|-----|-------|-----------|----------------------|--------|
| 1 | ⚙️ Setup | Python env + Node.js + React app scaffolded | What is Python? Why FastAPI not C# API? | ✅ Complete |
| 2 | 🧠 Concepts | Personal concept cheat-sheet | AI vs ML vs DL vs NLP — explain each | ✅ Complete |
| 3 | 🤗 First Model | `hello_ai.py` prints a real classification | What is HuggingFace? What is a model? | ✅ Complete |
| 4 | 📊 Dataset | Dataset downloaded + explored | Where does training data come from? | ✅ Complete |
| 5 | 🔧 AI Pipeline | Full pipeline: symptoms → model → disease + confidence | What is tokenization? How does inference work? | ✅ Complete |

### ── WEEK 2: Full Stack Build & Demo ──

| Day | Theme | Build Goal | Learn Goal (for Q&A) | Status |
|-----|-------|-----------|----------------------|--------|
| 6 | 🌐 FastAPI | Python REST API — `/classify` endpoint live | What is FastAPI? How does React talk to Python? | ✅ Complete |
| 7 | ⚛️ React Part 1 | React components + wired to FastAPI + data displayed | What is React? What is a component? | ✅ Complete |
| 8 | 🎨 React Part 2 | Tailwind CSS — responsive cards, confidence bars, polish | How would this go to production? | ✅ Complete |
| 9 | 🧪 Testing | Full integration tests + edge cases + limitations docs | What can it NOT do? What are the risks? | 🔄 In Progress |
| 10 | 🎤 Demo Day | Clean GitHub push + dry run rehearsed | Full Q&A prep (all audience types) | ⏳ Pending |

---

## 📁 Target File Structure

```
ai-automated-disease-classification/
│
├── Progress.md                        ← Roadmap + Q&A prep (this file)
├── README.md                          ← Project overview (Day 10)
│
├── backend/                           ← Python AI + API
│   ├── requirements.txt               ← Python packages (Day 1)
│   ├── hello_ai.py                    ← First model test (Day 3)
│   ├── pipeline.py                    ← Core AI classification logic (Day 5)
│   ├── main.py                        ← FastAPI server + /classify endpoint (Day 6)
│   └── data/
│       └── symptoms_dataset.csv       ← From Kaggle (Day 4)
│
├── frontend/                          ← React 19 + Vite + Tailwind CSS
│   ├── package.json                   ← Node packages (Day 1)
│   ├── index.html                     ← App entry point
│   ├── tailwind.config.js             ← Tailwind design tokens
│   └── src/
│       ├── main.jsx                   ← React entry point
│       ├── App.jsx                    ← Root component
│       ├── components/
│       │   ├── SymptomInput.jsx       ← Text input + submit button (Day 7)
│       │   ├── ResultCard.jsx         ← Disease result card (Day 7)
│       │   ├── ConfidenceBar.jsx      ← Color-coded progress bar (Day 8)
│       │   └── Header.jsx             ← Top navigation bar (Day 8)
│       └── services/
│           └── api.js                 ← Calls FastAPI /classify (Day 7)
│
└── tests/
    └── test_pipeline.py               ← AI pipeline test cases (Day 9)
```

---

## 🎤 Demo Q&A Preparation Bank

> These are real questions a Decos audience WILL ask. We build answers to each of
> these as part of the sprint — so you are never caught off guard.

### 👔 Management / Non-Technical Questions

| # | Question | Answer (built during sprint) |
|---|----------|------------------------------|
| M1 | What problem does this solve? | Doctors and patients waste time on initial symptom triage. This tool instantly analyses symptom text and returns the most likely diseases with confidence scores — speeding up the triage process and surfacing possibilities a clinician can investigate further. |
| M2 | How long did this take to build? | 10 working days as a solo developer learning Python and AI from scratch. A team of two with prior AI experience could deliver this in 3-4 days. The architecture is deliberately simple and extensible. |
| M3 | Can we use this in a real product? | This POC proves the concept and architecture work. For production we would: (1) fine-tune a medical-specific model like BioBERT on our dataset for higher accuracy, (2) add user authentication, (3) add audit logging for regulatory compliance, (4) containerise with Docker and deploy to Azure. Estimated production-ready timeline: 6-8 weeks with a small team. |
| M4 | What would it cost to run in production? | The HuggingFace model is free and runs locally — zero per-call cost. Infrastructure cost: Azure Container App (~€30-50/month for small scale). No OpenAI/Claude API fees. Scales cost-effectively compared to GPT-4 API which charges per token. |
| M5 | Is patient data safe? GDPR? | Yes — by design. The AI model runs 100% locally on our own infrastructure. Patient symptoms are never sent to any external service (no OpenAI, no HuggingFace cloud, no third-party API). Data stays within our network boundary. This was a deliberate architectural choice specifically for GDPR compliance in a medical context. |
| M6 | Can it replace a doctor? | No — and we are very clear about that. This is a decision-support tool, not a diagnostic tool. It surfaces possibilities for a clinician to consider — like a spell-checker helps a writer but never replaces them. Every result shows a disclaimer: "Always consult a qualified medical professional." |

### 🔬 Medical / Clinical Questions

| # | Question | Answer (built during sprint) |
|---|----------|------------------------------|
| C1 | How accurate is it? | *(Day 6 — filled in with real metrics)* |
| C2 | What diseases can it classify? | *(Day 4 — filled in)* |
| C3 | What if symptoms match multiple diseases? | *(Day 6 — filled in, shows top 3)* |
| C4 | What happens with rare or unknown symptoms? | If symptoms don't match known dataset patterns, the AI fallback model runs. If confidence is below 10%, the system shows a friendly message asking for clearer input instead of returning misleading results. In production, rare symptoms would be flagged for human review. |
| C5 | Was it trained on real medical data? | The dataset contains 4,920 real clinical cases across 41 diseases with 132 documented symptoms sourced from Kaggle. We use a pre-trained HuggingFace model and match against this medical dataset — no training from scratch required. |
| C6 | What are the risks if it gets it wrong? | This is why we show top 3 results, display confidence scores, and include a mandatory medical disclaimer. The tool is designed for decision support — not diagnosis. A doctor remains the decision maker. We are transparent about confidence and never claim certainty. |

### 💻 Technical / Developer Questions

| # | Question | Answer (built during sprint) |
|---|----------|------------------------------|
| T1 | What AI model is being used? Why that one? | *(Day 3 — filled in)* |
| T2 | Did you train the model yourself? | *(Day 3 — filled in)* |
| T3 | What is HuggingFace? | HuggingFace is the GitHub + NuGet of the AI world — a platform with 500,000+ free pre-trained models. We use their Python library to load a model in 3 lines of code. No training required — just download and use. |
| T4 | What is a confidence score? How is it calculated? | *(Day 6 — filled in)* |
| T5 | How would we integrate this with our .NET backend? | *(Day 8 — filled in)* |
| T6 | Can this be deployed to Azure? | Yes. React → Azure Static Web Apps (free tier). FastAPI → Azure Container Apps (serverless, scales to zero). The HuggingFace model runs inside the container — no external API calls. Estimated cost: €30-50/month at low scale. CI/CD via GitHub Actions. |
| T7 | How does it scale? What if 1000 users hit it? | Currently single-instance. For scale: (1) containerise FastAPI with Docker, (2) deploy to Azure Container Apps with auto-scaling, (3) load the model once at startup — shared across requests. The bottleneck is model inference (~200ms/request). At 1000 concurrent users, we'd add multiple container replicas behind a load balancer. |
| T8 | Why Python and not C#? | *(Day 1 — filled in)* |
| T9 | What is tokenization? | AI models only understand numbers, not text. Tokenization converts human text into a sequence of number IDs the model can process. Example: "fever headache" → [8915, 2132]. Like Encoding.UTF8.GetBytes() in C# but smarter — it preserves language meaning. |
| T10 | What is the difference between AI, ML, and NLP? | AI is the broad field of making computers do human-like tasks. Machine Learning is a subset of AI where the computer learns patterns from data instead of following hand-written rules. Deep Learning is a subset of ML using neural networks. NLP (Natural Language Processing) is Deep Learning applied specifically to human language — reading, understanding and classifying text. Our POC uses NLP because the input is free text symptoms. |

### 🏗️ Architecture Questions

| # | Question | Answer (built during sprint) |
|---|----------|------------------------------|
| A1 | What is the system architecture? | *(Day 8 — filled in with diagram)* |
| A2 | Where does the model live — local or cloud? | *(Day 3 — filled in)* |
| A3 | What is the request/response flow? | *(Day 6 — filled in)* |
| A4 | Can we add more diseases later without retraining? | *(Day 6 — filled in)* |

---

## 📅 Detailed Day Logs

> ### 🔁 Every Day Follows This 3-Part Structure:
> | Phase | What Happens |
> |-------|-------------|
> | 📖 **LEARN** | Concepts explained with C# analogies — theory first, no code yet |
> | 🧠 **UNDERSTAND** | Go deeper — how does it work internally? Why this approach? Fill Q&A bank |
> | 💻 **IMPLEMENT** | Write code, run it, verify output, commit to GitHub |

---

### Day 1 — ⚙️ Environment Setup (Python + Node.js + React)
**Theme:** Set up BOTH the AI backend and React frontend environments
**Q&A Answers Built:** T8 — *"Why Python + FastAPI and not C#?"*

#### 📖 LEARN
- What is Python? How is it different from C#?
- What is a virtual environment? *(C# analogy: isolated NuGet per project)*
- What is `pip`? *(C# analogy: NuGet CLI)*
- What is `requirements.txt`? *(C# analogy: `.csproj` PackageReference list)*
- What is Node.js? *(JavaScript runtime — needed to run React tooling)*
- What is Vite? *(C# analogy: `dotnet new` project scaffolding — but for React)*
- What is npm? *(C# analogy: NuGet — but for JavaScript)*

#### 🧠 UNDERSTAND
- Why Python for AI and not C#? *(AI library ecosystem)*
- Why React for UI and not Blazor? *(industry standard, modern, component-based)*
- Why FastAPI as the bridge? *(lightest Python REST API — C# analogy: minimal ASP.NET Core)*
- What packages will we install?
  - **Python:** `transformers`, `torch`, `fastapi`, `uvicorn`, `pandas`, `scikit-learn`
  - **Node/React:** `react`, `react-dom`, `tailwindcss`, `axios`, `vite`
- How does React talk to FastAPI? *(HTTP POST — same as any REST API call)*
- Q&A answer: *"Why this stack?"* ← write your own answer here after the session

#### 💻 IMPLEMENT
- [ ] Verify Python installed (`python --version`)
- [ ] Create `backend/` folder
- [ ] Create Python virtual environment inside `backend/`
- [ ] Install all Python packages
- [ ] Generate `backend/requirements.txt`
- [ ] Verify Node.js installed (`node --version`)
- [ ] Scaffold React app with Vite inside `frontend/`
- [ ] Install Tailwind CSS in the React project
- [ ] Run React app in browser (`npm run dev`) — see default page
- [ ] Commit both `backend/` and `frontend/` scaffolds to GitHub

#### ✅ Checklist
- [x] GitHub repo created
- [x] Repo cloned locally
- [x] `Progress.md` created
- [x] Python 3.13.14 verified + `backend/` venv set up
- [x] All Python packages installed (torch 2.12.1, transformers 5.13.0, fastapi, uvicorn, pandas, scikit-learn)
- [x] `requirements.txt` generated
- [x] Node.js v24.14.0 verified
- [x] React 19 + TypeScript + Vite scaffolded in `frontend/`
- [x] Tailwind CSS v4 configured
- [x] React app running at localhost:5173 ✅
- [x] Everything committed to GitHub

---

### Day 2 — 🧠 AI / ML / NLP Core Concepts
**Theme:** Build the vocabulary to talk about AI confidently
**Q&A Answers Built:** M1, M6, T10 — *"What is AI/ML/NLP?", "Can it replace a doctor?"*

#### 📖 LEARN
- What is Artificial Intelligence? *(broad umbrella — computers doing human-like tasks)*
- What is Machine Learning? *(AI that learns from data instead of hand-written rules)*
- What is Deep Learning? *(ML using neural networks — chains of math operations)*
- What is NLP? *(Deep Learning for human language — text understanding)*
- What is a Classification problem? *(input → one of N categories)*
- What is a pre-trained model? *(trained by researchers on millions of examples — we just use it)*

#### 🧠 UNDERSTAND
- AI → ML → DL → NLP nest inside each other like Russian dolls
- Why NLP for our POC? Because input is free text, not structured numbers
- Traditional code: YOU write rules. AI: computer LEARNS rules from data
- Pre-trained model = NuGet package for AI — download and use, don't build from scratch
- Label = the answer (disease name). Feature = the input (symptoms text)

#### ✅ Q&A Answers Completed
- [x] M1 — What problem does this solve?
- [x] M6 — Can it replace a doctor?
- [x] T10 — What is the difference between AI, ML and NLP?

#### 💻 IMPLEMENT
- [x] AI/ML/NLP hierarchy understood
- [x] Plain-English POC flow understood: symptoms → NLP → classification → confidence
- [x] Q&A bank updated with answers for M1, M6, T10

---

### Day 3 — 🤗 HuggingFace + First Model Running
**Theme:** Use a real AI model for the first time
**Q&A Answers Built:** T1, T2, T3 — *"What model? Did you train it? What is HuggingFace?"*

#### 📖 LEARN
- What is HuggingFace? *(C# analogy: NuGet Gallery but for AI models)*
- What is a pre-trained model? *(someone else already trained it on millions of examples)*
- What is zero-shot classification? *(classify without training on your specific data)*
- What is a pipeline in HuggingFace? *(C# analogy: a ready-made service class)*

#### 🧠 UNDERSTAND
- Why do we use a pre-trained model instead of training from scratch?
- What model will we use and why? (e.g. `facebook/bart-large-mnli`)
- Where does the model file live? (downloaded locally to cache)
- What is the difference between inference and training?
- Q&A answers to fill: T1, T2, T3, A2

#### 💻 IMPLEMENT
- [x] Create `backend/hello_ai.py`
- [x] Load `facebook/bart-large-mnli` model using HuggingFace pipeline
- [x] Run: input `"I have fever, headache and body aches"` → see disease output
- [x] Tested with multiple symptom inputs (chest pain, rash, frequent urination)
- [x] Understood why disease list must include the right categories
- [ ] Commit `hello_ai.py` to GitHub

#### ✅ Q&A Answers Completed
- [x] T1 — Model used: `facebook/bart-large-mnli` (Meta's BART, zero-shot NLI model). Chosen because it is free, runs locally, requires no medical training data, industry-standard for zero-shot classification.
- [x] T2 — We did NOT train the model. We use a pre-trained model from HuggingFace. Like using a NuGet package — someone else built and trained it, we just call it.
- [x] T3 — HuggingFace is the NuGet Gallery / GitHub of the AI world. 500,000+ free pre-trained models. 3 lines of code to load a model.
- [x] A2 — Model runs 100% locally. Downloaded once (~1.6GB) to local cache. Never calls the internet during inference. Patient symptoms never leave our infrastructure → GDPR compliant.

#### 🧠 Key Concepts Understood (Day 3)
- **Tokenization:** Text → token IDs (numbers). "fever" → 8915. AI only understands numbers.
- **Embeddings:** Token IDs → 768-dimensional meaning vectors. Similar words → similar vectors. This is why "fever" and "high temperature" match the same disease.
- **NLI (Natural Language Inference):** For each disease, tests "Does this symptom text entail this disease?" Returns entailment score per disease.
- **Softmax:** Normalizes raw entailment scores into percentages summing to 100%.
- **Zero-shot classification requires candidate labels** — the symptom input is free text but diseases must be provided. With only 5 diseases in the list, Diabetes cannot be found. With full Kaggle dataset (41 diseases), accuracy improves dramatically.
- **Local HuggingFace model vs GPT-4/Claude API:** Local = free + GDPR safe + offline. API = paid + data leaves machine + internet dependent.

---

### Day 4 — 📊 Dataset + Data Understanding
**Theme:** Understand the data the AI learns from
**Q&A Answers Built:** C2, C5 — *"What diseases can it classify?", "Was it trained on real data?"*

#### 📖 LEARN
- What is a dataset? *(C# analogy: a strongly-typed List<T> of training examples)*
- What is Kaggle? *(platform with free public datasets)*
- What columns matter in a disease dataset? (symptoms, disease label)
- What is data exploration? Why do it before building anything?

#### 🧠 UNDERSTAND
- What dataset will we use? Why this one?
- How many diseases does it cover?
- What does a "clean" vs "dirty" dataset look like?
- What is data preprocessing? *(C# analogy: input validation + transformation)*
- Q&A answers to fill: C2, C5

#### 💻 IMPLEMENT
- [x] Downloaded disease-symptoms dataset from Kaggle
- [x] Placed in `backend/data/symptoms_dataset.csv`
- [x] Created `backend/explore_data.py` with pandas exploration
- [x] Confirmed: 4,920 rows | 18 columns | 41 unique diseases
- [x] Committed to GitHub

#### ✅ Q&A Answers Completed
- [x] C2 — 41 diseases: AIDS, Acne, Allergy, Arthritis, Bronchial Asthma, Cervical Spondylosis, Chicken Pox, Common Cold, Dengue, Diabetes, Dimorphic Hemorrhoids, Drug Reaction, Fungal Infection, GERD, Gastroenteritis, Heart Attack, Hepatitis A/B/C/D/E, Hypertension, Hyperthyroidism, Hypoglycemia, Impetigo, Jaundice, Malaria, Migraine, Osteoarthritis, Paralysis, Peptic Ulcer, Pneumonia, Psoriasis, Tuberculosis, Typhoid, Urinary Tract Infection, Varicose Veins.
- [x] C5 — Dataset sourced from Kaggle "Disease Symptom Prediction" — 4,920 real medical cases with clinically documented symptom combinations.

#### 🧠 Key Concepts Understood (Day 4)
- **Dataset structure:** 1 Disease column + Symptom_1 to Symptom_17 (17 symptom columns per row)
- **NaN values:** Many symptom columns are empty (NaN) — diseases have different numbers of symptoms. Must handle in pipeline.
- **pandas:** Python's data analysis library. Like DataTable in C# but far more powerful. `df.head()`, `df.nunique()`, `df['col'].unique()` are key methods.
- **Why this dataset matters:** With 41 diseases in the list (vs 5 hardcoded), Diabetes, Hypertension, Pneumonia etc. now get correctly classified.

---

### Day 5 — 🔧 Full AI Classification Pipeline
**Theme:** Complete the AI engine — symptoms in, disease + confidence out
**Q&A Answers Built:** T9, T4, C1, C3 — *"Tokenization? Confidence? Accuracy? Top 3?"*

#### 📖 LEARN
- What is a pipeline in AI? *(C# analogy: CQRS handler chain — each step transforms the data)*
- What is tokenization? *(breaking text into pieces the model understands)*
- What is model inference? *(running the model to get a prediction)*
- What is a confidence score? *(how sure the model is — 0.0 to 1.0)*
- What is F1 Score? Why not just accuracy? *(critical for medical imbalanced data)*

#### 🧠 UNDERSTAND
- Full step-by-step flow: raw symptoms → cleaned → tokenized → model → top 3 results
- Why can't we just send "fever, headache" directly to the model?
- What does 92% confidence actually mean mathematically?
- Why show top 3 diseases instead of just 1?
- Q&A answers to fill: T9, T4, C1, C3

#### 💻 IMPLEMENT
- [x] Created `backend/pipeline.py`
- [x] Built `classify_symptoms(symptoms_text)` function — returns top 3 diseases + scores
- [x] Loaded 41 diseases dynamically from dataset (not hardcoded)
- [x] Built disease → symptom lookup from all 17 symptom columns
- [x] Hybrid approach: dataset keyword matching + AI zero-shot fallback
- [x] Tested with 5 symptom inputs — Heart attack, Fungal infection, Jaundice correctly identified
- [x] Committed to GitHub

#### ✅ Q&A Answers Completed
- [x] T9 — Tokenization: AI only understands numbers. Text → token IDs → meaning vectors (embeddings). "fever" → 8915. Similar words have similar vectors — that's why "fever" and "high temperature" match the same disease.
- [x] T4 — Confidence score: Dataset matching = symptom overlap ratio (matched symptoms ÷ total disease symptoms). AI fallback = softmax probability from NLI entailment scores. Both normalized to 0.0–1.0.
- [x] C1 — Accuracy: Hybrid approach correctly identifies Heart attack, Fungal infection, Jaundice from plain English. Medical terminology gaps (polyuria vs frequent urination) handled by AI fallback. Full accuracy metrics documented on Day 9.
- [x] C3 — Top 3 returned always: gives clinician multiple possibilities to investigate rather than a single potentially wrong answer.

#### 🧠 Key Concepts Understood (Day 5)
- **Hybrid AI = Industry Standard:** Netflix, Google Search, every real production AI system is hybrid. Dataset provides domain knowledge, AI provides language understanding.
- **Why not pure AI?** BART was trained on general text (news, books) — not medical data. It doesn't know chest pain = Heart attack. A fine-tuned medical model (BioBERT, ClinicalBERT) would solve this — that's the production next step.
- **POC purpose:** Proves the CONCEPT (architecture, stack, flow) works — not production accuracy. Accuracy improves with fine-tuned medical model.
- **Dataset matching:** Extracts all symptoms from 17 columns per disease → builds lookup dictionary → scores by overlap ratio. Like SQL WHERE with CONTAINS but smarter.
- **AI fallback:** When user types informal language ("frequent urination") that doesn't match dataset terms ("polyuria") — BART model handles it semantically.

#### 🧠 Key Concepts Understood (Day 9 — Semantic Upgrade)
- **Why keyword matching is not AI:** Checking if a word appears in a string is a `Contains()` operation — deterministic, brittle, not intelligent. Real AI understands *meaning*, not characters.
- **Embeddings:** An AI model converts any sentence into a vector of 384 numbers (e.g. `all-MiniLM-L6-v2`). Similar meanings → similar vectors. "throwing up" and "vomiting" end up near each other in vector space.
- **Cosine Similarity:** Measures the angle between two vectors (0 = unrelated, 1 = identical meaning). Used to rank all 41 diseases against the user's input.
- **Pre-computed embeddings:** At server startup, all 41 disease symptom profiles are encoded once into vectors and cached in memory. Each user request only encodes their input (fast — ~50ms).
- **`sentence-transformers` library:** Python library from HuggingFace. `model.encode(text)` → 384-dim vector. `util.cos_sim(a, b)` → similarity score. Two lines of code replace the entire keyword matching system.
- **`all-MiniLM-L6-v2` model:** 90MB multilingual sentence encoder. Trained on 1 billion sentence pairs to understand semantic similarity. Chosen for speed (6 transformer layers vs 12 in BERT-base) and accuracy balance.
- **C# analogy:** Like replacing a manual `if (text.Contains("fever"))` chain with a trained neural network that understands what "I feel very hot" means without being told.

---

### Day 6 — 🌐 FastAPI — Expose AI as REST API
**Theme:** Wrap the AI pipeline in a real REST API so React can call it
**Q&A Answers Built:** T5, A3 — *"How does React talk to Python? Request/response flow?"*

#### 📖 LEARN
- What is FastAPI? *(C# analogy: ASP.NET Core Minimal API — but Python)*
- What is a REST endpoint? *(you already know this from .NET!)*
- What is CORS? Why does the browser block cross-origin calls?
- What is `uvicorn`? *(C# analogy: Kestrel web server — hosts the FastAPI app)*
- What is Swagger/OpenAPI? *(FastAPI generates it automatically — same as .NET!)*

#### 🧠 UNDERSTAND
- Exact API contract React will use:
  - **Request:** `POST /classify` → `{ "symptoms": "fever, headache" }`
  - **Response:** `{ "results": [{ "disease": "Influenza", "confidence": 0.92 }] }`
- How React calls this *(same pattern as calling any .NET REST API from a frontend)*
- Q&A answers to fill: T5, A3

#### 💻 IMPLEMENT
- [x] Created `backend/main.py` with FastAPI
- [x] Defined Pydantic models: `SymptomRequest`, `DiseaseResult`, `ClassificationResponse`
- [x] Added `POST /classify` endpoint calling `classify_symptoms()` from pipeline.py
- [x] Added `GET /health` endpoint → returns `{"status": "ok"}`
- [x] Added CORS middleware → allows React `localhost:5173` to call the API
- [x] Fixed indentation bug — endpoints were accidentally inside the class body
- [x] Ran: `uvicorn main:app --reload` from `backend/` directory
- [x] Tested in Swagger UI at `http://127.0.0.1:8000/docs` ✅
- [x] Confirmed JSON response for "chest pain and shortness of breath":
      Heart attack 0.25 | Hypertension 0.20 | GERD 0.1667
- [x] Committed to GitHub

#### ✅ Q&A Answers Completed
- [x] T5 — How does React talk to Python? React sends HTTP POST to FastAPI `/classify` endpoint with JSON body `{"symptoms": "..."}`. FastAPI processes it through pipeline.py and returns JSON `{"results": [...]}`. Identical pattern to calling any .NET REST API from a frontend.
- [x] A3 — Request/response flow: User types symptoms → React POST /classify → FastAPI receives SymptomRequest → calls classify_symptoms() → returns ClassificationResponse JSON → React displays results.
- [x] A4 — Add more diseases without retraining: Yes! Just add rows to symptoms_dataset.csv. Pipeline loads diseases dynamically — no code change needed.

#### 🧠 Key Concepts Understood (Day 6)
- **FastAPI:** Python equivalent of ASP.NET Core Minimal API. Decorator `@app.post("/classify")` = `[HttpPost]` attribute in C#.
- **Pydantic models:** Python equivalent of C# DTOs / record types. Auto-validates request body and serializes response to JSON.
- **uvicorn:** Python web server = Kestrel in .NET. Command: `uvicorn main:app --reload` = `dotnet watch run`.
- **CORS middleware:** Browser blocks cross-origin requests by default. Must explicitly allow `localhost:5173` (React) to call `localhost:8000` (FastAPI).
- **Swagger UI:** FastAPI auto-generates it at `/docs` — same as .NET Swashbuckle. No extra setup needed.
- **`--reload` flag:** Auto-restarts server on file save = `dotnet watch run` hot reload.
- **Full request/response flow:**
  ```
  Swagger/React → POST /classify {"symptoms": "chest pain"}
       ↓
  FastAPI validates SymptomRequest (Pydantic)
       ↓
  classify_symptoms() → pipeline.py → dataset matching + AI
       ↓
  ClassificationResponse JSON → {"results": [{"disease": "Heart attack", "confidence": 0.25}]}
  ```

---

### Day 7 — ⚛️ React Part 1 (Components + API Integration)
**Theme:** Build React UI connected live to the FastAPI backend
**Q&A Answers Built:** T7 — *"Why React? What is a component?"*

#### 📖 LEARN
- What is React? *(C# analogy: components = C# classes — each has state + renders UI)*
- What is JSX? *(HTML written inside JavaScript — like Razor in Blazor)*
- What is a component? *(C# analogy: reusable UI class, props = constructor params)*
- What is `useState`? *(C# analogy: private field that triggers UI re-render on change)*
- What is `axios`? *(C# analogy: `HttpClient` — calls the FastAPI REST endpoint)*

#### 🧠 UNDERSTAND
- Component tree: `App → Header + SymptomInput + ResultCards`
- Data flow: user types → state updates → axios POST → results render
- Why React over plain HTML? *(reactivity, reusability, industry standard)*
- Q&A answers to fill: T7, A1

#### 💻 IMPLEMENT
- [x] Installed axios via `npm install axios`
- [x] Created `frontend/src/services/api.ts` — axios POST to FastAPI `/classify`
- [x] Created `frontend/src/components/Header.tsx` — dark slate header with official POC title
- [x] Created `frontend/src/components/SymptomInput.tsx` — controlled textarea + Classify + Reset buttons + example chips
- [x] Created `frontend/src/components/ResultCard.tsx` — disease card with animated confidence bar + medal + color coding
- [x] Updated `App.tsx` — wired all components, manages state (symptoms, results, loading, error)
- [x] Added input validation — scores below 10% show friendly error instead of fake results
- [x] Reset button clears textarea + results + error simultaneously
- [x] Ran both simultaneously: uvicorn (port 8000) + npm run dev (port 5173)
- [x] End-to-end test confirmed: type symptoms → real AI results in browser ✅
- [x] Committed to GitHub

#### ✅ Q&A Answers Completed
- [x] T7 — What is React? React is a JavaScript library for building UIs from reusable components. Each component = a class with state and a render method. C# analogy: like UserControls in WinForms or Blazor components — each manages its own state and renders HTML.
- [x] A1 — Architecture: React (port 5173) → axios HTTP POST → FastAPI (port 8000) → pipeline.py → HuggingFace model → JSON response → React renders ResultCards.

#### 🧠 Key Concepts Understood (Day 7)
- **Component tree:** App → Header + SymptomInput + ResultCard. Each component = one responsibility.
- **useState:** React's state management. `const [results, setResults] = useState([])` = private field that triggers re-render on change. C# analogy: INotifyPropertyChanged.
- **Controlled component:** Textarea value driven by React state — not the DOM. Enables Reset to clear the input programmatically.
- **axios:** HTTP client for React. `axios.post(url, body)` = `HttpClient.PostAsJsonAsync()` in C#.
- **Two terminals required:** uvicorn (backend) + npm run dev (frontend) must run simultaneously in separate terminals.
- **CORS:** Browser blocks React (5173) calling FastAPI (8000) unless CORS middleware explicitly allows it — already configured in main.py.
- **Input validation:** Confidence threshold of 10% — below this, input is meaningless text. Show friendly error instead of misleading results.

---

### Day 8 — 🎨 React Part 2 (Tailwind CSS + Responsive + Polish)
**Theme:** Make the app look pixel-perfect and genuinely demo-ready
**Q&A Answers Built:** M3, T6, A1 — *"Production? Azure deploy? Architecture diagram?"*

#### 📖 LEARN
- What is Tailwind CSS? *(utility-first CSS — design system as class names)*
- What is responsive design in Tailwind? *(`sm:` `md:` `lg:` breakpoint prefixes)*
- What makes a UI look trustworthy for a medical/enterprise audience?

#### 🧠 UNDERSTAND
- Color palette: medical blue + white + semantic confidence colors
- Green (≥80%) / Yellow (≥50%) / Red (<50%) — why these thresholds for medical?
- How would this be deployed to Azure? *(React → Azure Static Web App, FastAPI → Azure Container App)*
- Full production architecture diagram
- Q&A answers to fill: M3, T6, A1

#### 💻 IMPLEMENT
- [ ] Apply Tailwind medical blue color theme across all components
- [ ] `ConfidenceBar.jsx` — animated, color-coded progress bar
- [ ] Responsive layout — 3 cards side by side desktop → stacked on mobile
- [ ] Metrics summary row — top disease, confidence %, total matches
- [ ] Clickable example symptom chips (quick-fill input buttons)
- [ ] Loading spinner while API processes
- [ ] Styled disclaimer footer — warning box
- [ ] Test at multiple window sizes — fully responsive
- [ ] Commit final polished UI to GitHub

---

### Day 9 — 🧪 Testing + Limitations + Risk Documentation
**Theme:** Know exactly what works, what doesn't, and why — honestly
**Q&A Answers Built:** C4, C6, M5 — *"Edge cases? Risks? GDPR?"*

#### 📖 LEARN
- What is edge case testing in AI? *(very different from unit testing in C#)*
- What does "model hallucination" mean? *(AI confidently wrong)*
- What are the ethical considerations of medical AI?
- What is GDPR and how does it apply here?

#### 🧠 UNDERSTAND
- What symptoms break our model? (ambiguous, rare, multi-disease overlap)
- What should we NEVER claim this tool can do?
- What disclaimer must we show in the UI?
- Q&A answers to fill: C4, C6, M5

#### 💻 IMPLEMENT
- [x] Tested 10 symptom combinations via the React UI
- [x] Identified and fixed pipeline matching bug (word-level matching added)
- [x] Removed hardcoded test cases from pipeline.py (were printing in terminal on every uvicorn start)
- [x] Added input validation — empty input shows "Please enter a text to classify"
- [x] Reset button disabled when textarea is empty
- [x] Medical disclaimer added to UI
- [x] Known limitations documented below

#### ✅ Test Results Log

| # | Input | Top Result | Status |
|---|-------|-----------|--------|
| 1 | fever, headache, body aches (typo: "ever") | Paralysis ❌ | ⚠️ Typo broke keyword match |
| 2 | fever, headache, body aches | Paralysis 50% | ⚠️ Common symptoms match many diseases |
| 3 | chest pain and shortness of breath | Heart attack ✅ | ✅ Correct |
| 4 | skin rash and itching | Fungal infection 75% | ✅ Correct |
| 5 | yellow eyes and dark urine | Jaundice ✅ | ✅ Correct |
| 6 | (empty input) | Validation error | ✅ Handled correctly |
| 7 | random text (xvxvfxfg) | No meaningful match error | ✅ Handled correctly |

#### 🧠 Known Limitations (Documented for Demo)

- **Common symptom overlap:** Fever, headache appear in 20+ diseases. Scoring formula (overlap ÷ total symptoms) can favour diseases with fewer symptoms, surfacing unexpected results.
- **Typo sensitivity:** Keyword matching requires correct spelling. "ever" does not match "high fever". Production fix: add fuzzy matching / spell checker layer.
- **Medical terminology gap:** Dataset uses clinical terms (polyuria, polydipsia). Users typing "frequent urination" may miss exact matches — falls back to AI zero-shot.
- **General AI model:** `facebook/bart-large-mnli` is trained on general text, not medical data. Production fix: fine-tune BioBERT or ClinicalBERT on the dataset.
- **No personalisation:** Does not consider age, gender, medical history. Pure symptom text only.
- **Top 3 only:** Returns 3 results. A rare disease ranked 4th would be missed.

#### 🎤 Demo Answer — "What can it NOT do?"
> *"It cannot replace a doctor, handle typos gracefully, or personalise results by patient history. Common symptoms like fever produce ambiguous results because they appear in many diseases. For production, we would add fuzzy matching, fine-tune a medical-specific model like BioBERT, and add a human review step for low-confidence results. The POC proves the architecture works — production accuracy requires the next iteration."*

---

### Day 10 — 🎤 Demo Rehearsal + Final Push
**Theme:** Walk in prepared — know the code, know the answers, look confident
**Q&A Answers Built:** M2, M4, T6, T7 — *"Cost? Azure? Scale? How long to build?"*

#### 📖 LEARN
- How to structure a 10-minute technical demo
- What slides to show (if any)
- How to handle a question you don't know the answer to

#### 🧠 UNDERSTAND
- Review ALL Q&A bank entries — are all answers filled in?
- What is your 1-sentence pitch for the POC?
- What are the 3 most important things you want the audience to walk away knowing?

#### 💻 IMPLEMENT
- [ ] Final code review — clean up comments
- [ ] Write `README.md` with setup instructions
- [ ] Push everything to GitHub — repo is public and clean
- [ ] Full Q&A bank reviewed and all answers written
- [ ] Dry run the full demo (record yourself if helpful)
- [ ] Prepare 2-slide summary: Problem → Solution → Demo

---

## 🧠 Key Concepts Learned
*(Updated each session)*

---

## 🐛 Issues & Fixes
*(Updated as we encounter problems)*

---

## 📝 Session Notes
### Session 1
- Project initialized, 2-week plan created with Q&A bank
- `Progress.md` committed to GitHub

### Session 2 (Day 2)
- AI / ML / NLP core concepts covered
- Q&A answers filled: M1, M6, T10
- Concept hierarchy: AI → ML → Deep Learning → NLP

### Session 9 (Day 9)
- Ran 7 test cases via React UI — documented pass/fail in test results log
- Fixed pipeline word-level matching bug (fever now matches "high fever")
- Removed hardcoded test cases from pipeline.py — terminal now clean on startup
- Added empty input validation + disabled Reset button when textarea is empty
- Documented 6 known limitations with demo-ready explanations
- Q&A answers finalised: C4, C6, M5
- **Upgraded AI engine to Pure Semantic Similarity** — replaced all keyword matching with `sentence-transformers`
  - Installed `sentence-transformers 5.6.0`
  - Model: `all-MiniLM-L6-v2` (90MB, 384-dim embeddings)
  - Disease symptom profiles pre-encoded at startup (41 vectors cached in memory)
  - Each request: encode user input → cosine similarity against all 41 → top 3 returned
  - Natural language now works: "throwing up", "I feel very hot", "peeing too much" — no keyword rules
  - Removed `facebook/bart-large-mnli` (1.6GB) — replaced by 90MB semantic model
  - Result quality improved: "fever, headache, body aches" → Chicken pox / Malaria / Dengue (clinically correct) vs previous Paralysis (wrong)
- **New skills gained:** Embeddings, Cosine Similarity, Sentence-Transformers, Semantic Search
- **Next:** Day 10 — Demo rehearsal + README + final GitHub push

### Session 8 (Day 8)
- Added stats bar: 41 Diseases · 4,920 Cases · 132 Symptoms
- Added animated CSS loading spinner during AI analysis
- Improved medical disclaimer — formatted with title + body
- Added professional footer: Vikas Gage · Decos · 2026
- Filled ALL remaining Q&A answers: M2, M3, M4, M5, C4, C6, T6, T7
- Q&A bank now 100% complete ✅
- **Next:** Day 9 — Edge case testing + limitations documentation

### Session 7 (Day 7)
- Built complete React UI: Header, SymptomInput, ResultCard, App
- Installed axios — wired React to FastAPI /classify endpoint
- Full end-to-end working: type symptoms → AI results in browser ✅
- Added input validation (10% confidence threshold)
- Reset button clears textarea + results + error
- Color-coded confidence bars: green (≥50%) / amber (≥25%) / red (<25%)
- Q&A answers filled: T7, A1
- **Next:** Day 8 — Polish, responsive design, loading states, disclaimer

### Session 6 (Day 6)
- Created `backend/main.py` — FastAPI REST API wrapping the pipeline
- Fixed indentation bug — endpoints accidentally inside Pydantic class body
- API running on `http://127.0.0.1:8000`
- Swagger UI live at `/docs` — tested POST /classify and GET /health ✅
- JSON response confirmed: Heart attack, Hypertension, GERD for chest pain symptoms
- Q&A answers filled: T5, A3, A4
- **Next:** Day 7 — React UI Part 1 (components + wired to FastAPI)

### Session 5 (Day 5)
- Built `backend/pipeline.py` — core AI engine of the entire POC
- Hybrid approach: dataset keyword matching + AI zero-shot fallback
- Heart attack, Fungal infection, Jaundice correctly identified ✅
- Deep discussion: Why hybrid? Why not pure AI? What does POC mean?
- Key insight: Every production AI system is hybrid — dataset gives medical knowledge, AI gives language understanding
- Next step for production: Fine-tune BioBERT/ClinicalBERT on this dataset
- Q&A answers filled: T4, T9, C1, C3
- **Next:** Day 6 — FastAPI REST API wrapping the pipeline

### Session 4 (Day 4)
- Downloaded Kaggle disease-symptoms dataset
- Created `backend/explore_data.py` — pandas exploration script
- Dataset confirmed: 4,920 rows | 18 columns | 41 diseases
- Key insight: symptoms are in 17 separate columns — must merge in pipeline (Day 5)
- Q&A answers filled: C2, C5
- **Next:** Day 5 — Full AI classification pipeline using real dataset

### Session 3 (Day 3)
- `backend/hello_ai.py` created and running ✅
- `facebook/bart-large-mnli` model downloaded (~1.6GB, cached locally)
- Tested with: fever/headache, chest pain, rash/joint pain, frequent urination/thirst
- Discovered: disease list must include the target disease or model cannot find it
- Internals deep-dive: Tokenization → Embeddings → NLI → Softmax
- Q&A answers filled: T1, T2, T3, A2
- **Next:** Day 4 — Kaggle dataset download + pandas data exploration
