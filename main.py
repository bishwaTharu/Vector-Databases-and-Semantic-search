import os
import pinecone
from dotenv import load_dotenv, find_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone
from Components.document_tool import load_and_split


load_dotenv(find_dotenv())

PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV,
)

## Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# # document loading
docs = load_and_split(path="./data",chunk_size=1000,chunk_overlap=150)

docsearch = Pinecone.from_documents(docs, embeddings, index_name='llama-2')

while True:
    try:
        question = input("Query: ")
        results = docsearch.similarity_search_with_score(question, k=1)

        for doc in  results:
            content, score = doc
            print(f'===========Content===========: {content}')
            print(f'===============Score==========: {score}')
    except KeyboardInterrupt:
        break