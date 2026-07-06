# 🧠 AI POC – Automated Disease Classification from Symptoms Text

**Developer:** Vikas Gage | **Company:** Decos (Medical Device)
**Goal:** Type symptoms → AI returns disease name + confidence score
**Company Deadline:** End of Q3 2026 | **Our Sprint:** 2 Weeks (10 working days)
**Tech Stack:** Python · HuggingFace Transformers · Gradio · Kaggle · GitHub

> 💡 **North Star:** At the end of Week 2, you must be able to DEMO the app
> AND confidently answer any question from the audience — technical or non-technical.

---

## 🗺️ High-Level Roadmap

```
WEEK 1 — UNDERSTAND & BUILD CORE        WEEK 2 — COMPLETE & PRESENT
─────────────────────────────────        ──────────────────────────────────────
Day 1 → Setup + Tools                    Day 6  → Full Pipeline + Accuracy Metrics
Day 2 → AI/ML/NLP Concepts (Deep)        Day 7  → Gradio UI Part 1 (Basic)
Day 3 → HuggingFace + First Model        Day 8  → Gradio UI Part 2 (Polished)
Day 4 → Dataset + Data Understanding     Day 9  → Testing + Limitations Documented
Day 5 → Classification Pipeline Pt.1     Day 10 → Demo Rehearsal + Q&A Preparation
```

---

## 🗓️ 2-Week Sprint — Master Table

### ── WEEK 1: Foundation & Core AI ──

| Day | Theme | Build Goal | Learn Goal (for Q&A) | Status |
|-----|-------|-----------|----------------------|--------|
| 1 | ⚙️ Setup | Python env, packages, `requirements.txt` | What is Python? Why not C#? | 🔄 In Progress |
| 2 | 🧠 Concepts | Personal concept cheat-sheet | AI vs ML vs DL vs NLP — explain each | ⏳ Pending |
| 3 | 🤗 First Model | `hello_ai.py` prints a real classification | What is HuggingFace? What is a model? | ⏳ Pending |
| 4 | 📊 Dataset | Dataset downloaded + explored | Where does training data come from? | ⏳ Pending |
| 5 | 🔧 Pipeline Pt.1 | Symptoms text → tokenized → model input | What is tokenization? | ⏳ Pending |

### ── WEEK 2: Build, Polish & Present ──

| Day | Theme | Build Goal | Learn Goal (for Q&A) | Status |
|-----|-------|-----------|----------------------|--------|
| 6 | 🔧 Pipeline Pt.2 | Full output: disease + confidence score + accuracy | What is confidence? How accurate is it? | ⏳ Pending |
| 7 | 🖥️ UI Part 1 | `app.py` running in browser via Gradio | What is Gradio? Why not a React app? | ⏳ Pending |
| 8 | 🎨 UI Part 2 | Top 3 diseases, confidence bar, clean design | How would this go to production? | ⏳ Pending |
| 9 | 🧪 Testing | 20+ test cases logged, limitations documented | What can it NOT do? What are the risks? | ⏳ Pending |
| 10 | 🎤 Demo Day | Clean GitHub push + dry run rehearsed | Full Q&A prep (all audience types) | ⏳ Pending |

---

## 📁 Target File Structure

```
ai-automated-disease-classification/
│
├── Progress.md                  ← Roadmap + Q&A prep (this file)
├── README.md                    ← Project overview (Day 10)
├── requirements.txt             ← Python packages (Day 1)
│
├── src/
│   ├── hello_ai.py              ← First model test (Day 3)
│   ├── pipeline.py              ← Core classification logic (Day 5–6)
│   └── app.py                   ← Gradio UI (Day 7–8)
│
├── data/
│   └── symptoms_dataset.csv     ← From Kaggle (Day 4)
│
└── tests/
    └── test_symptoms.py         ← 20+ test cases (Day 9)
```

---

## 🎤 Demo Q&A Preparation Bank

> These are real questions a Decos audience WILL ask. We build answers to each of
> these as part of the sprint — so you are never caught off guard.

### 👔 Management / Non-Technical Questions

| # | Question | Answer (built during sprint) |
|---|----------|------------------------------|
| M1 | What problem does this solve? | *(Day 2 — filled in)* |
| M2 | How long did this take to build? | *(Day 10 — filled in)* |
| M3 | Can we use this in a real product? | *(Day 9 — filled in)* |
| M4 | What would it cost to run in production? | *(Day 10 — filled in)* |
| M5 | Is patient data safe? GDPR? | *(Day 9 — filled in)* |
| M6 | Can it replace a doctor? | *(Day 2 — filled in)* |

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
| T3 | What is HuggingFace? | *(Day 3 — filled in)* |
| T4 | What is a confidence score? How is it calculated? | *(Day 6 — filled in)* |
| T5 | How would we integrate this with our .NET backend? | *(Day 8 — filled in)* |
| T6 | Can this be deployed to Azure? | *(Day 10 — filled in)* |
| T7 | How does it scale? What if 1000 users hit it? | *(Day 10 — filled in)* |
| T8 | Why Python and not C#? | *(Day 1 — filled in)* |
| T9 | What is tokenization? | *(Day 5 — filled in)* |
| T10 | What is the difference between AI, ML, and NLP? | *(Day 2 — filled in)* |

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

### Day 1 — ⚙️ Environment Setup
**Theme:** Get the machine ready to do AI work
**Q&A Answers Built:** T8 — *"Why Python and not C#?"*

