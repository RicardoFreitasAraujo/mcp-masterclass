"""
MCP Client de Agente conversacional onde conecta em uma LLM da OpenAI
e disponibiliza tools de 2 servidores MCP para LLM integrar:  **Airbnb** e o **Memory Tracker (projeto local da solução)**
Neste chat, envia o prompt do uruário para LLM, no retorno da LLm valida se precisar chamar algum tool, caso sim chamar a 
tool e informa o retorno da tool para LLM.
"""

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback
import json

import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY not found"

# Define parametewrs for two servers
server_params_1 = StdioServerParameters(
    command="npx",
    args=["-y","@openbnb/mcp-server-airbnb","--ignore-robots-txt"],
)

server_params_2 = StdioServerParameters(
    command="uv",
    args=["--directory","C:\\projetos\\python\\mcp-masterclass\\mcp-build-memory-tracker","run","server.py"],
)

async def run():
    try:
        print("Starting stdio_clients fot both servers...")
        async with stdio_client(server_params_1) as (read1, write1), stdio_client(server_params_2) as (read2, write2):
            print("Clients connected, cretating sessions...")
            async with ClientSession(read1, write1) as session1, ClientSession(read2, write2) as session2:

                # Initialize both servers
                print("Initializing sessions...")
                await session1.initialize()
                print("Initializing sessions 2...")
                await session2.initialize()

                # Get tools from both servers
                print("Listing tools from both servers...")
                tools_result1 = await session1.list_tools()
                tools_result2 = await session2.list_tools()

                # Combine tools (simple merge, you can deduplicate by name if needed)
                combine_tools = tools_result1.tools + tools_result2.tools 
                print("Available tools (combined): ", combine_tools) 

                openai_tools = [
                    {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description,
                            "parameter": tool.inputSchema,
                        },
                    }
                    for tool in combine_tools
                ]

                client = OpenAI()
                messages = []
                while True:
                    user_input = input("You: ").strip()
                    if user_input.lower() in ("exit", "quit"): #Allow user to exit
                        print("Exiting chat.")
                        break
                    if not user_input:
                        continue
                    messages.append({"role": "user", "content": user_input})

                    # Chama LLm da OpenAI
                    response = client.chat.completions.create(
                        model = 'gpt-4o',
                        messages=messages,
                        tools=openai_tools,
                        tool_choice="auto"
                    )

                    # Adiciona mensagem da openai
                    messages.append(response.choices[0].message)
                    tool_calls = response.choices[0].message.tool_calls

                    # Handle any tool calls
                    # No retorno da LLM, verifica se precisa chamar alguma tool
                    if response.choices[0].message.tool_calls:
                        for tool_execution in tool_calls:
                            # Decide with session to sue based in tool name
                            if any(t.name == tool_execution.function.name for t in tools_result1.tools):
                                session = session1
                            else:
                                 session = session2   
                            
                            # Execute tool call
                            result = await session.call_tool(
                                tool_execution.function.name,
                                arguments=json.loads(tool_execution.function.arguments)
                            )

                            #Add tool response to conversation
                            messages.append(
                                {
                                    "role":"tool",
                                    "tool_call_id": tool_execution.id,
                                    "content": result.content[0].text
                                }
                            )

                            #Get rersponse from LLM informando o retorno da tool
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=messages,
                                tools=openai_tools,
                                tool_choice="auto",
                            )

                            # Com o retorno da LLM (informando retorno da tool), verifica no status "finish_reason"
                            # se a LLM irá chamar uma outra tool para responder o prompt do usuário

                            # Neste caso a LLm está informando que precisará chamar um outra tool
                            # para responder (extendendo o "tool_calls" para continaur o loop)
                            if response.choices[0].finish_reason == "total_calls":
                                tool_calls.extend(response.choices[0].message.tool_calls)

                            # Neste caso a LLm conseguiu responder o usuário sem chamar tools adicioanis
                            if response.choices[0].finish_reason == "stop":
                                print(f"AI: {response.choices[0].message.content}")
                                messages.append(response.choices[0].message)
                                break
                    else:
                        print(f"AI: {response.choices[0].message.content}")
                        messages.append(response.choices[0].message)
    except:
        print("An error occureed")
        traceback.print_exc()
    
if (__name__ == "__main__"):
    asyncio.run(run())