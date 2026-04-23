import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
from google import genai

# Load env
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Embedding model (local)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
index = None

def load_documents():
    global documents

    with open("knowledge_base.json") as f:
        data = json.load(f)

    documents = [
        "Basic Plan: $29/month, 10 videos/month, 720p resolution",
        "Pro Plan: $79/month, unlimited videos, 4K resolution, AI captions",
        "No refunds after 7 days",
        "24/7 support only for Pro plan"
    ]

def build_index():
    global index

    load_documents()

    embeddings = embedder.encode(documents)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

def retrieve_answer(query):
    global index

    query_embedding = embedder.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k=2)

    context = "\n".join([documents[i] for i in indices[0]])


    if "price" in query.lower() or "plan" in query.lower():
        return context

    # Gemini call (only when needed)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are an AI assistant for AutoStream.

Use ONLY the context below:

{context}

Answer the question clearly.

Question: {query}
"""
    )

    return response.text