from config import DATA_DIR
import pandas as pd
from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

xls = pd.ExcelFile(DATA_DIR / "enterprise-attack-v18.1.xlsx")

docs = []

for sheet in xls.sheet_names:
    df = xls.parse(sheet)
    
    for _, row in df.iterrows():
        content = f"Sheet: {sheet}\n"
        content += "\n".join([f"{col}: {row[col]}" for col in df.columns])
        
        docs.append(Document(page_content=content, metadata={"sheet": sheet}))

# print(docs[0])
# print(len(docs))

# print(docs[1000].page_content)
# print(docs[1000].metadata)




text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
texts = text_splitter.create_documents([docs])
print(texts[0])
print(texts[1])