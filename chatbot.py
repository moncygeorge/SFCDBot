from transformers import pipeline
# Initialize the pipeline for text generation
chatbot = pipeline("text-generation", model="distilgpt2")


def chat_with_gpt2(question):
    # Generate a response using GPT-2
    response = chatbot(question, max_length=50, temperature=0.3, num_return_sequences=1)

    # Extract and return the generated text
    return response[0]["generated_text"]


def start_chat():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        # Get user input
        user_input = input("You: ")

        # End the chat if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Generate and print the response
        response = chat_with_gpt2(user_input)
        print(f"Chatbot: {response}")


# Start the chatbot
start_chat()
