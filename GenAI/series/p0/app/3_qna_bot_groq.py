from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_serpdive import SerpdiveSearch
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessageChunk
from langgraph.checkpoint.memory import MemorySaver


# -----------------------------------
# LLM and Search Tool
# -----------------------------------

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    streaming=True
)

search = SerpdiveSearch()


@tool
def web_search(query: str) -> str:
    """Search the web for current and up-to-date information."""
    return search.run(query)


# -----------------------------------
# Streamlit Session State
# -----------------------------------

if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()

if "history" not in st.session_state:
    st.session_state.history = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_1"


# -----------------------------------
# Create Agent
# -----------------------------------

agent = create_agent(
    model=llm,
    tools=[web_search],
    checkpointer=st.session_state.memory,
    system_prompt="""
You are a web research agent.

For questions about current events, recent results, live information,
or information that may have changed, you MUST use the web_search tool
before answering.

Do not answer from your internal knowledge when current information
is requested. Use the search results to formulate your answer.

Do not use special citation formats such as 【1†L1-L3】.
Give the user a clean and natural response.
"""
)


# -----------------------------------
# Streamlit UI
# -----------------------------------

st.subheader("👩‍🚀 Web Research Agent")


# Display previous messages
for message in st.session_state.history:
    st.chat_message(message["role"]).markdown(
        message["content"]
    )


# User Input
query = st.chat_input("Ask anything...")


if query:

    # -----------------------------------
    # Display User Message
    # -----------------------------------

    st.chat_message("user").markdown(query)

    st.session_state.history.append({
        "role": "user",
        "content": query
    })


    # -----------------------------------
    # Stream Agent Response
    # -----------------------------------

    response = agent.stream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": st.session_state.thread_id
            }
        },
        stream_mode="messages"
    )


    # -----------------------------------
    # Display AI Response
    # -----------------------------------

    with st.chat_message("assistant"):

        space = st.empty()
        message = ""

        for chunk in response:

            # Display only AI-generated text,
            # not tool results
            if (
                isinstance(chunk[0], AIMessageChunk)
                and chunk[0].content
            ):
                message += chunk[0].content
                space.markdown(message)


    # -----------------------------------
    # Save AI Response
    # -----------------------------------

    if message:
        st.session_state.history.append({
            "role": "assistant",
            "content": message
        })