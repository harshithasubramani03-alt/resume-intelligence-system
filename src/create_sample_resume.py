from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Priya Sharma", ln=True)

pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, "Email: priya.sharma@email.com | Phone: 9876543210 | Bengaluru, India", ln=True)
pdf.ln(5)

pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 8, "Summary", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 6, "Data Science student with hands-on experience in Python, machine learning, and data analysis. Built end-to-end ML projects including fraud detection and price prediction models.")
pdf.ln(3)

pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 8, "Skills", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 6, "Python, SQL, Pandas, NumPy, Scikit-learn, Machine Learning, Data Visualization, Streamlit, Git, Excel")
pdf.ln(3)

pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 8, "Projects", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 6, "Credit Card Fraud Detection: Built a classification model using Logistic Regression, Random Forest, and XGBoost on transaction data. Deployed using Streamlit.\n\nHouse Price Prediction: Used Lasso regression for feature selection and Ridge regression for final model, deployed as a web app.")
pdf.ln(3)

pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 8, "Education", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 6, "B.Tech in Computer Science, XYZ University (2022-2026)")

pdf.output("../data/sample_resumes/test_resume.pdf")
print("Sample resume PDF created successfully!")
