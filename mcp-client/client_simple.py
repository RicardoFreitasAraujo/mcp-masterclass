"""
MCP Client simples que conecta em um MCP Server local (Server.py),
listando as tools, resources, prompts existentes.

Comando: uv run client_simple.py
"""
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

# Parâmetros de conexão
server_params = StdioServerParameters(
    command="uv",
    args=["--directory", "C:\Projetos\Python\mcp-masterclass\mcp-client", "run", "server.py"] # Optional command line arguments
)

async def run():
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                print("Initializing session...")
                await session.initialize()

                # TOOLS
                print("Listing tools...")
                tools = await session.list_tools()
                print("Available Tools:", tools)

                print("Calling tool...")
                result = await session.call_tool("get_weather", arguments={"location": "Santos"})
                print("Tool result:", result)

                # RESOURCES
                print("Listing resources...")
                resources = await session.list_resources()
                print("Available resources: ", resources)

                print("Getting resources templates...")
                resources = await session.list_resource_templates()
                print("Available resources templates: ", resources)

                print("Getting resource")
                resource = await session.read_resource("weather://statement")
                print(resource)

                print("Getting resource template")
                resource = await session.read_resource("weather://santos//statement")
                print(resource)

                # PROMPTS
                print("Listing prompts...")
                promtps = await session.list_prompts()
                print("Available prompts templates: ", promtps)

                print("Getting prompt...")
                result = await session.get_prompt("get_prompt", arguments={"topic:":"Water cycle"})
                print("Prompt result:", result)



    except Exception as e:
        print("An error occured:")
        traceback.print_exc()

if (__name__ == "__main__"):
    asyncio.run(run())


