from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from retrieval import chroma_tool
import streamlit as st
import json
import warnings
import sys

load_dotenv()

# llm = ChatGoogleGenerativeAI(
# 	model="gemini-1.5-flash",
# 	verbose=True,
# 	temperature=0.5,
# 	google_api_key=os.getenv("GEMINI_API_KEY")
# )

from crewai import Agent, LLM

llm = LLM(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini/gemini-1.5-flash",
)






@CrewBase
class UniversityAssistant:
	"""Agentic RAG crew for university manual assistance"""

	agents_config = 'agents.yaml'
	tasks_config = 'tasks.yaml'

	@agent
	def retriever_agent(self) -> Agent:
		return Agent(config=self.agents_config['retriever_agent'], tools=[chroma_tool], llm=llm, verbose=True)

	@agent
	def summarizer_agent(self) -> Agent:
		return Agent(config=self.agents_config['summarizer_agent'], llm=llm, verbose=True)

	@agent
	def generator_agent(self) -> Agent:
		return Agent(config=self.agents_config['generator_agent'], llm=llm, verbose=True)

	@task
	def retrieve_task(self) -> Task:
		return Task(config=self.tasks_config['retrieve_task'])

	@task
	def summarize_task(self) -> Task:
		return Task(config=self.tasks_config['summarize_task'])

	@task
	def generate_task(self) -> Task:
		return Task(config=self.tasks_config['generate_task'])

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True
		)


# if __name__ == "__main__":
# 	question = input("Ask a question about the university manual: ")
# 	crew_instance = UniversityAssistant()
# 	result = crew_instance.crew().kickoff(inputs={"question": question})
# 	print("\n🎓 Final Answer:\n")
# 	print(result)

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
        "question": text
    }
		
    crew_instance = UniversityAssistant()
		


    result = crew_instance.crew().kickoff(inputs=inputs)
    # data = json.loads(result)
    # st.json(data)
    #data = json.loads(result)
    #print(type(result))
    #st.write('Questions are here', result.raw)
    X= result.raw
    st.markdown(X,unsafe_allow_html=True)
    print(type(X))







with st.container():
    st.markdown('<p class="header">University chatbot</p>', unsafe_allow_html=True)
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


  





