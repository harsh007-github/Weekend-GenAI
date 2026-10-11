# Weekend-GenAI

A Python-based CLI Chatbot application built with **LangChain** and powered by the **Google Gemini API**. This project allows users to interact with an AI assistant while dynamically switching between specialized **Expert Roles** (such as Interviewer, Research Assistant, and Summarizer) to alter the assistant's persona and behavior.

---

## 💻 Tech Stack & Dependencies

- **Language:** Python
- **LLM Provider:** Google Gemini (`gemini-2.5-flash`)
- **Orchestration:** LangChain (`langchain`, `langchain_core`, `langchain_google_genai`)
- **Configuration:** `python-dotenv`

---

## ⚙️ Key Implementation Details

- **Dynamic Role Prompting:** Leverages `ChatPromptTemplate` with system prompt injection (`"You are a helpful and expert {role}"`) to seamlessly switch agent behaviors.
- **Conversation Memory:** Maintains an interactive local `chat_history` list using LangChain's `HumanMessage` and `AIMessage` objects for multi-turn conversational context.
- **API Resilience:** Implements `.with_retry()` configuration targeting `GoogleRateLimitError` with exponential backoff jitter to handle quota constraints gracefully.
- **Input Validation:** Utilizes `RunnableLambda` to filter out empty or whitespace-only inputs before hitting the API.
- **Execution Pipeline:** 
  $$\text{Input Validation} \rightarrow \text{Prompt Template} \rightarrow \text{Robust Gemini Model} \rightarrow \text{String Parsing}$$

---

## 📁 Project Structure

```text
Weekend-GenAI/
├── main.py             # Primary entry point, role switcher, chat loop, and LangChain pipeline
├── requirements.txt    # Dependency definitions (LangChain, transformers, scikit-learn, etc.)
└── .env                # Environment variables (GOOGLE_API_KEY)