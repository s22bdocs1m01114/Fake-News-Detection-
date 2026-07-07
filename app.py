import streamlit as st
import joblib
import os

# Load models at the start (outside functions)
@st.cache_resource
def load_models():
    try:
        # Adjust paths as needed
        vector = joblib.load('tfidf_vectorizer.pkl')
        model = joblib.load('fake_news_model.pkl')
        return vector, model
    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}")
        return None, None

# Load models once
vector, model = load_models()

# Check if models loaded successfully
if vector is None or model is None:
    st.error("Failed to load models. Please check model files.")
    st.stop()

def prediction(input_text):
    # Now vector is guaranteed to not be None
    input_data = vector.transform([input_text])
    result = model.predict(input_data)
    return result

# Your Streamlit UI
st.title("Fake News Detection")

input_text = st.text_area("Enter news article text:")
if st.button("Predict"):
    if input_text:
        Pred = prediction(input_text)
        if Pred[0] == 1:
            st.error("This is Fake News!")
        else:
            st.success("This is Real News!")
    else:
        st.warning("Please enter some text!")