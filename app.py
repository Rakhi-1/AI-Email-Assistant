import streamlit as st
from google.genai import Client
client = Client(api_key=st.secrets["GEMINI_API_KEY"])
st.write("Generate professional emails using Gemini AI.")

email_type = st.selectbox(
    "Select Email Type",
    ["Professional", "Leave Request", "Apology", "Thank You", "Job Application"]
)

recipient = st.text_input("Recipient Name")
purpose = st.text_area("What do you want to say?")

if st.button("Generate Email"):

    prompt = f"""
Write a professional {email_type} email.

Recipient: {recipient}

Purpose:
{purpose}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    with st.spinner("Generating..."):
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
        )

    st.subheader("Generated Email")
    st.write(response.text)
