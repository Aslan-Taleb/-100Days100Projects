import openai

# Get your API key by visiting the following link:
# "https://platform.openai.com/account/api-keys"
# Copy and paste your API key to replace "your-api-key" below

openai.api_key = "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"
messages = []

print("Welcome to The Assistant Generator!")
system_msg = input("Who do you want as your assistant today? ")
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant!")
while True:
    user_input = input("You: ")
    if user_input == "quit()":
        break
    
    # messages.append({"role": "user", "content": user_input})
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=messages
    # )
    # reply = response["choices"][0]["message"]["content"]
    # messages.append({"role": "assistant", "content": reply})
    # print("Assistant:", reply)
    print("""
    Welcome to The Assistant Generator!
Who do you want as your assistant today? John

Say hello to your new assistant!
You: How's the weather today?
Assistant: The weather is sunny and warm.

You: What are your favorite hobbies?
Assistant: I enjoy reading, playing chess, and going for long walks.

You: quit()
    
    
    
    
    
    """)
