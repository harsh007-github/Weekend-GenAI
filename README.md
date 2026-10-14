# 🚀 Weekend-GenAI

A collection of practical, production-ready Generative AI implementations built using the **Google Gemini API** and the **LangChain** framework. This repository showcases modular architectures for structured data parsing, dynamic multi-persona CLI agents, and Retrieval-Augmented Generation (RAG) pipelines.

---

## 📂 Project Architecture

```text
Weekend-GenAI/
├── resume_analyzer/        # Structured JSON evaluation of resumes vs. job descriptions
├── chatbot_cli/            # Persona-based interactive CLI chatbot with memory & resilience
└── semantic_pdf_search/    # RAG pipeline for high-performance semantic search over PDFs
```

---

## ✨ Features

### A. AI Resume Analyzer
An automated tool designed to evaluate a candidate's resume against a specific job description, providing actionable feedback and quantitative fit metrics.
* **Structured Output:** Leverages Pydantic models (`OutputSchema`) to enforce strict, reliable JSON-like responses from the LLM.
* **Comprehensive Metrics:** Computes a `Match_Score` (1-10) and extracts `Matching_Skills`, `Missing_Skills`, `Strengths`, and specific `Improvements`.
* **Tech Stack:** `langchain_google_genai` (Gemini 2.5 Flash), Pydantic, python-dotenv.

### B. ChatBot CLI
A flexible, resilient Command Line Interface (CLI) chatbot equipped with dynamic persona switching and conversation memory.
* **Dynamic Role Switching:** Seamlessly switch between professional personas including **Interviewer**, **Research Assistant**, **Summarizer**, and **AI Chat Bot**.
* **Conversation Memory:** Maintains state using `HumanMessage` and `AIMessage` history for fully context-aware interactions.
* **Built-in Resilience:** Implements `with_retry` strategies to handle Google API rate limits (`GoogleRateLimitError`) gracefully using exponential jitter.
* **Input Validation:** Custom validation lambdas prevent empty or whitespace-only queries.
* **Tech Stack:** `langchain_google_genai` (Gemini 2.5 Flash), `langchain_core` (Runnables, PromptTemplates).

### C. Semantic PDF Search
A robust Retrieval-Augmented Generation (RAG) implementation that enables natural language semantic queries over large PDF documents.
* **Optimized Ingestion Pipeline:** Utilizes `PyPDFLoader` for document ingestion and `RecursiveCharacterTextSplitter` for chunking (chunk size: 1000, overlap: 300).
* **Advanced Vector Embeddings:** Converts text chunks into vector representations using `GoogleGenerativeAIEmbeddings` (`gemini-embedding-001`).
* **High-Performance Retrieval:** Leverages **FAISS** (Facebook AI Similarity Search) as an in-memory vector database for fast similarity searches.
* **Batch Processing:** Handles large documents efficiently by processing pages in controlled batches to stay well within API limits.
* **Tech Stack:** FAISS, PyPDFLoader, GoogleGenerativeAIEmbeddings, langchain_text_splitters.

---

## 🛠️ Tech Summary

* **Primary LLMs:** Google Gemini 2.5 Flash / Gemini Embedding 001
* **Orchestration:** LangChain (LCEL - LangChain Expression Language)
* **Environment Management:** Python venv with `.env` configuration
* **Key Libraries:** `langchain`, `langchain-google-genai`, `pydantic`, `faiss-cpu`, `pypdf`

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Weekend-GenAI.git
cd Weekend-GenAI
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Alternatively, install the core packages manually: `pip install langchain langchain-google-genai pydantic faiss-cpu pypdf python-dotenv`)*

### 4. Configure Environment Variables
Create a `.env` file in the root directory of the project and add your Google Gemini API key:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

---

## 🚀 Usage Guide

### 1. Running the AI Resume Analyzer
Ensure your input files (`resume.json` and `job_description.json`) are placed in the appropriate directory, then run:
```bash
python -m resume_analyzer.main
```
The script will process the files through the structured Pydantic prompt and output a detailed JSON analysis report.

### 2. Running the ChatBot CLI
Launch the interactive CLI chatbot script:
```bash
python -m chatbot_cli.main
```
Follow the on-screen prompts to select your desired persona (Interviewer, Research Assistant, Summarizer, or AI Chat Bot) and begin chatting. Type `exit` or `quit` to end the session.

### 3. Running Semantic PDF Search
To ingest a PDF document and execute semantic queries against it:
```bash
python -m semantic_pdf_search.main --pdf path/to/your/document.pdf
```
You will be prompted to enter your natural language questions regarding the contents of the document.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
