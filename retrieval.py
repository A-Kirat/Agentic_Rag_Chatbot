from crewai.tools import tool
import chromadb
from sentence_transformers import SentenceTransformer

# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB and get the collection
client = chromadb.Client()
collection = client.get_or_create_collection("university_manual")

@tool("Search University Manual")
def chroma_tool(question: str) -> str:
    """
    Searches the university manual in ChromaDB and returns the most relevant information.
    """
    # Embed the query
    query_embedding = model.encode([question])[0]

    # Query ChromaDB
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    documents = results.get("documents", [[]])[0]

    # Return top matches
    return "\n\n".join(documents) if documents else "No relevant content found."
