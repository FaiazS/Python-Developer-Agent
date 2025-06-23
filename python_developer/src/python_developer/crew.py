from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class PythonDeveloper():
    """PythonDeveloper crew"""

    agents_config = 'agents.yaml'

    tasks_config = 'tasks.yaml'

    
    @agent
    def software_developer(self) -> Agent:

        return Agent(

            config=self.agents_config['software_developer'], 

            verbose=True,

            allow_code_execution = True,

            code_execution_mode = 'safe',
            
            max_execution_time = 300,

            max_retry_limit = 7
        )


    @task
    def coding_task(self) -> Task:

        return Task(

            config=self.tasks_config['coding_task'], 
          
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PythonDeveloper crew"""
        

        return Crew(

            agents=self.agents,
              
            tasks=self.tasks,
              
            process=Process.sequential,

            verbose=True,
        )
