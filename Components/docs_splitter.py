from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from typing import Any, Optional

def doc_Split(chuck_size:int, chuck_overlab:int,seperator:Optional[str],documets:Any):
    r_splitter = RecursiveCharacterTextSplitter(chunk_size=chuck_size,chunk_overlap=chuck_overlab,separators=seperator)
    c_splitter = CharacterTextSplitter(chunk_size=chuck_size,chunk_overlap=chuck_overlab,separator=seperator)
    r_docs = r_splitter.split_documents(documents=documets)
    c_docs = c_splitter.split_documents(documents=documets)
    return r_docs,c_docs

# [Test]


