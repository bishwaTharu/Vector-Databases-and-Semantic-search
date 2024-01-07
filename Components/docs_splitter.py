from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from typing import Any

def doc_Split(chuck_size:int, chuck_overlab:int,seperators:Any,documets:Any):
    r_splitter = RecursiveCharacterTextSplitter(chunk_size=chuck_size,chunk_overlap=chuck_overlab,separators=seperators)
    c_splitter = CharacterTextSplitter(chunk_size=chuck_size,chunk_overlap=chuck_overlab,separator=seperators)
    r_docs = r_splitter.split_documents(documents=documets)
    c_docs = c_splitter.split_documents(documents=documets)
    return r_docs,c_docs

# [Test]


