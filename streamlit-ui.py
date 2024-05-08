import streamlit as st
from query_data import query_rag
# ===============================================================================
# M. Meetarbhan 
# 5/7/2024

# Streamlit provides built-in modules and objects for Web-UI development 
# python

st.title("BdoGPT_v1")

#message = st.chat_message("assistant")
#message.write("prototype-1")

# prompt = st.chat_input("Say something")
# if prompt: 
#    st.write(f"sipaki has sent the following prompt : {prompt} ")

if "messages" not in st.session_state:
    st.session_state.messages = []

def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})
    with st.chat_message(role):
        st.markdown(content)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input ("What is up?")
if prompt: 
    add_message("user", prompt)
    response_text = query_rag(prompt)
    add_message("assistant", response_text)

    #with st.chat_message("user"):
     #   st.markdown(prompt)
      #  st.session_state.messages.append({"role":"user", "content": prompt})




# ===============================================================================
