from transformers_js import pipeline
from pyodide.ffi import create_proxy, to_js
from js import document

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="Xenova/distilbert-base-sequence-classifier")

# Define a function to generate responses based on sentiment
def generate_response(sentiment):
    if sentiment == "POSITIVE":
        responses = [
            "That's great to hear!",
            "I'm glad you're feeling positive!",
            "Awesome!",
        ]
    elif sentiment == "NEGATIVE":
        responses = [
            "I'm sorry to hear that.",
            "That sounds tough.",
            "I hope things get better!",
        ]
    else:
        responses = [
            "Interesting!",
            "Tell me more.",
            "Okay.",
        ]
    return responses[0]

# Function to handle user input and generate AI response
def handle_user_input(event):
    user_input = document.getElementById("user_input").value
    
    # Perform sentiment analysis
    result = sentiment_pipeline(user_input, to_js(dict(truncation=True)))
    sentiment = result[0]["label"]
    
    # Generate AI response
    ai_response = generate_response(sentiment)
    
    # Display AI response
    document.getElementById("ai_response").innerText = ai_response

# Attach event listener to the send button
send_button = document.getElementById("send_button")
send_button.addEventListener("click", create_proxy(handle_user_input))
