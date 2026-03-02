"""
Cria um simples servidor MCP utilizando fastmcp e uv (python)
onde disponibiliza uma tool: "get_weather" qu retorna
um clima fixo conforme localização.

Comandos
mkdir helloworld => cria dieratório
cd helloworld => vai no diretório
uv init => inicia projeto no UV
uv venv => cria um ambiente de venv (.venv)
.\.venv\scripts\activate => iniciar ambiente de desenvolvimento
uv add mcp[cli] => instalar pacote (MCP + cli)
uv run weather.py => rodar arquivo python (mas não irá aparecer nada no console)
mcp install weather.py => Instala mcp diretamente no Claude Desktop (MCP Host)
mcp install weather.py => instala mcp diretamente no Clude Desktop (MCP Host)
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Gets the weather given a location
    Args:
        location: location, can be city, country, state, etc.
    """
    return "The weather is hot and dry"

if __name__ == "__main__":
    mcp.run()


"""
Configuração para Claude Desktop em modo transporte STDIO

{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Projetos\\Python\\mcp-masterclass\\helloworld",
        "run",
        "weather.py"
      ]
    }
  }
}


"""