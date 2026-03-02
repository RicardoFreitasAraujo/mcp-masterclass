# MCP Cliente Diversos

- **server**: MCP Server Simples para testes com o cliente MCP com tools, resource e prompts que retorno sobre o clima (weather)
- **client_simple**: MCP Client simples que conecta em um MCP Server local (Server.py), listando as tools, resources, prompts existentes.
- **client_query**:MCP Client de Agente que conecta com à um LLM da OpenAI, disponibliza tools de um  MCP Server Local (server.py) para LLM chamar conforme prompt informado.


```uv run client.py``` => rodar MCP Client

## Comandos

```mkdir {nome-mcp-server}``` => cria diretório <br>
```cd {nome-mcp-server}``` => vai no diretório <br>
```uv init``` => inicia projeto no UV <br>
```uv venv``` => cria um ambiente de venv (.venv) <br>
```.\.venv\scripts\activate``` => iniciar ambiente de desenvolvimento <br>
```uv add mcp[cli]``` => instalar pacote (MCP + cli) <br>
```mcp dev {nome-mcp-server}``` => Rodar MCP em modo de desenvolvimenoto usando MCP Inspector <br>
```uv run {nome-mcp-server}``` => rodar arquivo python (mas não irá aparecer nada no console) <br>
```mcp install {nome-mcp-server.py}``` => instala mcp diretamente no Clude Desktop (MCP Host) <br>

## Configuração Claude Desktop
```json
{
  "mcpServers": {
    "prompt": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Projetos\\Python\\msp-masterclass\\mcp-primitive-and-inputs",
        "run",
        "prompt.py"
      ]
    },
    "resource": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Projetos\\Python\\msp-masterclass\\mcp-primitive-and-inputs",
        "run",
        "resources.py"
      ]
    }
  }
}
```