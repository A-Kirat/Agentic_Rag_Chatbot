#Code to convert pdf to txt file

# #Converting the Pdf to text
# import sys, pathlib
# import pymupdf
# fname="C:/Ahmed/agentic_rag_chatbot/data/University_Manual.pdf" # file name
# with pymupdf.open(fname) as doc:  # open document
#     text = chr(12).join([page.get_text() for page in doc])
# # write as a binary file to support non-ASCII characters
# pathlib.Path(fname + ".txt").write_bytes(text.encode())
# text cleaning
import pandas as pd
import re
import string
import nltk
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import string
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Make sure NLTK resources are downloaded
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def clean_string(text, stem="None"):

    final_string = ""

    # Make lower
    text = text.lower()

    # Remove line breaks
    text = re.sub(r'\n', '', text)

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Tokenize
    text = text.split()

    # Remove stopwords
    useless_words = nltk.corpus.stopwords.words("english")
    useless_words = useless_words + ['hi', 'im']  # custom stopwords
    text_filtered = [word for word in text if word not in useless_words]

    # Remove numbers inside words
    text_filtered = [re.sub(r'\w*\d\w*', '', w) for w in text_filtered]

    # Stem or Lemmatize
    if stem == 'Stem':
        stemmer = PorterStemmer() 
        text_stemmed = [stemmer.stem(word) for word in text_filtered]

    elif stem == 'Lem':
        lemmatizer = WordNetLemmatizer()
        text_stemmed = [lemmatizer.lemmatize(word) for word in text_filtered]

    else:
        text_stemmed = text_filtered

    final_string = ' '.join(text_stemmed)

    return final_string
# === Load the .txt file ===
with open("data/University_Manual.pdf.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# === Clean the text ===
cleaned_text = clean_string(raw_text, stem="Lem")  # or "Stem" or "None"

# === Save cleaned text to a new file (optional) ===
with open("data/university_manual.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Done. Cleaned text saved to cleaned_file.txt")