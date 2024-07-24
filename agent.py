from crewai import Agent
from tools.search_tools import SearchTools

class AINewsLetterAgent():
    def editor_agent(self):
        return Agent(
            role='Editor',
            goal="Oversee the creation of AI Newsletter",
            backstory="""With a keen eye for detail and a passion
                      for storytelling, you ensure that the newsletter not only informs
                      but also engages and inspires the readers""",
            verbose=True,
            allow_delegation=True,
            max_iter=15
        )
    
    def news_fetcher_agent(self):
        return Agent(
            role='News Fetcher',
            goal="Fetch the top AI news for the day",
            backstory="""As a digital sleuth, you scour the internet for the latest and 
                        most impactful developments in the world of AI, 
                        ensuring that our readers are always in the know.""",
            verbose=True,
            allow_delegation=True,
            tools=[SearchTools.search_internet]
        )
    
    def news_analyzer_agent(self):
        return Agent(
            role='News Analyzer',
            goal="Analyze the news articles",
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of AI news stories, making them accessible and engaging for our audience.""",
            verbose=True,
            allow_delegation=True,
            tools=[SearchTools.search_internet]
        )
    
    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""As the final architect of the newsletter, you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation that captivates our readers. Make sure to follow
            newsletter format guidelines and maintain consistency throughout.""",
            verbose=True,
        )