from langchain_ollama import OllamaLLM

chatbot_a = OllamaLLM(model="deepseek-r1:7b")
chatbot_b = OllamaLLM(model="deepseek-r1:7b")

conversation_history = ""
message_a = "How can one find a girlfriend? do not output chain of thoughts"

for turn in range(1):
    # Bot B responds to Bot A
    prompt_b = f"You are Chatbot B, a scientist who follows Richard Feynman's approach. Respond to Chatbot A's statement in a scientific way. do not output chain of thoughts\n\nConversation so far:\n{conversation_history}\n\nChatbot A: {message_a}\nChatbot B:"
    response_b = chatbot_b.invoke(prompt_b)
    print(f"\n[Bot B] {response_b}")

    # Update conversation history
    conversation_history += f"\nChatbot A: {message_a}\nChatbot B: {response_b}"

    # Bot A responds to Bot B
    prompt_a = f"You are Chatbot A, a philosopher who follows Martin Heidegger's ideas. Respond to Chatbot B's statement in a philosophical way. do not output chain of thoughts\n\nConversation so far:\n{conversation_history}\n\nChatbot A:"
    response_a = chatbot_a.invoke(prompt_a)
    print(f"[Bot A] {response_a}")

    # Update conversation history
    conversation_history += f"\nChatbot A: {response_a}"

    # Set next message
    message_a = response_a

# Store the final conversation in a text file
with open(r"D:\response\conversation1.txt", "w", encoding="utf-8") as file:
    file.write(conversation_history)
