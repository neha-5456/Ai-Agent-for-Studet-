from agent_setup import agent_executor, parser

exams = [
    "UPSC Prelims Indian Polity",
    "SSC CGL Quantitative Aptitude",
    "RBI Grade B Economic and Social Issues"
]

for exam in exams:
    raw_response = agent_executor.invoke({
        "query": f"Prepare topic-wise questions and past papers for {exam}."
    })
    
    try:
        structured_response = parser.parse(raw_response.get("output")[0]["text"])
        print(f"=== {exam} ===")
        print("Exam Name:", structured_response.exam_name)
        print("Topics:", structured_response.topics)
        print("Questions:", structured_response.questions)
        print("Previous Year Summary:", structured_response.previous_year_summary)
        print("\n" + "="*60 + "\n")
    except Exception as e:
        print(f"Error parsing response for {exam}: {e}")
