import streamlit as st
from spam_predict import predict_spam

st.set_page_config(page_title="Email Spam Detection", page_icon="📧")

st.title("📧 Email Spam Detection")
st.write("Enter email text below and check if it is spam or not.")

email = st.text_area("Email Text", height=150)

if st.button("Check Spam"):
    if email.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        result = predict_spam(email)

        if result == 1:
            st.error(" This Email is SPAM")
        else:
            st.success(" This Email is NOT Spam")
