```uv run client.py``` => rodar MCP Client

# MCP Client
Cria um simples servidor MCP utilizando fastmcp e uv (python)
onde disponibiliza uma tool: "**get_weather**" que retorna
um clima fixo conforme localização.


## Comandos

```mkdir helloworld``` => cria diretório <br>
```cd helloworld``` => vai no diretório <br>
```uv init``` => inicia projeto no UV <br>
```uv venv``` => cria um ambiente de venv (.venv) <br>
```.\.venv\scripts\activate``` => iniciar ambiente de desenvolvimento <br>
```uv add mcp[cli]``` => instalar pacote (MCP + cli) <br>
```mcp dev weather.py``` => Rodar MCP em modo de desenvolvimenoto usando MCP Inspector <br>
```uv run weather.py``` => rodar arquivo python (mas não irá aparecer nada no console) <br>
```mcp install weather.py``` => instala mcp diretamente no Clude Desktop (MCP Host) <br>