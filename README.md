# Government Exam Research Assistant

A **Python-based AI chatbot** designed to help students prepare for government exams.  
It provides **topic-wise questions**, **previous year paper summaries**, and **study tips** using OpenAI GPT models via LangChain. The project includes a **Tkinter GUI** for a user-friendly desktop experience.

---

## **Features**

- Collect and summarize **previous year papers** for any government exam.
- Generate **practice questions** on every topic of the syllabus.
- Provide **explanations, tips, and resources** for each question/topic.
- Maintain **chat history** for continuous conversation.
- **Save chat** history to a file.
- **Clear chat** to start fresh.
- Modular structure with support for **search and Wikipedia tools**.

---

## **Project Structure**
gov_exam_assistant/
│
├── .env # OpenAI API key
├── models.py # Pydantic model for structured responses
├── tools.py # Custom tools (search, Wikipedia, save)
├── agent_setup.py # LLM, prompt, parser, agent executor
├── main.py # CLI testing of the agent
├── gui_chatbot.py # Tkinter GUI chatbot
├── chat_history.txt # Optional saved chat history
└── requirements.txt # Python dependencies


---

## **Setup**

1. Clone the repository:

```bash
git clone <repo-url>
cd gov_exam_assistant
Create and activate a Python environment:
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

Install dependencies:
pip install -r requirements.txt

Create a .env file in the project root and add your OpenAI API key:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

Run GUI
python gui_chatbot.py
