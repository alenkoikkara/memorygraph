from pydantic import BaseModel
import re
from typing import Tuple

class ContentInput(BaseModel):
    """Model for handling content input, supporting both URL and text content."""
    content: str

    def is_url(self) -> bool:
        """Check if the content is a valid URL."""
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

    def get_content(self) -> Tuple[str, str]:
        """Extract content based on input type (URL or text)."""
        if self.is_url():
            from services.url_parser import extract_main_content
            return self.content, extract_main_content(self.content)
        else:
            brief = self.content[:100] + "..." if len(self.content) > 100 else self.content
            return brief, self.content 
        
class SearchQuery(BaseModel):
    """Model for handling search query input."""
    query: str
