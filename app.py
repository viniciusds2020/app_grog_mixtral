import streamlit as st
from langchain_groq import ChatGroq
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from decouple import config
from langchain.memory import ConversationBufferWindowMemory

GROQ_API_KEY = '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'
MODEL_NAME = 'llama3-70b-8192'

prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""You are a very kindl and friendly AI assistant. You are
    currently having a conversation with a human. Answer the questions
    in a kind and friendly tone with some sense of humor.
    
    chat_history: {chat_history},
    Human: {question}
    AI:"""
)

llm = ChatGroq(temperature=0.7, groq_api_key=GROQ_API_KEY, model_name=MODEL_NAME)
memory = ConversationBufferWindowMemory(memory_key="chat_history", k=4)
llm_chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt
)

st.set_page_config(
    page_title="Chat Llama3",
    page_icon="🤖",
    layout="wide"
)

st.title("Chat Llama3")

# check for messages in session and create if not exists
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there, am ChatGPT clone"}
    ]

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = llm_chain.predict(question=user_prompt)
            st.write(ai_response)
    new_ai_message = {"role": "assistant", "content": ai_response}
    st.session_state.messages.append(new_ai_message)
