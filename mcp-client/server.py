"""
MCP Server Simples para testes com o cliente MCP
com tools, resouce e prompts que retorno sobre
o cliema (weather)

Testar: mcp dev server.py
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Gets the weather given a location
    Args:
        location, can be city, country, state, etc.
    """
    return f"The Wheater in {location} is hot an dry"

@mcp.resource("weather://statement")
def get_weather_statement() -> str:
    """
    Returns the weather statement 
    """
    return "This is an example weather statement"

@mcp.resource("weather://{city}//statement")
def get_weather_statement_from_city(city: str) -> str:
    """
    Returns the weather statement basead an particular city
    """
    return "No special statements for this city: {city}"

@mcp.prompt()
def get_prompt(topic:str) -> str:
    """
    Returns a prompt realted to asking for more information on weather concepts about {topic}
    Args:
        topic: the tipic to do research on
    """
    return f"Describe the weather concept of {topic}"

if (__name__ == "__main__"):
    mcp.run()