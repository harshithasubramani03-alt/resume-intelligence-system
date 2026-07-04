from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_similarity(resume_text, jd_text):
    """
    Takes resume text and job description text.
    Returns a similarity score between 0 and 100.
    """
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, jd_embedding)
    score = similarity.item() * 100

    return round(score, 2)


if __name__ == "__main__":
    from extract_text import extract_text_from_pdf, get_job_description_text

    resume_text = extract_text_from_pdf("../data/sample_resumes/test_resume.pdf")

    sample_jd = """
    We are looking for a Data Science intern with strong skills in Python, 
    SQL, machine learning, and data visualization. Experience with 
    scikit-learn, pandas, and deploying ML models is a plus. 
    Currently pursuing or recently completed a degree in Computer Science 
    or related field.
    """
    jd_text = get_job_description_text(sample_jd)

    score = calculate_similarity(resume_text, jd_text)
    print(f"Match Score: {score}%")