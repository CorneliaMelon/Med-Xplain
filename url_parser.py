import dotenv

dotenv.load_dotenv()
import os
import openai

import pprint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.chains import create_extraction_chain
from langchain.chat_models import ChatOpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

# Schema is essential for deciding the best information to provide for the user
schema = {
    "properties": {
        "article_title": {"type": "string"},
    },
    "required": ["article_title"],
}


def extract(content: str, schema: dict):
    return create_extraction_chain(schema=schema, llm=llm).run(content)


###############
# This function returns the relevant information from URLs
# Input: list of URLs ; dictionary (SCHEMA)
# Output: list of relevant information
###############
def scrape_with_playwright(urls, schema):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(docs, tags_to_extract=["span"])
    print("Extracting content with LLM")

    # Grab the first 1000 tokens of the site
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000,
                                                                    chunk_overlap=0)
    splits = splitter.split_documents(docs_transformed)

    extracted_content = []

    # Process splits
    for split in splits:
        try:
            split_content = extract(
                schema=schema, content=split.page_content
            )
            pprint.pprint(split_content)
            extracted_content.append(split_content)
        except:
            print("Error with url. Moving to next url")
            continue

    return extracted_content


urls = ["https://www.nhs.uk/conditions/lung-cancer/", "https://www.nhs.uk/conditions/lung-cancer/treatment/",
        "https://www.nhs.uk/conditions/lung-cancer/symptoms/"]
try:
    extracted_content = scrape_with_playwright(urls, schema=schema)
except Exception as e:
    print("Error with url")
