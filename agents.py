from crewai import Agent
from tools import yt_tool
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

import os
groq_api_key = os.getenv("Groq_API_KEY")
#os.environ["Grow_Model_Name"]="groq/llama3-8b-8192"
llm=ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")

## Create a  Senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Video',
    goal='get the relivant video content for the topic{topic} from Yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning And Gen AI and providing suggessions"
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=True
)

## Creating a senior blog writer agent with YT tool
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False
)