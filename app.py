import streamlit as st
import pandas as pd

from src.parse_resumes import extract_text_from_pdf  # ⬅️ NEW IMPORT
from src.parse_resumes import extract_text_from_pdf
from src.scorer import score_resumes

st.title("📄 Machine Learning Engineer - Resume Scanner")

st.write("Upload one or more resumes (PDF) and a Job Description to get relevance ranking.")

jd_option = st.radio(
    "Select Job Description Input:",
    ("Use Sample JD", "Paste JD Text")
)

if jd_option == "Paste JD Text":
    jd_text = st.text_area("Enter Job Description")
else:
    jd_text = None  # We will load from sample_data later

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze Resumes"):

    if not uploaded_files:
        st.warning("⚠️ Please upload at least one resume PDF.")
    else:
        st.info("🔄 Parsing resumes...")

        resume_texts = {}
        for f in uploaded_files:
            resume_texts[f.name] = extract_text_from_pdf(f.read())

        # Load JD text based on user choice
        if jd_option == "Paste JD Text":
            if not jd_text or jd_text.strip() == "":
                st.warning("⚠️ Please paste a valid Job Description.")
                st.stop()
            jd_raw = jd_text  # USE the pasted JD 🚀
        else:
            # Load sample ML JD
            with open("sample_data/jd_ml_engineer.txt", "r", encoding="utf-8") as f:
                jd_raw = f.read()

        st.info("⚙️ Scoring resumes...")
        results_df = score_resumes(jd_raw, resume_texts)
        results_df.index.name = "Rank"
        results_df.reset_index(inplace=True)
        st.subheader("📊 Resume Match Scores")

        # Always work on a copy so we don't modify original unexpectedly
        results_df = results_df.copy()

        # If Rank already exists from previous step / scorer, drop it
        if "Rank" in results_df.columns:
            results_df = results_df.drop(columns=["Rank"])

        # Ensure sorted by match_score (just in case)
        results_df = results_df.sort_values(by="match_score", ascending=False).reset_index(drop=True)

        # Add Rank column (1, 2, 3, ...)
        results_df.insert(0, "Rank", range(1, len(results_df) + 1))

        # Highlight top match
        top_row = results_df.iloc[0]
        st.success(
            f"🏆 **Top Match: {top_row['file_name']}** — Score: {top_row['match_score']}%"
        )

        # Show results table
        st.dataframe(
            results_df[[
                "Rank",
                "file_name",
                "match_score",
                "similarity",
                "skill_coverage",
                "matched_skills",
                "missing_skills"
            ]],
            width="stretch"
        )

        # Download report
        csv = results_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv,
            file_name="resume_ranking_report.csv",
            mime="text/csv"
        )