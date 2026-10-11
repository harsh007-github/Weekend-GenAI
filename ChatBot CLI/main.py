from langchain_google_genai.chat_models import GoogleRateLimitError
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
# Validation function to validate empty and whitespaced inputs
def validate_input(input:dict):
    userInput = input.get("user_input")
    if not userInput:
        raise ValueError('Input message cannot be empty!')
    return input


# All the necessary runnables
# Model, model with retries on certain exceptions
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
robust_model = model.with_retry(
    stop_after_attempt=4,
    retry_if_exception_type=(GoogleRateLimitError),
    # Increases wait time after each retry exponentially
    wait_exponential_jitter=True
)

# Converts output to simple python strings
parser = StrOutputParser()

# Runnables chained together
chain = RunnableLambda(validate_input) | template | robust_model | parser


roles = ['Interviewer', 'Research Assistant', 'Summarizer', 'AI Chat Bot']
# Template for the prompts
template = ChatPromptTemplate([
    ('system', 'You are a helpful and expert {role}'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{user_input}'),
])

# history
chat_history = []

# Menu
print(" Available Roles: ")
print(f"{roles}")
selected_role = input("Select a Role: ")
print(f"Chat Session Started (Role: {selected_role})")
print("Type 'exit' or 'quit' to end the session.\n")
print("Type 'role' to change the system role.\n")

# Chat Loop
while True:
    user_input = input('Task: ')

    if user_input.lower() in ['exit', 'quit']:
        break

    if  user_input.lower() == 'role':
        print(" Available Roles: ")
        print(f"{roles}")
        selected_role = input("Select a Role: ")
        print(f"Chat Session Started (Role: {selected_role})")
        continue

    try:
        response = chain.invoke({
            "role": selected_role,
            "chat_history": chat_history,
            "user_input": user_input,
        })
    except ValueError as v:
        print(f"Error:{v}")
        continue
    except Exception as e:
        print(f"API Error {e}")
        break   
    
    print(f'AI: {response}\n')
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response))

print('\nChat History:\n', chat_history)
print("Session Ended")