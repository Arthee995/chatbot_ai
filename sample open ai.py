# import openai

# openai.api_key = ""

# try:
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": "Hello"}],
#     )
#     print("✅ API Key is working!")
#     print("AI says:", response['choices'][0]['message']['content'])

# except openai.error.AuthenticationError:
#     print("❌ Invalid API Key!")
# except openai.error.RateLimitError:
#     print("⚠️ API Key is valid, but rate-limited or out of credits.")
# except Exception as e:
#     print(f"⚠️ Unexpected error: {e}")


# import openai
# import json


# openai.api_key = ""


# # # Initialize conversation history
# # messages = [
# #     {"role": "system", "content": "You are a helpful assistant."}
# # ]

# system_prompt = (
#     "You are a JSON-only assistant. "
#     "You must always respond using JSON format like this: "
#     '{ "reply": "your answer here" }. '
#     "Do not include any explanations or extra text."
# )

# # Set system message
# messages = [{"role": "system", "content": system_prompt}]

# print("🧠 JSON-Only AI Chatbot is ready. Type 'exit' to quit.\n")

# while True:
#     user_input = input("👤 You: ")
    
#     if user_input.lower() == "exit":
#         print("👋 Goodbye!")
#         break

#     # Add user's message to history
#     messages.append({"role": "user", "content": user_input})

#     try:
#         # Get AI response
#             parsed = json.loads(reply_raw)
#             print(f"🤖 AI (JSON): {parsed['reply']}\n")
#     except Exception:
#             print("⚠️ The AI did not return valid JSON:")
#             print(reply_raw)

#     messages.append({"role": "assistant", "content": reply_raw})

    
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

# Set your API key
os.environ["OPENAI_API_KEY"] = ""
# Create memory
memory = ConversationBufferMemory()

# Initialize model
llm = ChatOpenAI(temperature=0)

# Create conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Interact with the bot
while True:
    user_input = input("👤 You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break
    response = conversation.predict(input=user_input)
    print(f"🤖 AI: {response}\n")

