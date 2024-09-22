
import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client('ZHaOY2n1fbGF342yisQKgq3coGFZvGMIcL8DBjPy')  # Replace with your Cohere API key

# Pricing logic
MIN_PRICE = 100
MAX_PRICE = 500


# Function to handle pricing negotiation
def handle_negotiation(user_offer):
    if user_offer >= MIN_PRICE and user_offer <= MAX_PRICE:
        return f"Accepted! Your offer of {user_offer} is within the acceptable range."
    elif user_offer < MIN_PRICE:
        counter_offer = MIN_PRICE + 20  # Raise the counteroffer above the minimum
        return f"Too low! How about a counteroffer of {counter_offer}?"
    else:
        return f"Too high! We cannot accept offers above {MAX_PRICE}."

# Function to generate chatbot responses using Cohere
def generate_response(prompt):
    try:
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=500
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Streamlit app setup
st.title("Negotiation Chatbot")
st.write("Start negotiating the price for a product. Enter your price offer!")

# Initial price offered by the bot
bot_initial_offer = 400
st.write(f"Bot's initial offer: {bot_initial_offer}")

# User input for price negotiation
user_offer = st.number_input("Enter your price offer:", min_value=50, max_value=600, step=10)

if st.button("Submit Offer"):
    negotiation_result = handle_negotiation(user_offer)
    st.write(f"Bot's response: {negotiation_result}")

# Additional chatbot conversation (optional)
st.write("You can also talk to the bot below:")
user_message = st.text_input("Enter your message to the bot:")

if st.button("Send Message"):
    if user_message.strip():  # Check if the input is not empty
        bot_response = generate_response(user_message)
        st.write(f"Bot's response: {bot_response}")
    else:
        st.write("Please enter a valid message.")
