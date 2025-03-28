from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined responses for the chatbot
responses = {
    "hi": "Hi there! Thanks for visiting Sharon Dallas site, how can I help you?",
    "hello": "Hi there! Thanks for visiting Sharon Dallas site, how can I help you?",
    "Service times": "Our Sunday worship service starts at 10 am",
    "Address": "940 Barnes Bridge Rd, Mesquite, TX 75150",
    "bye": "Have a nice day! God Bless you",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message'].lower()  # Get the message from the user
    response_message = responses.get(user_message, "Sorry, I might not be able to answer that.")  # Get response from predefined responses
    return jsonify({'response': response_message})  # Return the response as JSON

if __name__ == '__main__':
    app.run(debug=True)
