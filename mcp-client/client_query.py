"""
MCP Client de Agente que conecta com à um LLM da OpenAI, disponibliza tools 
de um  MCP Server Local (server.py) para LLM chamar conforme prompt informado.
"""
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback
import json

import os
from dotenv import load_dotenv

from openai import OpenAI #uv add openai

load_dotenv('.env')
assert os.getenv("OPENAI_API_KEY"), "OPEN_API_KEY not found"

server_params = StdioServerParameters(
    command="uv",
    args=["run","server.py"], #Optional command line arguments
)

async def run(query):
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                #Initialize server
                print("Initializing session...")
                await session.initialize()

                #Get tools
                print("Listing tools...")
                tools_result = await session.list_tools()
                print("Available tools:", tools_result)

                #Transformar as tools listadas do MCP Server
                #e tranformar para um fomataro válida para OpenAI LLM
                openai_tools = [
                    {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description,
                            "parameters": tool.inputSchema,
                        },
                    }
                    for tool in tools_result.tools
                ]

                # Make OpenAI LLM call
                messages = [
                    {"role":"user", "content": query}
                ]

                # Iniciando Cliente da OpenAI (conforme dados da LLM)
                client = OpenAI()
                response = client.chat.completions.create(
                    model="gpt-4o", # modelo de LLM
                    messages=messages, # mensagens do chat (contexto)
                    tools=openai_tools, # informando para o LLM quais tools tenho para utilizar (à partir do MCP Server)
                    tool_choice="auto", # Controla qual tool é chamada pelo LLM
                )   

                #Adicionando a resposta do LLM nas mensagens
                messages.append(response.choices[0].message)

                # Handle any tool calls
                # na resposta da LLM já indica se irá chamar a tool pela propriedade 'tool_calls' 
                if response.choices[0].message.tool_calls:
                    # Se na resposta da LLM indicar que irá chamar a tool (tool_calls)
                    # chamaremos a tool no código abaixo (call_tool)
                    for tool_execution in response.choices[0].message.tool_calls:
                        # Execute tool call
                        result = await session.call_tool(
                            tool_execution.function.name,
                            arguments=json.loads(tool_execution.function.arguments)
                        )

                        # Add tool response to convesation
                        messages.append(
                            {
                                "role": "tool", #role deverá ser tool, já que é retorno de uma tool
                                "tool_call_id": tool_execution.id,
                                "content": result.content[0].text,
                            }
                        )
                else:
                    return response.choices[0].message.content
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()


if __name__ == "__main__":
    query = "Whats the weather in Santos?"
    asyncio.run(run(query))
