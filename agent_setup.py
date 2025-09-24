from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from models import ResearchResponse
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

# LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Prompt 
# Prompt 
prompt = ChatPromptTemplate([
    ("system",
     """Instructions: {format_instructions}
        You are a research assistant for a student preparing for government exams.
        Your job:
        1. Collect & summarize previous year papers for any government exam.
        2. Generate practice questions on every topic of the syllabus.
        3. Provide detailed explanations, tips, and resources.
        4. Help the student organize their study plan efficiently.
        Be structured, clear, and student-friendly.
        """
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")  # <- Use correct variable name
]).partial(format_instructions="Answer in a clear step-by-step manner, with examples if possible.")

# Agent
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[search_tool, wiki_tool, save_tool]
)

# Agent Executor
agent_executor = AgentExecutor(agent=agent, tools=[], verbose=False)
