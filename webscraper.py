import dotenv
dotenv.load_dotenv()
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_nhs_search():
    from langchain.document_loaders import AsyncChromiumLoader
    from langchain.document_transformers import BeautifulSoupTransformer

    # Load HTML
    loader = AsyncChromiumLoader(["https://www.wsj.com"])
    html = loader.load()


if __name__ == "__main__":
    call_nhs_search()