from Components.docs_splitter import doc_Split 

with open("data/some_txt.txt") as f:
    some_txt = f.read()
print(some_txt)

rSplit_result, cSplit_result = doc_Split(chuck_size=100,chuck_overlab=50,documets=[some_txt],seperator=" ")
print(f'==============R_split======================\n {rSplit_result}')
print(f'===============c_split==================\n {cSplit_result}')