import re

SKILL_ALIASES = {
    "python": ["python"],
    "sql": ["sql", "mysql", "postgresql", "t-sql"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript"],
    "c++": ["c++", "cpp"],
    "c#": ["c#", "csharp"],
    ".net": [".net", "dotnet", "asp.net", "asp.net core", ".net core"],
    "react": ["react", "reactjs", "react.js"],
    "redux": ["redux", "redux toolkit"],
    "node.js": ["node.js", "nodejs"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "rest api": ["rest api", "restful api", "web api", "rest services", "restful services"],
    "graphql": ["graphql"],
    "machine learning": ["machine learning"],
    "deep learning": ["deep learning"],
    "nlp": ["natural language processing"],
    "computer vision": ["computer vision"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "data visualization": ["data visualization", "data viz"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "excel": ["excel", "ms excel", "microsoft excel"],
    "git": ["git", "git version control"],
    "github": ["github", "github actions"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes"],
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": ["google cloud", "google cloud platform"],
    "ci/cd": ["ci/cd", "cicd", "continuous integration", "continuous deployment"],
    "agile": ["agile"],
    "scrum": ["scrum"],
    "streamlit": ["streamlit"],
    "flask": ["flask"],
    "django": ["django"],
    "mongodb": ["mongodb", "mongo"],
    "statistics": ["statistics"],
    "a/b testing": ["a/b testing", "ab testing"],

    "social media management": ["social media management", "social media"],
    "content creation": ["content creation"],
    "email marketing": ["email marketing"],
    "seo": ["seo", "search engine optimization"],
    "sem": ["search engine marketing"],
    "brand strategy": ["brand strategy"],
    "google analytics": ["google analytics"],
    "copywriting": ["copywriting"],
    "market research": ["market research"],
    "campaign management": ["campaign management"],

    "financial modeling": ["financial modeling", "financial modelling"],
    "budgeting": ["budgeting"],
    "forecasting": ["forecasting"],
    "quickbooks": ["quickbooks"],
    "financial statements": ["financial statements"],
    "payroll": ["payroll"],
    "tax preparation": ["tax preparation"],
    "auditing": ["auditing"],

    "recruiting": ["recruiting", "recruitment"],
    "onboarding": ["onboarding"],
    "employee relations": ["employee relations"],
    "performance management": ["performance management"],
    "hris": ["hris"],
    "talent acquisition": ["talent acquisition"],

    "project management": ["project management"],
    "communication": ["communication", "communication skills"],
    "leadership": ["leadership"],
    "problem solving": ["problem solving", "problem-solving"],
    "data analysis": ["data analysis"],
    "customer service": ["customer service"],
    "presentation skills": ["presentation skills"],
    "teamwork": ["teamwork"]
}


def extract_skills(text):
    found_skills = []
    text_lower = text.lower()

    for canonical_skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            pattern = r'\b' + re.escape(alias) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.append(canonical_skill)
                break

    return found_skills


def compare_skills(resume_text, jd_text):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))

    matching_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills

    return {
        "matching_skills": sorted(list(matching_skills)),
        "missing_skills": sorted(list(missing_skills)),
        "resume_skills": sorted(list(resume_skills)),
        "jd_skills": sorted(list(jd_skills))
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

    result = compare_skills(resume_text, jd_text)

    print("Matching Skills:", result["matching_skills"])
    print("Missing Skills:", result["missing_skills"])