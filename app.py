from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
load_dotenv()

model_openai = ChatOpenAI(model="gpt-4.1-nano",seed=6)
model_google = ChatGoogleGenerativeAI(model="gemini-2.5-flash",seed=6)

#resp1 = model_openai.invoke("We are building an AI system for processing medical insurance claims.")

#resp2 = model_openai.invoke("What are the main risks in this system?")

messages = [
    SystemMessage(content="You are a senior AI architect reviewing production systems."),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]

messages = model_openai.invoke(messages)

print(f"OpenAI response 1: {messages}")

"""
Reflection:

1. Why did string-based invocation fail?
Each invoke() call is stateless. The second question said "this system" but the model had no idea what that referred to, since the first call wasn't passed along. So it just guessed.
2. Why does message-based invocation work?
Because we pass the full chat history (Human + AI messages) every time. The model sees the prior turn, so "this system" now clearly means the medical insurance claims AI.
3. What breaks in production if we ignore message history?
The assistant feels forgetful and incoherent. Follow-ups lose meaning, answers contradict earlier ones, multi-turn flows (like claim intake or escalation) fall apart, and the model hallucinates context to fill the gap — risky in healthcare. Basically, no memory = no real conversation.
"""
