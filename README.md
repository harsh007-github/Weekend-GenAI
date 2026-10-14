# Weekend-GenAI 🚀

A collection of Generative AI utility tools built using Python and the LangChain framework, leveraging Google's Gemini models. This project demonstrates the practical application of Large Language Models (LLMs) in structured data analysis (Resume Analysis) and versatile conversational interfaces (ChatBot CLI).

## 📌 Introduction

`Weekend-GenAI` is designed to showcase modular GenAI engineering patterns. Whether you are automating complex recruitment workflows or building stateful conversational interfaces with role-switching capabilities, this repository provides clean, production-ready implementation examples using modern orchestration frameworks and Google's high-performance Gemini models.

## ✨ Features

### 🤖 AI Resume Analyzer

* **Structured Output:** Utilizes Pydantic schemas (`OutputSchema`) to force the LLM to return a precise JSON format containing `Matching_Skills`, `Missing_Skills`, `Strengths`, `Improvements`, and a `Match_Score` (1-10).
* **LLM Integration:** Powered by `ChatGoogleGenerativeAI` (Gemini Flash) via LangChain.
* **Deterministic Workflow:** Automatically reads `resume.json` and `job_description.json`, processes them through a `ChatPromptTemplate`, validates output via structured models, and prints a formatted evaluation report.

### 💬 ChatBot CLI

* **Dynamic Role Switching:** Allows users to dynamically switch agent personas (such as Interviewer, Research Assistant, Summarizer, or AI Chat Bot) during the session using simple commands.
* **Conversation Memory:** Maintains a robust session history (`chat_history`) of `HumanMessage` and `AIMessage` objects for contextual multi-turn conversations.
* **Robust Pipeline & Error Handling:** Implements LangChain Expression Language (LCEL) with input validation (`RunnableLambda`) and automatic retry logic (`with_retry`) to gracefully handle Google API rate limits (`GoogleRateLimitError`).

## 📂 Project Structure

```text
Weekend-GenAI/
├── AI Resume Analyzer/
│   ├── main.py             # Core logic for resume-job matching and structured reporting
│   ├── requirements.txt    # Dependencies for the analyzer
│   ├── resume.json         # Structured input containing candidate's profile, experience, and skills
│   └── job_description.json # Structured input containing job requirements and benefits
├── ChatBot CLI/
│   ├── main.py             # Interactive CLI chatbot with dynamic role switching and memory
│   └── requirements.txt    # Dependencies for the chatbot
└── README.md               # Project Documentation
```

## 🛠️ Tech Stack

* **Language:** Python
* **Orchestration:** LangChain (`langchain`, `langchain_core`)
* **LLM Provider:** Google Gemini (`langchain_google_genai`)
* **Data Validation:** Pydantic
* **Environment Management:** `python-dotenv`
* **Additional Libraries:** NumPy, Scikit-learn, Streamlit, HuggingFace Transformers

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher installed on your system.
* A valid Google Gemini API Key.

### Configuration

1. Create a `.env` file in the root directory or inside the respective tool folder.
2. Add your Google API key to the `.env` file:

```env
GOOGLE_API_KEY=your_actual_google_api_key_here
```

### Installation & Execution

#### 1. Running the AI Resume Analyzer

```bash
# Navigate to the analyzer directory
cd "AI Resume Analyzer"

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

#### 2. Running the ChatBot CLI

```bash
# Navigate to the chatbot directory
cd "ChatBot CLI"

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## 📊 Example Output

### AI Resume Analyzer

When executing the resume analyzer, you will receive a clean, structured output breakdown in your console:
* **Match Score:** A numerical rating from 1 to 10 indicating job fit.
* **Matching Skills:** A breakdown of overlapping tech stacks and proficiencies.
* **Missing Skills:** Key technical gaps identified between the candidate and the role requirements.
* **Strengths & Improvements:** Actionable insights outlining candidate advantages and areas for professional growth.

### ChatBot CLI

Upon launching the chatbot, you can interact continuously via the terminal, switch personas dynamically, and maintain conversational context across your dialogue turns.
```markdown
