from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List
import os

groq_api_key = os.environ.get("GROQ_API_KEY")
class Tags(BaseModel):
    tags: List[str]

class LLMExtractor:
    def __init__(self):
        self.llm = ChatGroq(api_key=groq_api_key,
                        model="llama-3.1-8b-instant",
                        temperature=0.3)
        self.parser = PydanticOutputParser(pydantic_object=Tags)
        self.prompt = ChatPromptTemplate.from_template(
            "Extract relevant tags from the text below.\n\nText: {text}\n\n{format_instructions}"
        ).partial(format_instructions=self.parser.get_format_instructions())

    def extract_tags(self, text):
        response = self.llm(self.prompt.format_messages(text=text))
        return self.parser.parse(response.content).tags
