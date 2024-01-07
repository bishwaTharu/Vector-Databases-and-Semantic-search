from Components.docs_splitter import doc_Split 
from Components.docs_loader import load_db

documents = load_db(path="./data")
rSplit_result, cSplit_result = doc_Split(chuck_size=300,chuck_overlab=50,documets=documents,seperators=["\n\n\n", "\n", " ", ""])

print(f'==============R_split length======================\n {len(rSplit_result.split_documents(documents))}')
print(f'==============0_split item======================\n {rSplit_result.split_documents(documents)[0]}')