import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.title("LAWS 90286 - D1")
st.header("Part 1 - Get Name")
name = st.text_input("What is your name?")
age = st.number_input("What is your age?")

user_info = {"name": name, "age": age}

if st.button("Submit"):
    st.write(f"Welcome, {user_info['name']}!")
    if user_info["age"] <= 24:
        st.write("You were born this millennium")
    else:
        st.write("You were born last millennium")

st.header("Part 2 - Ask OpenAI")
client = OpenAI()
response = client.responses.create(
    model="gpt-4o",
    input="Write a short poem about a unicorn.",
)

st.write(response.output_text)


topic = st.text_input("What should the poem be about?")
if st.button("Generate Poem"):
    response = client.responses.create(
        model="gpt-4o",
        input=f"Write a short poem about {topic}.",
    )
    st.write(response.output_text)