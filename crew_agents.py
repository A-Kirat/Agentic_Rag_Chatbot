from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
#from crewai_tools import PDFSearchTool
#from pathlib import Path
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5, google_api_key=os.getenv("GEMINI_API_KEY"),
													 provider = "google")
print("hi")
#..........................................................................................................
@CrewBase
class crew_agents():
	"""PdfRag crew"""

	agents_config = 'agents.yaml'
	tasks_config = 'tasks.yaml'

	@agent
	def text_analyist_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['text_analyist_agent'],
			verbose=True,
			llm=llm
		)

	# @agent
	# def mcq_Generator_agent(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['question_generator_agent'],
	# 		verbose=True
	# 	)

	@task
	def text_analyist_task(self) -> Task:
		return Task(
			config=self.tasks_config['text_analyist_task'],
		)

	# @task
	# def mcq_Generator_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['question_generator_task'],
	# 	)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)