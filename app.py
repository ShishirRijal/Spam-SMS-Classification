import streamlit as st
import pickle
from utils.preprocess import preprocess

tfidf = pickle.load(open('./model/vectorizer.pkl', 'rb'))
model = pickle.load(open('./model/model.pkl', 'rb'))

st.title("E-mail Spam Classifier")

input_sms = st.text_input("Enter the message here...")

if st.button("Predict", type="primary"):
    # 1. Preprocess
    cleaned_sms = preprocess(input_sms)

    # 2. Vectorize
    vector_input = tfidf.transform([cleaned_sms])

    # 3. Predict
    prediction = model.predict(vector_input)[0]

    # 4. Display result
    if prediction == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")



