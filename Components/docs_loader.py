from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader


def load_db(path: str):
    """
    load the directory and split the data in chunks
    path: path of directory
    chuck_size: int
    chuck_overlab: int
    """
    text_loader_kwargs = {"autodetect_encoding": True}
    loader = DirectoryLoader(
        path,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs=text_loader_kwargs,
        use_multithreading=True,
        show_progress=True,
    )
    documents = loader.load()
    return documents