#### 📖 LEARN
- What is Python? How is it different from C#?
- What is a virtual environment? *(C# analogy: isolated NuGet per project)*
- What is `pip`? *(C# analogy: NuGet CLI)*
- What is `requirements.txt`? *(C# analogy: `.csproj` PackageReference list)*
- Why do AI developers use Python? (ecosystem, libraries, community)

#### 🧠 UNDERSTAND
- Why can't we just use C# for this POC? *(AI library availability)*
- What packages will we install and what does each one do?
  - `transformers` — HuggingFace AI models library
  - `torch` — Math engine that powers the models (PyTorch)
  - `gradio` — Quick UI framework for AI demos
  - `pandas` — Data manipulation (like LINQ + DataTable combined)
  - `scikit-learn` — Accuracy metrics and evaluation tools
- Q&A answer: *"Why Python?"* ← write your own answer here after the session

#### 💻 IMPLEMENT
- [ ] Verify Python is installed (`python --version`)
- [ ] Create virtual environment (`python -m venv venv`)
- [ ] Activate it (`venv\Scripts\activate`)
- [ ] Install all packages (`pip install ...`)
- [ ] Generate `requirements.txt` (`pip freeze > requirements.txt`)
- [ ] Commit and push to GitHub
- [ ] VS Code Python extension configured and pointing to venv

#### ✅ Checklist
- [x] GitHub repo created
- [x] Repo cloned locally
- [x] `Progress.md` created
- [ ] Python verified
- [ ] Virtual env created and activated
- [ ] All packages installed
- [ ] `requirements.txt` pushed to GitHub

---

### Day 2 — 🧠 AI / ML / NLP Core Concepts
**Theme:** Build the vocabulary to talk about AI confidently
**Q&A Answers Built:** M1, M6, T10 — *"What is AI/ML/NLP?", "Can it replace a doctor?"*

#### 📖 LEARN
- What is Artificial Intelligence? *(broad umbrella)*
- What is Machine Learning? *(AI that learns from data)*
- What is Deep Learning? *(ML using neural networks)*
- What is NLP — Natural Language Processing? *(AI that understands text)*
- What is a Classification problem? *(input → one of N categories)*
- What is a pre-trained model?

#### 🧠 UNDERSTAND
- AI vs ML vs DL vs NLP — how they nest inside each other
- Why is NLP the right tool for symptoms-to-disease?
- What does "the model learned from data" actually mean?
- What is a label? What is a feature? *(C# analogy: label = return type, feature = method parameter)*
- Q&A answers to fill: M1, M6, T10

#### 💻 IMPLEMENT
- [ ] Draw the AI/ML/NLP hierarchy diagram (in your notes)
- [ ] Write a plain-English explanation of how our POC works end-to-end
- [ ] Update Q&A bank with answers for M1, M6, T10

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
- [ ] Create HuggingFace account at huggingface.co
- [ ] Create `src/hello_ai.py`
- [ ] Load the model using HuggingFace pipeline
- [ ] Run: input `"I have fever and headache"` → see disease output
- [ ] Commit `hello_ai.py` to GitHub

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

### Day 5 — 🔧 Classification Pipeline Part 1
**Theme:** Connect symptoms text to the AI model input
**Q&A Answers Built:** T9 — *"What is tokenization?"*

#### 📖 LEARN
- What is a pipeline in AI? *(C# analogy: middleware chain / CQRS handler chain)*
- What is tokenization? *(breaking text into pieces the model understands)*
- What is text preprocessing? (lowercase, remove punctuation, etc.)
- What goes IN to a model? (not raw text — numbers called tokens)

#### 🧠 UNDERSTAND
- Step by step: raw text → cleaned → tokenized → model-ready input
- Why can't we just send "fever, headache" directly to the model?
- What is a token ID vs a word?
- Q&A answer to fill: T9

#### 💻 IMPLEMENT
- [ ] Create `src/pipeline.py` (Part 1)
- [ ] Function: takes symptoms string → cleans it → tokenizes it
- [ ] Print token output so you can see what the model actually receives
- [ ] Commit to GitHub

---

### Day 6 — 🔧 Pipeline Part 2 + Accuracy Metrics
**Theme:** Get the full result and measure how good it is
**Q&A Answers Built:** C1, C3, T4, A3, A4 — *"How accurate? Confidence score? Top 3?"*

#### 📖 LEARN
- What is model inference? *(running the model to get a prediction)*
- What is a confidence score / probability? *(how sure the model is)*
- What is model accuracy? *(% of correct predictions)*
- What is F1 Score? Why not just use accuracy? *(important for medical data)*

#### 🧠 UNDERSTAND
- How does the model output a confidence score?
- What does 92% confidence actually mean mathematically?
- Why show top 3 diseases instead of just one?
- What metrics matter for a medical classification tool?
- Q&A answers to fill: C1, C3, T4, A3, A4

#### 💻 IMPLEMENT
- [ ] Complete `src/pipeline.py` (Part 2)
- [ ] Output: top 3 diseases with confidence scores
- [ ] Run against 10 test symptom inputs
- [ ] Print accuracy metrics (if using the dataset for evaluation)
- [ ] Commit to GitHub

---

### Day 7 — 🖥️ Gradio UI Part 1 (Basic)
**Theme:** Give the AI a face — a real browser-based UI
**Q&A Answers Built:** T7 (partial) — *"Why Gradio and not a React app?"*

#### 📖 LEARN
- What is Gradio? *(C# analogy: Blazor quick demo — UI with almost no frontend code)*
- What is a web server in Python context?
- How does Gradio connect the UI to your Python function?

#### 🧠 UNDERSTAND
- Why Gradio for a POC instead of React/Angular?
- What are Gradio's limitations? *(not production-grade)*
- How would this become a real product? *(REST API + React frontend + .NET backend)*
- Q&A answer to fill: T7 (partial), A1 (architecture diagram sketch)

#### 💻 IMPLEMENT
- [ ] Create `src/app.py`
- [ ] Text input box + Submit button + Output text area
- [ ] Wire it to `pipeline.py` classification function
- [ ] Run `python src/app.py` → open browser → test it
- [ ] Commit to GitHub

---

### Day 8 — 🎨 Gradio UI Part 2 (Demo-Ready Polish)
**Theme:** Make the UI look good enough for a company demo
**Q&A Answers Built:** M3, T5, T6, A1 — *"Production? Azure? .NET integration? Architecture?"*

#### 📖 LEARN
- What UI components does Gradio offer? (sliders, dropdowns, tables, labels)
- What makes a demo UI look professional?
- What is a confidence bar / progress bar in UI terms?

#### 🧠 UNDERSTAND
- How would we integrate this with a .NET REST API? *(HTTP call from C# to Python FastAPI)*
- How would we deploy this to Azure? *(Azure Container Instance / App Service)*
- Draw the production architecture: .NET API → Python Model Service → Response
- Q&A answers to fill: M3, T5, T6, A1

#### 💻 IMPLEMENT
- [ ] Show top 3 diseases with confidence percentages
- [ ] Add confidence progress bars
- [ ] Add example symptom inputs (clickable)
- [ ] Add app title, description, disclaimer text
- [ ] Test the full UI end to end
- [ ] Commit polished `app.py` to GitHub

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
