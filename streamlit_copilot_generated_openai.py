# create a streamlit app that connects to the openai api and returns the generated text
import streamlit as st
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("OpenAI GPT-3 Demo")

prompt = st.text_area("Enter a prompt for GPT-3 to complete", "The dog is cute because")

max_tokens = st.slider("Maximum number of tokens to generate", 1, 100, 50)

temperature = st.slider("Temperature", 0.0, 1.0, 0.5)

frequency_penalty = st.slider("Frequency Penalty", 0.0, 1.0, 0.0)

presence_penalty = st.slider("Presence Penalty", 0.0, 1.0, 0.0)

stop = st.text_input("Stop Sequence", ".")

response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
    stop=stop,
)

st.write(response.choices[0].text)