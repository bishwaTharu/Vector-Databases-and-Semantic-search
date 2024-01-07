from Components.docs_splitter import doc_Split 

with open("data/some_txt.txt") as f:
    some_txt = f.read()
print(type(some_txt))

rSplit_result, cSplit_result = doc_Split(chuck_size=1000,chuck_overlab=150,documets=[some_txt],seperators=["\n\n", "\n", " ", ""])
print(f'==============R_split======================\n {rSplit_result.split_text(some_txt)}')
print(f'==============R_split length======================\n {len(rSplit_result.split_text(some_txt))}')
print(f'==============0_split length======================\n {rSplit_result.split_text(some_txt)[0]}')
# print(f'===============c_split==================\n {cSplit_result.split_text(some_txt)}')