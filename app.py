import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from extract_text import extract_text_from_pdf, get_job_description_text
from ats_score import calculate_ats_score
from bullet_improver import improve_bullet_point

st.set_page_config(page_title="AI Resume Intelligence System", page_icon="📄", layout="wide")

st.title("📄 AI-Powered Resume Intelligence System")
st.write("Upload your resume and paste a job description to get your ATS score, skill gaps, and AI-powered improvement suggestions.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Upload Resume (PDF)")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

with col2:
    st.subheader("2. Paste Job Description")
    jd_input = st.text_area("Paste the job description here", height=250)

analyze_button = st.button("🔍 Analyze Resume", type="primary")

if analyze_button:
    if uploaded_file is None:
        st.error("Please upload a resume PDF first.")
    elif not jd_input.strip():
        st.error("Please paste a job description.")
    else:
        with st.spinner("Analyzing your resume..."):
            with open("temp_resume.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())

            resume_text = extract_text_from_pdf("temp_resume.pdf")
            jd_text = get_job_description_text(jd_input)

            result = calculate_ats_score(resume_text, jd_text)

            os.remove("temp_resume.pdf")

        st.success("Analysis complete!")

        st.subheader("📊 Your ATS Score")
        score = result["ats_score"]
        st.metric(label="Overall Match Score", value=f"{score}/100")
        st.progress(min(int(score), 100) / 100)

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("✅ Matching Skills")
            if result["matching_skills"]:
                for skill in result["matching_skills"]:
                    st.write(f"✔️ {skill}")
            else:
                st.write("No matching skills found.")

        with col4:
            st.subheader("❌ Missing Skills")
            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.write(f"⚠️ {skill}")
            else:
                st.write("No missing skills — great match!")

        st.divider()
        st.subheader("✍️ Improve a Resume Bullet Point")
        bullet_input = st.text_area("Paste a weak bullet point from your resume", height=80)
        improve_button = st.button("✨ Improve with AI")

        if improve_button and bullet_input.strip():
            with st.spinner("Improving your bullet point..."):
                improved = improve_bullet_point(bullet_input)
            
            col5, col6 = st.columns(2)
            with col5:
                st.markdown("**Original:**")
                st.info(bullet_input)
            with col6:
                st.markdown("**Improved:**")
                st.success(improved)