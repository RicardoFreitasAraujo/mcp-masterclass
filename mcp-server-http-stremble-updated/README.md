# MCP com transporte HTTP Streamable

- **server**: MCP Server simples com transporte HTTP Streamable

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
O Claude Desktop não suporta transporte HTTP Streamable, dessa maneira
precisamos utilziar o pacote intermrdiário no npm: **mcp-remote** (https://www.npmjs.com/packages/mcp-remote)

```json
{
  "mcpServers": {
    "add_tool": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://127.0.0.1:8000/mcp"
        "--alllow-http"
      ]
    }
  }
}
```