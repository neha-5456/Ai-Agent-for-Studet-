# Government Exam Research Assistant

A Python project that uses **LangChain** and **OpenAI GPT** to help students prepare for government exams. The assistant can:

- Collect and summarize previous year exam papers
- Generate topic-wise practice questions
- Provide detailed explanations, tips, and resources
- Output structured JSON for easy study plan creation
- Optionally search the web or Wikipedia for updated information
- Save research output to a text file

---

## Features

1. **Dynamic Exam Support**  
   Works for any government exam by specifying the exam name.

2. **Structured Output**  
   Uses a Pydantic model (`ResearchResponse`) to generate JSON containing:
   - `exam_name`
   - `topics`
   - `questions`
   - `previous_year_summary`

3. **Integrated Tools**  
   - `search_tool`: Web search using DuckDuckGo  
   - `wiki_tool`: Query Wikipedia for content  
   - `save_tool`: Save research output to a text file  

4. **LLM**  
   Powered by OpenAI GPT (`gpt-4o-mini`), using the API key from `.env`.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/gov-exam-assistant.git
cd gov-exam-assistant
