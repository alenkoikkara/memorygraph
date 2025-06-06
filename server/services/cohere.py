import cohere
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Cohere API key from environment
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY environment variable is not set")

co = cohere.ClientV2(COHERE_API_KEY)

def generate_keywords(text: str) -> dict:
    response = co.generate(
        model="command-r-plus",
        prompt=f"""You are a helpful assistant that generates keywords, title and a summary for a given text. 
          The summary should be a brief summary of the text.
        The keywords should be a list of keywords that are relevant to the text.
        The title should be a concise, descriptive title (maximum 10 words) for the text.
        Please provide the output in the following exact JSON format:
        {{
            "summary": "a brief summary of the text",
            "keywords": ["keyword1", "keyword2", "keyword3"],
            "title": "a concise, descriptive title (maximum 10 words) for the text"
        }}
        
        The text to process is: {text}
        
        Remember to only output the JSON object, nothing else.""",
        max_tokens=1000,
    )
    try:
        # Get the generated text and parse it as JSON
        generated_text = response.generations[0].text.strip()
        result = json.loads(generated_text)
        return result
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Generated text: {generated_text}")
        # Return a default response in case of parsing error
        print(f"Error: {e}")

def generate_embedding(text: str) -> list[float]:
    response = co.embed(
        texts=[text],
        model="embed-v4.0",
        input_type="classification",
        embedding_types=["float"],
        output_dimension=512,
      )
    return response.embeddings.float[0]
