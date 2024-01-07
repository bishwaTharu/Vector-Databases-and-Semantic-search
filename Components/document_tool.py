from langchain.text_splitter import  RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader 
from langchain_community.document_loaders import TextLoader


def load_and_split(path:str,chunk_size:int , chunk_overlap:int):
    """
    load the directory and split the data in chunks 
    path: path of directory 
    chuck_size: int
    chuck_overlab: int
    """
    text_loader_kwargs={'autodetect_encoding': True}
    loader = DirectoryLoader(path, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs,use_multithreading=True,show_progress=True)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs
