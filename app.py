
import streamlit as st
import random

def main():
    st.title("🌱 Growth Mindset Challenge")
    st.write("Believe in your ability to learn and grow!")

    # Motivational Quote Generator
    quotes = [
        "Mistakes are proof that you are trying.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "A challenge only becomes an obstacle when you bow to it.",
        "Hard work beats talent when talent doesn’t work hard.",
        "Your potential is endless, keep growing!"
    ]
    
    if st.button("Get Inspired 💡"):
        st.write(random.choice(quotes))
    
    # User Reflection
    st.subheader("📝 Share Your Growth Mindset Experience")
    user_input = st.text_area("What challenge did you overcome today?", "")
    if st.button("Submit"):
        if user_input:
            st.success("Great! Keep growing! 🚀")
        else:
            st.warning("Please share your experience before submitting.")
    
    # Interactive Progress Tracker
    st.subheader("📈 Track Your Progress")
    progress = st.slider("How would you rate your growth mindset today?", 0, 100, 50)
    st.write(f"You're at {progress}% of your growth journey!")

if __name__ == "__main__":
    main()
