
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="AI Study Assistant",
    layout="centered"
)

st.title("AI Study Assistant")
st.write("Your personal AI assistant for learning and exam preparation.")

if not api_key:
    st.error("Groq API key not found. Please add it to your .env file.")
    st.stop()

client = Groq(api_key=api_key)

# Select functionality
task = st.selectbox(
    "Choose what you want to do",
    [
        "Explain a Topic",
        "Generate Revision Notes",
        "Generate Exam Questions",
        "Summarize Text"
    ]
)

topic = st.text_input("Enter your topic")

content = st.text_area(
    "Enter text here (required only for summarization)",
    height=150
)

if st.button("Generate", type="primary"):

    if task == "Summarize Text":
        if not content.strip():
            st.warning("Please enter some text to summarize.")
            st.stop()

        prompt = f"""
        Summarize the following text in simple language.
        Include the important points.

        Text:
        {content}
        """

    else:
        if not topic.strip():
            st.warning("Please enter a topic.")
            st.stop()

        if task == "Explain a Topic":
            prompt = f"Explain {topic} in simple language with examples."

        elif task == "Generate Revision Notes":
            prompt = f"Generate clear and concise revision notes on {topic}."

        elif task == "Generate Exam Questions":
            prompt = f"""
            Generate 10 important exam questions about {topic}.
            Include answers after the questions.
            """

    try:
        with st.spinner("AI is generating your response..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful study assistant. Give accurate, clear and beginner-friendly answers."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_completion_tokens=1500,
                temperature=0.5
            )

            answer = response.choices[0].message.content

        st.subheader("AI Generated Result")
        st.markdown(answer)

    except Exception as e:
        st.error(f"Something went wrong: {e}")

st.divider()
st.caption("Built using Python, Streamlit and Groq API.")
