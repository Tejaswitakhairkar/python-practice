import streamlit as st
import pdfplumber

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.markdown("""
# 🤖 AI Resume Analyzer

### 🚀 AI Powered ATS Resume Checker

📄 Upload your Resume and get:

✅ ATS Score

✅ Skills Analysis

✅ AI Suggestions

✅ Job Role Prediction
""")

st.divider()
with st.sidebar:
    st.title("📋 Menu")

    st.markdown("### Features")

    st.write("✅ ATS Score")
    st.write("✅ Skills Detection")
    st.write("✅ Missing Skills")
    st.write("✅ Resume Suggestions")
    st.write("✅ Job Role Prediction")
    st.write("✅ Resume Strengths")
    st.write("✅ Resume Weaknesses")

st.subheader("👤 Candidate Details")

name = st.text_input("Enter Your Name")

st.subheader("📄 Upload Your Resume")

resume = st.file_uploader(
    "Choose your Resume (PDF only)",
    type=["pdf"],
    help="Upload your resume in PDF format."
)

if st.button("Analyze Resume"):

    if resume is not None:

        st.success("Resume Uploaded Successfully!")

        text = ""

        with pdfplumber.open(resume) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        st.subheader("Resume Text")
        st.write(text)

        skills = [
              "Python",
            "Java",
            "C++",
            "C",
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "SQL",
            "MongoDB",
            "Machine Learning",
            "AI",
            "Git",
            "Docker"
        ]

        found_skills = []

        for skill in skills:
            if skill.lower() in text.lower():
                found_skills.append(skill)

        st.subheader("Detected Skills")

        if found_skills:
            for skill in found_skills:
                st.success(skill)
        else:
            st.warning("No skills detected.")
            st.subheader("Detected Skills")

if found_skills:
    for skill in found_skills:
        st.success(skill)
else:
    st.warning("No skills detected.")

st.subheader("ATS Score")

score = min(len(found_skills) * 10, 100)

st.progress(score)

st.success(f"Your ATS Score is: {score}/100")

st.subheader("❌ Missing Skills")

missing_skills = []

for skill in skills:
    if skill not in found_skills:
        missing_skills.append(skill)

if missing_skills:
    for skill in missing_skills:
        st.error(skill)
else:
    st.success("No Missing Skills 🎉")
    st.subheader("💡 Resume Suggestions")

suggestions = []

if "Git" not in found_skills:
    suggestions.append("Add Git skills.")

if "SQL" not in found_skills:
    suggestions.append("Learn SQL and add it to your resume.")

if "Machine Learning" not in found_skills:
    suggestions.append("Add Machine Learning projects.")

if "AI" not in found_skills:
    suggestions.append("Include AI-related skills or projects.")

if "Docker" not in found_skills:
    suggestions.append("Learn Docker for better backend knowledge.")

if suggestions:
     for suggestion in suggestions:
        st.info(suggestion)
else:
    st.success("🎉 Excellent! Your resume already includes the major skills.")
    st.subheader("💼 Recommended Job Role")

roles = []

if "Python" in found_skills and "Machine Learning" in found_skills:
    roles.append("AI / Machine Learning Engineer")

if "React" in found_skills and "JavaScript" in found_skills:
    roles.append("Frontend Developer")

if "Node.js" in found_skills and "MongoDB" in found_skills:
    roles.append("Backend Developer")

if "React" in found_skills and "Node.js" in found_skills:
    roles.append("Full Stack Developer")

if "SQL" in found_skills:
    roles.append("Data Analyst")

if roles:
    for role in roles:
        st.success(role)
else:
    st.warning("No suitable job role found.")
    st.subheader("💪 Resume Strengths")

strengths = []

if len(found_skills) >= 8:
    strengths.append("Strong Technical Skills")

if "React" in found_skills and "Node.js" in found_skills:
    strengths.append("Full Stack Development Skills")

if "SQL" in found_skills:
    strengths.append("Database Knowledge")

if strengths:
    for strength in strengths:
        st.success(strength)
else:
    st.warning("No major strengths detected.")
    st.subheader("⚠️ Resume Weaknesses")

weaknesses = []

if "Machine Learning" not in found_skills:
    weaknesses.append("Machine Learning skills are missing.")

if "Docker" not in found_skills:
    weaknesses.append("Docker knowledge is missing.")

if "Git" not in found_skills:
    weaknesses.append("Git skills are missing.")

if "AI" not in found_skills:
    weaknesses.append("AI-related skills are missing.")

if weaknesses:
    for weakness in weaknesses:
        st.error(weakness)
else:
    st.success("No major weaknesses found.")
    st.subheader("📈 Resume Match Percentage")

total_skills = len(skills)
matched_skills = len(found_skills)

match_percentage = (matched_skills / total_skills) * 100

st.progress(int(match_percentage))

st.success(f"Resume Match: {match_percentage:.1f}%")
st.subheader("📜 Certifications")

certifications = [
    "AWS",
    "Google",
    "Microsoft",
    "Oracle",
    "Coursera",
    "Udemy",
    "NPTEL"
]

found_certifications = []

for cert in certifications:
    if cert.lower() in text.lower():
        found_certifications.append(cert)

if found_certifications:
    for cert in found_certifications:
        st.success(cert)
else:
    st.warning("No certifications found.")
    st.subheader("🏆 Resume Rating")

if match_percentage >= 85:
    st.success("🌟 Excellent Resume")
elif match_percentage >= 70:
    st.success("✅ Good Resume")
elif match_percentage >= 50:
    st.warning("🟡 Average Resume")
else:
    st.error("🔴 Poor Resume")
    st.subheader("💼 Experience")

experience_words = [
    "Internship",
    "Experience",
    "Worked",
    "Developer",
    "Engineer"
]

experience_found = False

for word in experience_words:
    if word.lower() in text.lower():
        experience_found = True
        break

if experience_found:
    st.success("Experience Found")
else:
    st.warning("No Experience Found")
    