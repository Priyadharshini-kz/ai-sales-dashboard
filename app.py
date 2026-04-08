import streamlit as st
import pandas as pd
import requests

# 📂 Load CSV
df = pd.read_csv("Burger_Point.csv")

st.title("🍔 Local AI Sales Dashboard")

# Show data
st.write("### 📊 Data Preview")
st.dataframe(df)

# ---------------- AI FUNCTION ---------------- #
def ask_local_llm(prompt):
    response = requests.post(
        "https://monique-courtlier-nonbarbarously.ngrok-free.dev/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# ---------------- USER INPUT ---------------- #
st.write("## 🤖 Ask Questions")

user_question = st.text_input("Ask something like: Top item? Total revenue?")

# ---------------- RESPONSE ---------------- #
if user_question:
    prompt = f"""
    You are a data analyst.

    Dataset:
    {df.to_string()}

    Question:
    {user_question}

    Give a clear answer.
    """

    answer = ask_local_llm(prompt)

    st.write("### 🧠 Answer")
    st.write(answer)
