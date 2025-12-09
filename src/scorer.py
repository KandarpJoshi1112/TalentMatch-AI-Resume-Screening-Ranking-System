import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .text_preprocess import clean_text

# Combined skill dictionary: ML + Web Dev (you can expand anytime)
SKILLS = {
    # ML / Data
    "python", "pandas", "numpy", "sql",
    "scikit-learn", "sklearn", "tensorflow", "pytorch",
    "machine learning", "deep learning",
    "supervised learning", "unsupervised learning",

    # MLOps / Cloud
    "git", "docker", "kubernetes",
    "aws", "gcp", "azure",

    # Web Dev
    "javascript", "typescript", "react", "reactjs",
    "node", "node.js", "nodejs",
    "express", "express.js", "expressjs",
    "html", "css",
    "mongodb", "mongo",
    "rest", "rest api", "api",
    "websockets",
}


def extract_skills(text: str):
    text_lower = text.lower()
    found = {skill for skill in SKILLS if skill in text_lower}
    return found


def score_resumes(jd_text: str, resume_texts: dict) -> pd.DataFrame:
    """
    TF-IDF similarity + skill coverage scoring.
    """
    if not jd_text or not resume_texts:
        return pd.DataFrame()

    # Clean text for TF-IDF similarity
    cleaned_jd = clean_text(jd_text)
    cleaned_resumes = {fn: clean_text(txt) for fn, txt in resume_texts.items()}

    # TF-IDF on JD + all resumes
    docs = [cleaned_jd] + list(cleaned_resumes.values())
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs)

    jd_vec = vectors[0]
    resume_vecs = vectors[1:]
    sims = cosine_similarity(jd_vec, resume_vecs).flatten()

    # Skill sets (raw text, not cleaned)
    jd_skills = extract_skills(jd_text)

    results = []
    for i, (fn, raw_text) in enumerate(resume_texts.items()):
        resume_skills = extract_skills(raw_text)

        # Skills actually in BOTH JD and resume
        common_skills = jd_skills & resume_skills
        missing_skills = jd_skills - resume_skills

        sim_score = sims[i] * 100  # 0–100
        if jd_skills:
            skill_coverage = (len(common_skills) / len(jd_skills)) * 100
        else:
            skill_coverage = 0.0

        # Clamp both to [0, 100]
        sim_score = max(0.0, min(100.0, sim_score))
        skill_coverage = max(0.0, min(100.0, skill_coverage))

        # Weighted final score
        match_score = (0.8 * sim_score) + (0.2 * skill_coverage)

        results.append({
            "file_name": fn,
            "similarity": round(sim_score, 2),
            "skill_coverage": round(skill_coverage, 2),
            "match_score": round(match_score, 2),
            "matched_skills": ", ".join(sorted(common_skills)) if common_skills else "-",
            "missing_skills": ", ".join(sorted(missing_skills)) if missing_skills else "-",
        })

    df = pd.DataFrame(results)
    df = df.sort_values(by="match_score", ascending=False).reset_index(drop=True)
    return df
