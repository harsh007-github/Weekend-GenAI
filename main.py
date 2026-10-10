from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

roles = ['Interviewer', 'Research Assistant', 'Summarizer', 'AI Chat Bot']
selected_role = roles[1]  

template = ChatPromptTemplate([
    ('system', 'You are a helpful and expert {role}'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{user_input}'),
])

chat_history = []

print(f"Chat Session Started (Role: {selected_role})")
print("Type 'exit' or 'quit' to end the session.\n")

while True:
    user_input = input('Task: ')
    if user_input.lower() in ['exit', 'quit']:
        break
    
    
    chain = template | model
    response = chain.invoke({
        "role": selected_role,
        "chat_history": chat_history,
        "user_input": user_input,
    })
    print(f'AI: {response.content}\n')
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))

print('\nChat History:\n', chat_history)
print("Session Ended")