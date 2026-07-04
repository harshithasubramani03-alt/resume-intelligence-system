from semantic_match import calculate_similarity
from skill_extractor import compare_skills


def calculate_ats_score(resume_text, jd_text):
    """
    Combines semantic similarity and skill matching into one ATS score.
    Formula: 60% semantic similarity + 40% skill match ratio
    """
    semantic_score = calculate_similarity(resume_text, jd_text)

    skills_result = compare_skills(resume_text, jd_text)
    jd_skills = skills_result["jd_skills"]
    matching_skills = skills_result["matching_skills"]

    if len(jd_skills) > 0:
        skill_match_ratio = (len(matching_skills) / len(jd_skills)) * 100
    else:
        skill_match_ratio = 0

    final_score = (0.6 * semantic_score) + (0.4 * skill_match_ratio)

    return {
        "ats_score": round(final_score, 2),
        "semantic_score": semantic_score,
        "skill_match_ratio": round(skill_match_ratio, 2),
        "matching_skills": skills_result["matching_skills"],
        "missing_skills": skills_result["missing_skills"]
    }


if __name__ == "__main__":
    from extract_text import extract_text_from_pdf, get_job_description_text

    resume_text = extract_text_from_pdf("../data/sample_resumes/test_resume.pdf")

    sample_jd = """
    We are looking for a Data Science intern with strong skills in Python, 
    SQL, machine learning, and data visualization. Experience with 
    scikit-learn and pandas is a plus.
    """
    jd_text = get_job_description_text(sample_jd)

    result = calculate_ats_score(resume_text, jd_text)

    print(f"ATS Score: {result['ats_score']}/100")
    print(f"Semantic Score: {result['semantic_score']}%")
    print(f"Skill Match Ratio: {result['skill_match_ratio']}%")
    print(f"Matching Skills: {result['matching_skills']}")
    print(f"Missing Skills: {result['missing_skills']}")