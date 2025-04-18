# retrieval.py
from crewai_tools import Tool
import chromadb

# Load the ChromaDB client and collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="university_manual")

# Define the function CrewAI can call
def chroma_search_tool(query: str) -> str:
    results = collection.query(query_texts=[query], n_results=3)
    documents = results['documents'][0]
    return "\n".join(documents)

# Wrap it in a CrewAI Tool
chroma_tool = Tool(
    name="University Manual Retriever",
    description="Useful for retrieving university information from the manual",
    func=chroma_search_tool
)
