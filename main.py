from typing import Union, Optional
from fastapi import FastAPI
from core.core import create_record
from core.core import Record
from pydantic import BaseModel
from services.url_parser import extract_main_content
import re

app = FastAPI()

class ContentInput(BaseModel):
    content: str

    def is_url(self) -> bool:
        # Simple URL pattern matching
        url_pattern = re.compile(
            r'^(https?:\/\/)?'  # http:// or https://
            r'((([a-z\d]([a-z\d-]*[a-z\d])*)\.)+[a-z]{2,}|'  # domain
            r'((\d{1,3}\.){3}\d{1,3}))'  # or ip
            r'(\:\d+)?'  # port
            r'(\/[-a-z\d%_.~+]*)*'  # path
            r'(\?[;&a-z\d%_.~+=-]*)?'  # query
            r'(\#[-a-z\d_]*)?$',  # fragment
            re.IGNORECASE
        )
        return bool(url_pattern.match(self.content))

    def get_content(self) -> tuple[str, str]:
        if self.is_url():
            # For URLs, return the URL as original and extracted content as text
            return self.content, extract_main_content(self.content)
        else:
            # For text, return a brief version as original and full text
            brief = self.content[:100] + "..." if len(self.content) > 100 else self.content
            return brief, self.content

class SummaryResponse(BaseModel):
    record: Record

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/api/v1/process", response_model=SummaryResponse)
async def process_content(input: ContentInput):
    original, content = input.get_content()
    response = create_record(original, content)
    return SummaryResponse(record=response)

