#Code to convert pdf to txt file
fname="C:/Ahmed/agentic_rag_chatbot/data/University_Manual.pdf" # file name
#Converting the Pdf to text
import sys, pathlib
import pymupdf
with pymupdf.open(fname) as doc:  # open document
    text = chr(12).join([page.get_text() for page in doc])
# write as a binary file to support non-ASCII characters
pathlib.Path(fname + ".txt").write_bytes(text.encode())
print("done")