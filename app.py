import os
import streamlit as st
from dotenv import load_dotenv

# Try imports compatible with different langchain versions
try:
    from langchain_core.prompts import PromptTemplate
except Exception:
    from langchain_core.prompts import PromptTemplate

from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Read API key and validate
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("Missing GROQ_API_KEY. Add it to your .env file (GROQ_API_KEY=...).")
    st.stop()

# Initialize Groq model once
#lm = ChatGroq(api_key=groq_api_key, model="llama3-8b-8192", temperature=0.3)
llm = ChatGroq(api_key=groq_api_key, model="llama-3.3-70b-versatile", temperature=0.3)

# Streamlit UI setup
st.set_page_config(page_title="Text to SQL Query Tool", page_icon="🧾")
st.title("🧾 Text to SQL Query Helper Tool")
st.markdown(
    """
Convert natural language text into structured SQL queries effortlessly.  
Streamline your database interaction and data retrieval with AI-powered assistance.
"""
)

# Input area
user_text = st.text_area("Enter your question or request about the database:", height=150)

# SQL dialect selector
sql_dialect = st.selectbox(
    "Select SQL Dialect", ["Standard SQL", "MySQL", "PostgreSQL", "SQLite"], index=0
)

if st.button("Generate SQL Query") and user_text.strip():
    prompt_template = """
You are an expert SQL developer.

Convert the following natural language request into a {dialect} SQL query.
Only return the SQL query without any explanations.

Request:
{user_text}
"""
    prompt = PromptTemplate(input_variables=["dialect", "user_text"], template=prompt_template)
    prompt_text = prompt.format(dialect=sql_dialect, user_text=user_text)

    try:
        response = llm.invoke(prompt_text)
        # Response shape can vary — try common attributes, fallback to str()
        if hasattr(response, "content"):
            sql_query = response.content
        elif hasattr(response, "text"):
            sql_query = response.text
        else:
            sql_query = str(response)

        st.subheader("Generated SQL Query:")
        st.code(sql_query.strip(), language="sql")
    except Exception as e:
        st.error(f"Error generating SQL: {e}")
else:
    st.info("Enter a natural language request and click the button to generate the SQL query.")
