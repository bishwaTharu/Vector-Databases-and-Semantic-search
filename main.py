import os
import pinecone
from dotenv import load_dotenv, find_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone
from Components.docs_loader import load_db
from langchain.embeddings import HuggingFaceInstructEmbeddings


load_dotenv(find_dotenv())

PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV,
)

## Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



embeddings_1 = HuggingFaceInstructEmbeddings(
    model_name='hkunlp/instructor-large',
    encode_kwargs={'normalize_embeddings': True},
    query_instruction="Represent the query for retrieval: "
)

# # document loading
docs = load_db(path="./data")

# data splitting 
# split here

docsearch = Pinecone.from_documents(docs, embeddings_1, index_name="llama-2")

while True:
    try:
        question = input("Query: ")
        results = docsearch.similarity_search_with_score(question, k=1)

        for doc in results:
            content, score = doc
            print(f"===========Content===========: {content}")
            print(f"===============Score==========: {score}")
    except KeyboardInterrupt:
        break
