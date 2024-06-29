import streamlit as st
import os
from dotenv import load_dotenv
from model import llm
from tools import retrieve_recipes, retrieve_recipes_by_ingredients, retrieve_hotels
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage

load_dotenv()

tools = [retrieve_recipes_by_ingredients, retrieve_recipes, retrieve_hotels]

if 'messages' not in st.session_state:
    st.session_state.messages = []

def display_messages():
    print(st.session_state.messages)
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage) and message.content != '':
            with st.chat_message("assistant"):
                st.write(message.content)
        # elif isinstance(message, ToolMessage):
        #     with st.chat_message("tool"):
        #         st.write("tool", message.content)

def main():
    st.title("Chef BOT - Your Personal Chef")

    # display_messages()
    
    query = st.chat_input("What type of recipe are you looking for?")

    if query:
        print("Question taken")
        llm_with_tools = llm.bind_tools(tools)
        human_message = HumanMessage(content=query)
        st.session_state.messages.append(human_message)

        ai_msg = llm_with_tools.invoke(st.session_state.messages)
        st.session_state.messages.append(ai_msg)
        
        for tool_call in ai_msg.tool_calls:
            selected_tool = {
                "retrieve_recipes": retrieve_recipes,
                "retrieve_recipes_by_ingredients": retrieve_recipes_by_ingredients,
                "retrieve_hotels" : retrieve_hotels
            }[tool_call["name"].lower()]
            tool_output = selected_tool.invoke(tool_call["args"])
            tool_message = ToolMessage(content=tool_output, tool_call_id=tool_call["id"])
            st.session_state.messages.append(tool_message)

        results = llm_with_tools.invoke(st.session_state.messages)
        st.session_state.messages.append(results)
        print("displaying")
        display_messages()

if __name__ == "__main__":
    main()
