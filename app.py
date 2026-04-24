from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import faiss, pickle, numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os

app = FastAPI(title="Nafa.ai RAG API Service")

index = faiss.read_index("faiss_index_file.idx")
with open("faiss_metadata_file.pkl", "rb") as f:
    metadata = pickle.load(f)

sentence_model = SentenceTransformer("all-MiniLM-L6-v2")

# Setup Gemini
gemini_api_key = 'AIzaSyDxdEN-lae6__1JESazjiW7c27K2WeIzmE'
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")


class RiskRequest(BaseModel):
    risk: str  # Low, Moderate, or High


def embed_query(text: str):
    """Convert a query to a FAISS vector embedding."""
    vec = sentence_model.encode([text])
    vec = np.array(vec).astype("float32")
    faiss.normalize_L2(vec)
    return vec


def get_recommendations_for_risk(risk_level: str, top_k: int = 170):
    """Search the FAISS index for relevant companies given a risk profile."""
    query = f"best {risk_level.lower()} risk investment companies in Pakistan"
    qvec = embed_query(query)
    D, I = index.search(qvec, top_k)

    results = []
    for score, idx in zip(D[0], I[0]):
        item = metadata[idx]
        if str(item.get("RiskLevel", "")).lower() != risk_level.lower():
            continue
        item["_score"] = float(score)
        results.append(item)
    return results


def generate_summary(risk_level: str, recommendations: list):
    """Use Gemini to summarize or explain recommendations."""
    if not recommendations:
        return f"No recommendations found for {risk_level} risk investors."

    prompt = f"""
    You are a financial advisor for Pakistani retail investors.
    The user's risk profile is: {risk_level}.
    Below are recommended companies with their details.
    Please summarize key insights and mention 2-3 standout companies briefly.

    Recommendations:
    {recommendations[:10]}  # only a few top for context
    """

    response = gemini_model.generate_content(prompt)
    return response.text


@app.post("/recommend-by-risk")
def recommend_by_risk(req: RiskRequest):
    results = get_recommendations_for_risk(req.risk)
    summary = generate_summary(req.risk, results)
    return {
        "summary": summary,
        "recommendations": results
    }
