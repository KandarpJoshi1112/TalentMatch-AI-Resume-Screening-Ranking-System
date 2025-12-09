# 🤖 TalentMatch AI – Resume Screening & Ranking System

An AI-powered resume screening system that analyzes multiple **PDF resumes** against a **Job Description**, ranks candidates based on **text similarity** and **skill match**, and provides detailed insights for each resume.
Designed for **recruiters, hiring teams, and job seekers** to quickly identify best-fit candidates.

🟢 Live Demo: https://talentmatch-ai-resume-screening-ranking-system.streamlit.app/
---

## 🚀 Features

| Feature                         | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| 📥 Upload multiple resumes      | Drag-drop UI for PDF documents                  |
| 📝 Paste or use sample JD       | Flexible job role evaluation                    |
| 🤖 TF-IDF similarity ranking    | Matches resume content to JD description        |
| 🧠 Skill-based coverage scoring | Measures how well skills align with the role    |
| 🏆 Highlighted Top Match        | Easily identify best candidate                  |
| 📊 Detailed scoring table       | Similarity %, Skill coverage %, Final relevance |
| 📤 CSV Export                   | Download results for hiring workflow            |
| 🎨 Modern UI                    | Streamlit-powered interactive interface         |

---

## 🔎 How TalentMatch AI Scores Resumes

Each resume receives a **final weighted match score**:

```
match_score = 0.8 * similarity_score + 0.2 * skill_coverage_score
```

✔ Similarity Score → TF-IDF + Cosine Similarity
✔ Skill Coverage → Only counts skills present in BOTH resume & JD
✔ Score Range → 0–100 for clear evaluation

---

## 🧠 Tech Stack

| Layer                | Technology                 |
| -------------------- | -------------------------- |
| Frontend UI          | Streamlit                  |
| NLP & Matching       | TF-IDF + Cosine Similarity |
| Skill Intelligence   | Keyword-based matching     |
| PDF Parsing          | PyPDF2                     |
| Programming Language | Python 3.10                |

---

## 📂 Project Structure

```
talentmatch-ai/
│── app.py                # Streamlit web UI
│── src/
│   ├── pdf_parser.py     # PDF text extractor
│   ├── text_preprocess.py # NLP cleaning
│   ├── scorer.py         # Scoring pipeline
│── sample_data/
│   ├── resumes/          # Example resumes (optional)
│   ├── jd_ml_engineer.txt # Sample JD
│── requirements.txt
│── README.md
```

---

## 📸 Screenshots

### Upload Resumes & JD Input

<img width="1920" height="1080" alt="Screenshot (245)" src="https://github.com/user-attachments/assets/7f1b517b-2903-420b-b350-78a48b2d14af" />


### Ranked Results Table

<img width="1920" height="1080" alt="Screenshot (250)" src="https://github.com/user-attachments/assets/788f0c81-43bb-4b9d-a5a2-72f51b5ee3f6" />


---

## ▶️ Run Locally

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch application

```bash
streamlit run app.py
```

Visit 👉 [http://localhost:8501/](http://localhost:8501/)

---

## 🧪 Usage Examples

✔ Compare resumes for **different job roles** (Web Dev, Data Analyst, ML Engineer)
✔ Identify **missing skills** for upskilling
✔ Provide **ranked shortlists** to hiring teams

---

## 🧭 Future Enhancements

🔹 Role-based Skill Dictionaries (Web / Data / ML)
🔹 Resume-specific feedback statements
🔹 Wordcloud visualizations of found skills
🔹 Support for BERT embeddings for semantic analysis
🔹 PDF/Docx report export
🔹 Deployable on Streamlit Cloud with user uploads

> This project is built to easily accept advanced NLP upgrades.

---

## 🧑‍💻 Author

**Kandarp Joshi**
AI & Data Science Developer

🌐  Github: [@Kandarp Joshi](https://github.com/KandarpJoshi1112)
🔗  LinkedIn: [@Kandarp Joshi](https://www.linkedin.com/in/kandarp-joshi-3451231bb/)

---

## ⭐ Support

If you find this project useful, please **star ⭐ the repository** — it really helps!

---

# 🎯 Conclusion

TalentMatch AI delivers a **fast, intelligent and actionable** resume ranking solution using NLP.
It is designed as a **practical AI hiring assistant**, showcasing real-world ML skills in deployment-ready form — perfect for professional and academic portfolios.

