from langchain_core.tools import tool
import os
from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv
from datetime import date,datetime
import requests
load_dotenv()



@tool
def get_weather(city: str) -> str:
    """This is a mock function that returns a fixed weather description for any city."""
    api_key=os.getenv('WEATHER_API_KEY')
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()


    weather=f"The current weather in {city},{data["location"]["region"]},{data["location"]["country"]} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."

    return weather

@tool
def get_time(city: str) -> str:
    """This is a mock function that returns a fixed time for any city."""
    now = datetime.now()
    time=now.time().strftime("%I:%M %p")
    return f"The current time is {time}."

@tool
def get_date(city: str) -> str:
    """This is a mock function that returns a fixed date for any city."""
    today = date.today()

    return f"The current date is {today}."

llm=AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    api_version='2024-12-01-preview',
    temperature=0.3,
    max_tokens=1000,
)


agent = create_agent(
    model=llm,
    tools=[get_weather,get_time,get_date],
    system_prompt="You are a helpful assistant",

)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in Narowal?"}]}
)

print(result["messages"][-1].content_blocks)