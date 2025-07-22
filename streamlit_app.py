import streamlit as st
from code_review_ai.core import review_code

st.set_page_config(page_title="Code Review AI", layout="wide")
st.title("🤖 AI Code Reviewer")

code = st.text_area("Paste your code below:", height=300)

if st.button("Review Code"):
    if code.strip():
        with st.spinner("Reviewing your code..."):
            review = review_code(code)
            st.success("Review Complete")
            st.text_area("Review Result:", review, height=300)
    else:
        st.warning("Please paste some code before reviewing.")
