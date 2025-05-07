import sys
import warnings
import streamlit as st
import json

from test import McqGen

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
local_css("style.css")
def run():
    """
    Run the crew.
    """

    #user_input = input("Enter your question: ")

    inputs = {
        'input': text
    }

    result = McqGen().crew().kickoff(inputs=inputs)
    # data = json.loads(result)
    # st.json(data)
    #data = json.loads(result)
    #print(type(result))
    #st.write('Questions are here', result.raw)
    X= result.raw
    st.markdown(X,unsafe_allow_html=True)
    print(type(X))





with st.container():
    st.markdown('<p class="header">Multiple Choice Questions Generator</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Enter The Text Please:</p>', unsafe_allow_html=True)
    text = st.text_area("", height=150)
    #st.write(messi_text)
    # name = st.text_input('Enter your name: ',)
    #text = st.text_area('Enter The Text Please: ', height=150) 
    # st.write('Your name is ', name)
    # st.write('Your name is1 ', ame)
    submit_button = st.markdown('<button class="submit_button">Submit the text</button>', unsafe_allow_html=True)
# Check if the button is clicked and if the input is valid
    if submit_button:
        if text.strip():
            st.markdown('<p class="content">Your submission was successful!</p>', unsafe_allow_html=True)
            run()  # Check if name is not empty or just spaces
        else:
            st.warning('Please enter the text before submitting.')


  





