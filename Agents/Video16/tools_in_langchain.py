
#my first tool calling agent.
from langchain_core.tools import tool
import os
from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv

import requests
load_dotenv()

# built in tools
# from langchain_core.tools import tool
# from langchain_community.tools import DuckDuckGoSearchRun,DuckDuckGoSearchResults
#
# search=DuckDuckGoSearchResults()
#
#
# print(search.invoke("who is psl winner in 2026 and what is the score of the final match"))


#tool creation using @ tool decorator

# custom tool's
# @tool
# def get_weather(city: str) -> str:
#     """This is a mock function that returns a fixed weather description for any city."""
#     api_key=os.getenv('WEATHER_API_KEY')
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
#     response = requests.get(url)
#     data = response.json()
#
#
#     weather=f"The current weather in {city},{data["location"]["region"]},{data["location"]["country"]} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."
#
#     return weather

# print(get_weather.name)
# print(get_weather.description)
# print(get_weather.args)


# print(get_weather.invoke({"city":"New York"}))


#tool creation using structured tool and pydantic model

# from pydantic import BaseModel, Field
# from langchain_community.tools import StructuredTool
#
#
# def get_weather(city: str) -> str:
#     api_key=os.getenv('WEATHER_API_KEY')
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
#     response = requests.get(url)
#     data = response.json()
#     weather=f"The current weather in {city},{data["location"]["region"]},{data["location"]["country"]} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."
#     return weather
#
#
# class WeatherToolInput(BaseModel):
#     city: str = Field(required=True, description="The name of the city to get the weather for")
#
#
# weather_tool=StructuredTool.from_function(
#     name="get_weather",
#     description="""This is a mock function that returns a fixed weather description for any city."""
#     ,func=get_weather,
#     input=WeatherToolInput
# )
#
# print(weather_tool.name)
# print(weather_tool.description)
# print(weather_tool.args)
#
# print(weather_tool.invoke({"city":"New York"}))



#tool creation using base class.











