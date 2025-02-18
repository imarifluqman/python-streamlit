import streamlit as st
import random

# Initialize game state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 25)
    st.session_state.attempts = 0
    st.session_state.message = "Guess a number between 1 and 25!"

# Function to check guess
def check_guess(guess):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.session_state.message = "🔼 Too low! Try again."
    elif guess > st.session_state.secret_number:
        st.session_state.message = "🔽 Too high! Try again."
    else:
        st.session_state.message = f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts."
        st.session_state.secret_number = random.randint(1, 25)
        st.session_state.attempts = 0  # Reset game

# Streamlit UI
st.title("🎯 Number Guessing Game")

st.write(st.session_state.message)

guess = st.number_input("Enter your guess:", min_value=1, max_value=25, step=1)

if st.button("Submit Guess"):
    check_guess(guess)
    st.rerun()
