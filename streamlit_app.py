import os 
import langchain
from datetime import date
import streamlit as st
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import time

apikey=st.secrets["key"]
os.environ["OPENAI_API_KEY"] = apikey
st.title('🦜🔗 Shubham\'s Fun Fact Creator')

title_template = PromptTemplate(
    input_variables=['date'],
    template='Tell me a funny and interesting fact specific to the date today. The date today is {date}. Start your response with "Dear Shubham, here is a funny historical fact about today: \n" and end the output with "That\'s it for today! See you soon! and Take Care!". Reply in a positive mood always.'
)
model_name = "gpt-3.5-turbo"
title_memory = ConversationBufferMemory(input_key='date', memory_key='chat_history')
llm = ChatOpenAI(model_name=model_name)

title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
d2 = date.today().strftime("%B %d, %Y")
answer = title_chain.run({'date':str(d2)})
with st.spinner('Please wait, Shubham, your fun fact is loading...'):
    time.sleep(5)
st.write(answer)
