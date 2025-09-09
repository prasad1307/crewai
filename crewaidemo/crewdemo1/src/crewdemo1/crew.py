from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class StudyNotesDemo():
    """Education: Study Notes Generator Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def research_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['research_assistant'],
            verbose=True
        )

    @agent
    def note_maker(self) -> Agent:
        return Agent(
            config=self.agents_config['note_maker'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def notes_task(self) -> Task:
        return Task(
            config=self.tasks_config['notes_task'],
            output_file='study_notes.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # run tasks in order
            verbose=True,
            output_log_file=True
        )
