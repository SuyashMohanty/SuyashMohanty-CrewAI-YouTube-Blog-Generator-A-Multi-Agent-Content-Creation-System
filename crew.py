from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Froming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_researcher],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI Vs ML Vs DL Vs Data Science'})
print(result)