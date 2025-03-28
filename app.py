from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined responses for the chatbot
responses = {
    "hi": "Hi there! How can I help you?",
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "bye": "Goodbye! Have a nice day!",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message'].lower()  # Get the message from the user
    response_message = responses.get(user_message, "Sorry, I don't understand that.")  # Get response from predefined responses
    return jsonify({'response': response_message})  # Return the response as JSON

if __name__ == '__main__':
    app.run(debug=True)
