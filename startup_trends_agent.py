import os
import streamlit as st
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper import NewspaperTools

load_dotenv()

# Set up the Grok model with API key from .env
# Ensure GROK_API_KEY is set in .env file
api_key = os.getenv("GROK_API_KEY")
if not api_key:
    st.error("GROK_API_KEY not found in .env file. Please add it.")
    st.stop()

model = Groq(id="llama-3.3-70b-versatile", api_key=api_key, temperature=0)

# Create the agent with free tools
agent = Agent(
    model=model,
    tools=[DuckDuckGoTools(), NewspaperTools()],
    description="You are an AI agent specialized in analyzing startup trends. Use DuckDuckGo to search for recent startup news and Newspaper to extract article content. Provide insights on emerging trends, key players, and market opportunities.",
    instructions=[
        "Always use free resources only.",
        "Search for recent startup trends in AI, tech, and innovation sectors.",
        "Summarize key findings from articles and searches.",
        "Highlight potential opportunities and challenges.",
    ],
    markdown=True,
)

# Streamlit UI
st.title("AI Startup Trend Analysis Agent")
st.write("Analyze current trends in AI startups using free resources.")

# User input
query = st.text_input("Enter your query about startup trends:", "What are the latest trends in AI startups?")

if st.button("Analyze Trends"):
    if query:
        with st.spinner("Analyzing trends..."):
            response = agent.run(query)
            st.markdown(response.content)
    else:
        st.warning("Please enter a query.")

st.info("Note: This uses Grok LLM with a free tier. You need to add your own Grok API key from xAI to 'your_grok_api_key_here' in the code.")
