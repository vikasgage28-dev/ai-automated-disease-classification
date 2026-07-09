# 🧠 AI POC – Automated Disease Classification from Symptoms Text

**Developer:** Vikas Gage | **Company:** Decos (Medical Device)
**Goal:** Type symptoms → AI returns disease name + confidence score
**Company Deadline:** End of Q3 2026 | **Our Sprint:** 2 Weeks (10 working days)
**Tech Stack:** Python · FastAPI · HuggingFace Transformers · PyTorch · React 19 · Vite · Tailwind CSS · Kaggle · GitHub

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
| 4 | 📊 Dataset | Dataset downloaded + explored | Where does training data come from? | ⏳ Pending |
| 5 | 🔧 AI Pipeline | Full pipeline: symptoms → model → disease + confidence | What is tokenization? How does inference work? | ⏳ Pending |

### ── WEEK 2: Full Stack Build & Demo ──

| Day | Theme | Build Goal | Learn Goal (for Q&A) | Status |
|-----|-------|-----------|----------------------|--------|
| 6 | 🌐 FastAPI | Python REST API — `/classify` endpoint live | What is FastAPI? How does React talk to Python? | ⏳ Pending |
| 7 | ⚛️ React Part 1 | React components + wired to FastAPI + data displayed | What is React? What is a component? | ⏳ Pending |
| 8 | 🎨 React Part 2 | Tailwind CSS — responsive cards, confidence bars, polish | How would this go to production? | ⏳ Pending |
| 9 | 🧪 Testing | Full integration tests + edge cases + limitations docs | What can it NOT do? What are the risks? | ⏳ Pending |
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
| M2 | How long did this take to build? | *(Day 10 — filled in)* |
| M3 | Can we use this in a real product? | *(Day 9 — filled in)* |
| M4 | What would it cost to run in production? | *(Day 10 — filled in)* |
| M5 | Is patient data safe? GDPR? | *(Day 9 — filled in)* |
| M6 | Can it replace a doctor? | No — and we are very clear about that. This is a decision-support tool, not a diagnostic tool. It surfaces possibilities for a clinician to consider — like a spell-checker helps a writer but never replaces them. Every result shows a disclaimer: "Always consult a qualified medical professional." |

### 🔬 Medical / Clinical Questions

| # | Question | Answer (built during sprint) |
|---|----------|------------------------------|
| C1 | How accurate is it? | *(Day 6 — filled in with real metrics)* |
| C2 | What diseases can it classify? | *(Day 4 — filled in)* |
| C3 | What if symptoms match multiple diseases? | *(Day 6 — filled in, shows top 3)* |
| C4 | What happens with rare or unknown symptoms? | *(Day 9 — filled in)* |
| C5 | Was it trained on real medical data? | *(Day 4 — filled in)* |
| C6 | What are the risks if it gets it wrong? | *(Day 9 — filled in)* |

### 💻 Technical / Developer Questions

| # | Question | Answer (built during sprint) |
|---|----------|------------------------------|
| T1 | What AI model is being used? Why that one? | *(Day 3 — filled in)* |
| T2 | Did you train the model yourself? | *(Day 3 — filled in)* |
| T3 | What is HuggingFace? | HuggingFace is the GitHub + NuGet of the AI world — a platform with 500,000+ free pre-trained models. We use their Python library to load a model in 3 lines of code. No training required — just download and use. |
| T4 | What is a confidence score? How is it calculated? | *(Day 6 — filled in)* |
| T5 | How would we integrate this with our .NET backend? | *(Day 8 — filled in)* |
| T6 | Can this be deployed to Azure? | *(Day 10 — filled in)* |
| T7 | How does it scale? What if 1000 users hit it? | *(Day 10 — filled in)* |
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
- [ ] Create Kaggle account at kaggle.com
- [ ] Find and download the disease-symptoms dataset
- [ ] Place it in `data/symptoms_dataset.csv`
- [ ] Write a script to load and explore it with `pandas`
- [ ] Print: how many rows, how many diseases, sample rows
- [ ] Commit dataset exploration script to GitHub

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
- [ ] Create `backend/pipeline.py`
- [ ] Function: takes symptoms string → returns top 3 diseases with confidence scores
- [ ] Test with 10 different symptom inputs — print all results
- [ ] Commit to GitHub

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
- [ ] Create `backend/main.py` with FastAPI
- [ ] Define request/response models (Pydantic — C# analogy: DTOs / record types)
- [ ] Add `POST /classify` endpoint that calls `pipeline.py`
- [ ] Add CORS middleware (allow React `localhost:5173` to call it)
- [ ] Run: `uvicorn main:app --reload`
- [ ] Test in browser auto-generated Swagger UI at `/docs`
- [ ] Commit to GitHub

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
- [ ] Create `frontend/src/components/Header.jsx`
- [ ] Create `frontend/src/components/SymptomInput.jsx` — textarea + submit + loading state
- [ ] Create `frontend/src/services/api.js` — axios POST to FastAPI `/classify`
- [ ] Create `frontend/src/components/ResultCard.jsx` — one disease result
- [ ] Wire everything in `App.jsx`
- [ ] Run both: frontend (`npm run dev`) + backend (`uvicorn`) simultaneously
- [ ] End-to-end test: type symptoms → see real AI results in browser
- [ ] Commit to GitHub

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
- [ ] Create `tests/test_symptoms.py`
- [ ] Test 20+ symptom combinations
- [ ] Log: input → expected → actual → pass/fail
- [ ] Document known limitations in Progress.md
- [ ] Add disclaimer to the UI
- [ ] Commit all test results to GitHub

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

### Session 3 (Day 3)
- `backend/hello_ai.py` created and running ✅
- `facebook/bart-large-mnli` model downloaded (~1.6GB, cached locally)
- Tested with: fever/headache, chest pain, rash/joint pain, frequent urination/thirst
- Discovered: disease list must include the target disease or model cannot find it
- Internals deep-dive: Tokenization → Embeddings → NLI → Softmax
- Q&A answers filled: T1, T2, T3, A2
- **Next:** Day 4 — Kaggle dataset download + pandas data exploration
