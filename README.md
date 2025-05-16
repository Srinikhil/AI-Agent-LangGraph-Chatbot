cat > README.md << 'EOF'
# 🤖 AI Agent LangGraph Chatbot

An intelligent agent-powered chatbot API built using **LangGraph**, **Groq LLMs**, and **FastAPI**, enhanced with real-time search using **TavilySearchResults**. Supports multiple large models such as LLaMA 3, Mixtral, and Gemma.

🔗 **Live Repo:** [github.com/Srinikhil/AI-Agent-LangGraph-Chatbot](https://github.com/Srinikhil/AI-Agent-LangGraph-Chatbot/)

---

## � Features

- 🌐 FastAPI backend for handling chat requests
- 🧠 Agent-based reasoning via `LangGraph`'s ReAct pattern
- 🔍 Integrated web search using `TavilySearchResults`
- 🔄 Supports multiple LLMs via `Groq`:
  - `llama3-70b-8192`
  - `distil-whisper-large-v3-en`
  - `gemma2-9b-it`
  - `mixtral-8x7b-32768`
- 📡 API-first design for frontend or app integrations

---

## 🧠 Models Supported

| Model Name                   | Description                             |
|------------------------------|-----------------------------------------|
| `llama3-70b-8192`            | Meta's latest high-accuracy LLM         |
| `distil-whisper-large-v3-en` | Efficient speech recognition (English)  |
| `gemma2-9b-it`               | Fine-tuned conversational model         |
| `mixtral-8x7b-32768`         | Sparse Mixture-of-Experts model         |

---

## 🔐 Setup

1. Clone the repo:
```bash
git clone https://github.com/Srinikhil/AI-Agent-LangGraph-Chatbot.git
cd AI-Agent-LangGraph-Chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add API keys in app.py:

```python
groq_api_key = 'your_groq_api_key_here'
os.environ["TAVILY_API_KEY"] = 'your_tavily_api_key_here'
```

4. Run
```bash
uvicorn app:app --reload
# API at: http://127.0.0.1:8000/chat
```

5. Run UI
```bash
streamlit run UI.py
```
