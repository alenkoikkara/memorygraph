from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, List, Optional, Tuple
import requests
from bs4 import BeautifulSoup
import re

def fetch_url_content(url: str) -> Dict[str, str]:
    """
    Fetch content from a URL and return it in a structured format.
    
    Args:
        url (str): The URL to fetch content from
        
    Returns:
        Dict[str, str]: Dictionary containing different parts of the content
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text content
        text = soup.get_text()
        # Clean up text
        text = re.sub(r'\s+', ' ', text).strip()
        
        return {
            'title': soup.title.string if soup.title else '',
            'text': text,
            'links': [link.get('href') for link in soup.find_all('a', href=True)],
            'images': [img.get('src') for img in soup.find_all('img', src=True)],
            'status_code': response.status_code,
            'content_type': response.headers.get('content-type', '')
        }
    except requests.RequestException as e:
        return {
            'error': str(e),
            'status_code': getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None
        }

def extract_main_content(url: str) -> str:
    """
    Extract the main content from a URL, focusing on the article or main text.
    
    Args:
        url (str): The URL to extract content from
        
    Returns:
        str: The main content text
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
            
        # Try to find the main content
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile(r'content|main|article'))
        
        if main_content:
            text = main_content.get_text()
        else:
            text = soup.get_text()
            
        # Clean up text
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    except requests.RequestException as e:
        return f"Error fetching content: {str(e)}"

def get_metadata(url: str) -> Dict[str, str]:
    """
    Extract metadata from a URL (meta tags, OpenGraph, etc.)
    
    Args:
        url (str): The URL to extract metadata from
        
    Returns:
        Dict[str, str]: Dictionary containing metadata
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        metadata = {}
        
        # Get meta tags
        for meta in soup.find_all('meta'):
            name = meta.get('name') or meta.get('property')
            content = meta.get('content')
            if name and content:
                metadata[name] = content
                
        # Get OpenGraph tags
        og_tags = {}
        for meta in soup.find_all('meta', property=re.compile(r'^og:')):
            og_tags[meta['property']] = meta['content']
            
        if og_tags:
            metadata['og'] = og_tags
            
        return metadata
    except requests.RequestException as e:
        return {'error': str(e)} 