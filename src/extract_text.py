import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Takes a path to a PDF file and returns the extracted text as a string.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # some pages might be empty/images, skip those
                text += page_text + "\n"
    return text


def get_job_description_text(jd_input):
    """
    For now, just returns the JD text directly.
    Later this could read from a file or URL.
    """
    return jd_input.strip()


# quick test — only runs when you run this file directly
if __name__ == "__main__":
    sample_path = "../data/sample_resumes/test_resume.pdf"
    result = extract_text_from_pdf(sample_path)
    print(result)