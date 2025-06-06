# ✍️ CrewAI YouTube Blog Generator: A Multi-Agent Content Creation System

**CrewAI YouTube Blog Generator** is a sophisticated multi-agent system designed to automate the creation of blog posts from YouTube videos. This project leverages the **CrewAI framework** to orchestrate a team of specialized AI agents that collaborate to research a YouTube video, write compelling content, and format it for publication. The agents are powered by a Large Language Model (LLM) via the **Groq API** (`llama3-8b-8192`) and use custom tools to search for and analyze YouTube content.

---
## 🚀 Features

* **Multi-Agent Collaboration**: Utilizes CrewAI to create a team of autonomous AI agents with distinct roles (e.g., Researcher, Writer).
* **Specialized Agent Roles**:
    * **`blog_researcher`**: An agent responsible for finding relevant video content on a specific YouTube channel for a given topic.
    * **`blog_writer`**: An agent tasked with narrating a compelling tech story based on the researched video content.
* **LLM Integration via Groq**: Agents are powered by the `llama3-8b-8192` model through the high-speed Groq API.
* **Custom Tool Integration**: Employs a `YoutubeChannelSearchTool` to allow agents to search for videos on a specific YouTube channel.
* **Task-Driven Workflow**: Defines specific tasks for each agent, such as identifying a video and creating a comprehensive report, or summarizing the video into a blog post.
* **Sequential Process**: The crew is configured to execute tasks sequentially, ensuring the writer has the necessary information from the researcher.
* **Automated Output**: The writing task is configured to automatically save the final blog post to a Markdown file (`new-blog-post.md`).
* **Memory and Caching**: The crew is configured with memory and caching enabled to enhance performance and maintain context across tasks.

---
## ⚙️ How it Works

The system is built around the CrewAI framework, which defines the agents, tasks, and the process they follow:

1.  **Initialization**: The main script (`crew.py`) kicks off the process with a defined topic (e.g., 'AI Vs ML Vs DL Vs Data Science').
2.  **Agents**: Two primary agents are defined in `agents.py`:
    * The **`blog_researcher`** agent's goal is to find relevant video content using the `YoutubeChannelSearchTool`. It's designed to understand AI-related topics and provide suggestions.
    * The **`blog_writer`** agent takes the information and crafts an engaging narrative. Its backstory emphasizes simplifying complex topics.
3.  **Tasks**: In `tasks.py`, two corresponding tasks are defined:
    * The **`research_task`** instructs the `blog_researcher` to identify a video on the given topic and generate a 3-paragraph report.
    * The **`write_task`** instructs the `blog_writer` to use the researched information to create a blog post, which is then saved to `new-blog-post.md`.
4.  **The Crew**: The `crew.py` script assembles the agents and tasks into a `Crew`. It sets the process as sequential, meaning the research task must be completed before the writing task begins.
5.  **Execution**: The `crew.kickoff()` method starts the execution. The `blog_researcher` first searches the specified YouTube channel for the video, and its findings are passed to the `blog_writer` to complete its task. The final result is printed to the console and saved to a file.

---
## 📋 Requirements

* Python 3.x
* A Groq API Key
* Required Python libraries: `crewai`, `crewai_tools`, `langchain_groq`, `python-dotenv`.

---
## 🛠️ Setup & Installation

1.  **Clone the repository or download the project files (`agents.py`, `crew.py`, `tasks.py`, `tools.py`).**

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install crewai crewai_tools langchain_groq python-dotenv
    ```

4.  **Set up Groq API Key:**
    * Obtain an API key from [Groq](https://console.groq.com/keys).
    * Create a `.env` file in the root directory of your project.
    * Add your Groq API key to the `.env` file:
        ```env
        Groq_API_KEY="your_groq_api_key_here"
        ```
    The scripts use `load_dotenv()` to load this key automatically.

---
## ▶️ Usage

1.  **Customize the Tools (Optional)**:
    * By default, the `YoutubeChannelSearchTool` is configured to search the `@krishnaik06` YouTube channel. You can change this handle in the `tools.py` file to target a different channel:
        ```python
        # in tools.py
        yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@YourTargetChannel')
        ```

2.  **Define the Topic**:
    * Open the `crew.py` file.
    * Modify the `inputs` dictionary in the `crew.kickoff()` call to set the topic you want the agents to create a blog post about:
        ```python
        # in crew.py
        result = crew.kickoff(inputs={'topic': 'Your New Topic Here'})
        ```

3.  **Run the Crew**:
    * Execute the main script from your terminal:
        ```bash
        python crew.py
        ```
    * The agents will start their sequential tasks. You will see verbose output in the console as they think and execute their actions.

4.  **Check the Output**:
    * Once the process is complete, the final result will be printed to the console.
    * A new Markdown file named `new-blog-post.md` will be created in your project directory containing the generated blog post.

---