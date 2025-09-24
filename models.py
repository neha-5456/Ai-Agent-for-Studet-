from pydantic import BaseModel
from typing import List

class ResearchResponse(BaseModel):
    exam_name: str
    topics: List[str]
    questions: List[str]
    previous_year_summary: str
