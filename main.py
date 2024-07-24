from agent import AINewsLetterAgent
from tasks import AINewsLetterTask
from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI
from file_io import save_markdown
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')

#initialize gpt-3.5 turbo

chat_gpt_35 = ChatOpenAI(temperature=0.4, model_name="gpt-3.5-turbo")

#initialize agents and tasks
agents = AINewsLetterAgent()
tasks = AINewsLetterTask()


#setting up agents

editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

#settng up tasks

fetch_news_task = tasks.NewsFetcherTask(news_fetcher)
news_analysis_task = tasks.NewsAnalyzerTask(news_analyzer, [fetch_news_task])
compile_task = tasks.compile_newsletter_task(
    newsletter_compiler, [news_analysis_task], callback_function=save_markdown)
#setting up tools



#setting up crew

crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, news_analysis_task, compile_task],
    process=Process.hierarchical,
    manager_llm=chat_gpt_35


)

#kickoff the crew
result=crew.kickoff()

print("Crew work result:")
print(result)
