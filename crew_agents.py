from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from retrieval import chroma_tool

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


if __name__ == "__main__":
	question = input("Ask a question about the university manual: ")
	crew_instance = UniversityAssistant()
	result = crew_instance.crew().kickoff(inputs={"question": question})
	print("\n🎓 Final Answer:\n")
	print(result)
