# AutoStream AI Agent – Social-to-Lead Workflow

## 🚀 Overview
This project implements a Conversational AI Agent for **AutoStream**, a SaaS platform for automated video editing. The agent can understand user intent, answer product-related queries using Retrieval-Augmented Generation (RAG), identify high-intent users, and capture leads through a tool execution workflow.

---

## ⚙️ How to Run the Project Locally

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd autostream-agent
```
### 2. Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```
#### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Setup Environment Variables
Create a .env file in the root directory:
```
GOOGLE_API_KEY=your_api_key_here
```
### 5. Run the Application
```
python main.py
```
---
## 🧠 Architecture Explanation

This project uses a modular architecture combining rule-based logic, vector search, and LLM reasoning.

Instead of using LangGraph, a lightweight custom agent pipeline was implemented to maintain simplicity while still fulfilling the assignment requirements. State is managed using a dictionary within the agent, which tracks conversation stages such as name, email, and platform across multiple turns, ensuring continuity.

For knowledge retrieval, a Retrieval-Augmented Generation (RAG) pipeline is used. The knowledge base is embedded using the **all-MiniLM-L6-v2** model from SentenceTransformers, and FAISS is used for efficient vector similarity search. When a user asks a question, the system retrieves the most relevant context and passes it to the Gemini model for response generation.

Intent detection is handled using a rule-based approach to reduce API calls and improve performance. This hybrid design ensures efficiency, scalability, and real-world applicability.

---

## 📲 WhatsApp Integration (Using Webhooks)

To integrate this agent with WhatsApp, the WhatsApp Business API can be used along with a backend server (e.g., Flask or FastAPI).

1. A webhook endpoint is created to receive incoming WhatsApp messages.  
2. When a user sends a message, WhatsApp forwards it to the webhook.  
3. The backend extracts the message and passes it to the AutoStream agent.  
4. The agent processes the input (intent detection → RAG → response).  
5. The response is sent back to the user via the WhatsApp API.  

This setup enables real-time, automated conversational interactions and can be deployed on cloud platforms for scalability.

---

## ✅ Features

- Intent Detection (Greeting, Pricing, High Intent)  
- RAG-based Knowledge Retrieval  
- Stateful Multi-turn Conversation  
- Lead Capture Tool Execution  
- Modular and Scalable Design  

---

## 🎯 Evaluation Criteria Covered

- ✔ Agent reasoning & intent detection  
- ✔ Correct use of RAG  
- ✔ Clean state management  
- ✔ Proper tool calling logic  
- ✔ Code clarity & structure  
- ✔ Real-world deployability  
