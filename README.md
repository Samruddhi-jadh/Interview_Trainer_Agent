# 💼 Interview Trainer Agent — Powered by Agentic AI & IBM Granite

An AI-powered Interview Preparation Assistant that uses IBM Granite foundation models and Retrieval-Augmented Generation (RAG) to generate personalized interview questions, answers, and coaching plans based on a user’s resume or job role. It simulates a smart coaching experience using Agentic AI techniques.

---

## 🚀 Features

- 📄 **Resume Parsing or Job Title Input**
- 🧠 **Role-Specific Question Retrieval (via RAG)**
- 💡 **LLM-Based Answer & Tip Generation (IBM Granite)**
- 🤖 **Agentic AI Coaching Mode** — a smart, planning assistant that guides you like a real coach
- 📊 Simple, interactive UI using **Streamlit**

---

## 🧠 Technologies Used

| Component        | Stack                               |
|------------------|--------------------------------------|
| Frontend         | Streamlit (Python)                  |
| AI Model         | IBM Granite (`granite-13b-chat`)    |
| RAG Backend      | Pre-curated JSON knowledge base     |
| Agentic AI Mode  | Plan–Think–Act prompting logic      |
| Cloud Platform   | IBM Cloud + Watsonx.ai              |

---

## ⚙️ Setup Instructions

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/interview-trainer-agent.git
cd interview-trainer-agent
````

2. **Install required libraries**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file** with the following:

```env
IBM_API_KEY=your-api-key-here
IBM_URL=https://us-south.ml.cloud.ibm.com
IBM_INSTANCE_ID=your-instance-id
IBM_DEPLOYMENT_ID=granite-chat-agent
```

> 💡 Get these values from IBM Cloud → Resources → Your Watsonx.ai instance → Service Credentials

4. **Run the app**

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```plaintext
├── app.py                   # Streamlit UI logic
├── resume_parser.py         # PDF text extractor
├── rag_utils.py             # Retrieves questions based on role
├── prompts.py               # Prompt templates for IBM Granite
├── granite_integration.py   # Handles Granite API requests
├── assets/
│   └── logo.png             # App logo
├── .env                     # (Your secret keys here)
└── requirements.txt         # Python dependencies
```

---

## 💡 Smart Agent Mode (Agentic AI)

The Agentic AI mode uses LLM prompting to:

* Plan a 3-step interview preparation strategy
* Highlight focus areas, common mistakes, and practice questions
* Simulate a career coach that **reasons and adapts** like a human

---

## 🎯 Problem Statement Addressed

> **Problem Statement No.22 – Interview Trainer Agent**
 : An Interview Trainer Agent, powered by RAG (Retrieval-Augmented Generation),
prepares users for job interviews by generating tailored question sets and preparation strategies based
on their profile name, experience level, and job role.
It retrieves role-specific interview questions, industry expectations, behavioral scenarios, and HR
guidelines from recruitment portals, professional networks, and company interview databases.
Users can input their resume or job title, and the agent provides targeted questions, model answers,
and improvement tips.
It supports both technical and soft skill assessment, ensuring a comprehensive interview prep
experience.
This AI-driven assistant builds user confidence, sharpens responses, and increases success rates in
competitive hiring environments.

---

## 📸 Screenshots

![UI Demo](assets/demo.png)

---

## 👤 Author

* **Samruddhi Jadhav**


---

## 📜 License

