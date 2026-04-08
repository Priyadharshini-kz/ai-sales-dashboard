import streamlit as st
import pandas as pd
import requests

# 📂 Load CSV
df = pd.read_csv("Burger_Point.csv")

st.title("🍔 Local Dashboard")

# Show data
st.write("### 📊 Data Preview")
st.dataframe(df)

# ---------------- AI FUNCTION ---------------- #
def ask_local_llm(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        # Debug (optional)
        st.write("🔍 Raw Response:", response.text)

        return response.json().get("response", "No response from model")

    except Exception as e:
        return f"❌ Error: {e}"

# ---------------- USER INPUT ---------------- #
st.write("## 🤖 Ask Questions")

user_question = st.text_input("Ask something like: Top item? Total revenue?")

# ---------------- RESPONSE ---------------- #
if user_question:
    prompt = f"""
    You are a data analyst.

    Dataset:
    {df.head(100).to_string()}

    Question:
    {user_question}

    Give a clear answer.
    """

    with st.spinner("Thinking... 🤔"):
        answer = ask_local_llm(prompt)

    st.write("### 🧠 Answer")
    st.write(answer)
