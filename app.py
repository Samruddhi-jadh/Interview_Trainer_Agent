import streamlit as st
from resume_parser import parse_resume
from rag_utils import get_questions_by_role
from granite_integration import query_granite
from prompts import EXTRACT_INFO_PROMPT, GEN_QUESTIONS_PROMPT, GEN_ANSWERS_TIPS_PROMPT
import time

# Set page config
st.set_page_config(
    page_title="Interview Trainer Agent",
    layout="wide",
    page_icon="💼"
)

# Header
st.markdown("<h1 style='color:#4CAF50;'>💼 AI Interview Trainer Agent</h1>", unsafe_allow_html=True)
st.markdown("🔍 *Get personalized interview questions, answers, and expert tips based on your resume or job title.*")

# Sidebar
st.sidebar.image("logo.png", width=150)
st.sidebar.markdown("**Built with IBM Granite + RAG**")
st.sidebar.markdown("🚀 Created by Samy")

# Predefined roles
job_roles_list = [
    "Data Scientist", "Software Engineer", "Machine Learning Engineer",
    "Frontend Developer", "Backend Developer", "Full Stack Developer",
    "DevOps Engineer", "Cloud Engineer", "Cybersecurity Analyst",
    "Data Analyst", "UI/UX Designer", "Product Manager",
    "QA Engineer", "AI Researcher", "Business Analyst",
    "Technical Writer", "Robotics Engineer", "Mobile App Developer",
    "Network Engineer", "Blockchain Developer", "Other"
]

# Resume upload and role selection
st.markdown("### 📤 Upload your Resume (PDF) *or* Select/Enter a Job Role")
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
selected_role = st.selectbox("Select Job Role", job_roles_list)
manual_job = ""
if selected_role == "Other":
    manual_job = st.text_input("Type your job role")

# Name input
user_name = st.text_input("Enter your name (for personalized coaching)", value="Candidate")

# Submit button
if st.button("🚀 Start Interview Preparation"):
    job_role = manual_job.strip() if selected_role == "Other" else selected_role
    resume_text = ""
    experience = "2 years"

    with st.spinner("🔍 Extracting information..."):
        if uploaded_file:
            resume_text = parse_resume(uploaded_file)
            prompt = EXTRACT_INFO_PROMPT.replace("{text}", resume_text)
            extracted_info = query_granite(prompt)
            st.success("✅ Resume parsed successfully!")
            st.markdown(f"**Extracted Info:**\n\n```{extracted_info}```")

    # Step 2: Fetch Questions
    with st.spinner("📚 Retrieving role-specific questions..."):
        rag_data = get_questions_by_role(job_role)
        technical = rag_data.get("technical", [])
        hr = rag_data.get("hr", [])

        st.subheader("📋 Retrieved Questions (RAG)")
        st.markdown("#### 🛠️ Technical Questions:")
        for q in technical:
            st.markdown(f"- {q}")
        st.markdown("#### 🧠 HR Questions:")
        for q in hr:
            st.markdown(f"- {q}")

    all_questions = technical + hr
    questions_prompt = GEN_ANSWERS_TIPS_PROMPT.replace("{questions}", "\n".join(all_questions))

    # Step 3: Generate Answers + Tips
    if st.button("🎯 Generate Model Answers & Tips"):
        with st.spinner("💡 Generating model answers using IBM Granite..."):
            response = query_granite(questions_prompt)
            time.sleep(1)
            st.success("✅ Answers generated successfully!")
            st.markdown("### 🧠 Model Answers and Tips")
            st.markdown(f"```{response}```")

    # Step 4: AGENTIC AI MODE
    st.markdown("---")
    st.markdown("### 🤖 Smart Agent Mode (Agentic AI Coaching)")
    st.markdown("*Let the AI agent think, plan, and guide you like a real career coach.*")

    if st.button("🧠 Let the AI Agent Guide Me"):
        with st.spinner("🧠 Generating your personalized coaching strategy..."):
            agent_prompt = f"""
            You are an intelligent Interview Coach AI for job seekers.
            Your task is to guide {user_name}, who is applying for the role of '{job_role}' with {experience} experience.

            Follow a structured 3-step coaching plan:
            Step 1: Profile Understanding
            - Summarize the candidate’s strengths, background, and interview goals.

            Step 2: Coaching Plan
            - List 3 key technical or behavioral areas to focus on.
            - Mention common mistakes made by candidates in this role.
            - Give improvement tips or resources.

            Step 3: Mock Interview Drill
            - Generate 3 targeted technical/HR questions.
            - Add short answer strategy for each (not full answer, just approach).

            Format your response in markdown, using bullet points and headers for clarity.
            """
            coaching_response = query_granite(agent_prompt)
            time.sleep(1)
            st.success("✅ Your AI coaching plan is ready!")
            st.markdown("### 🧠 Agentic Coaching Strategy")
            st.markdown(coaching_response, unsafe_allow_html=True)
else:
    st.info("👈 Select a job role or upload a resume, then click 'Start Interview Preparation'.")
