# MCP Server 

- **server**: MCP Server de salvar e consultar Memórias (formato string) em um storage  de Vetor na OpenAI

```mcp dev server.py``` => rodar MCP server em mdo desenvolvimento

## Comandos

```mkdir {nome-mcp-server}``` => cria diretório <br>
```cd {nome-mcp-server}``` => vai no diretório <br>
```uv init``` => inicia projeto no UV <br>
```uv venv``` => cria um ambiente de venv (.venv) <br>
```.\.venv\scripts\activate``` => iniciar ambiente de desenvolvimento <br>
```uv add mcp[cli]``` => instalar pacote (MCP + cli) <br>
```mcp dev {nome-mcp-server}``` => Rodar MCP em modo de desenvolvimenoto usando MCP Inspector <br>
```uv run {nome-mcp-server}``` => rodar arquivo python (mas não irá aparecer nada no console) <br>
```mcp install {nome-mcp-server.py}``` => instala mcp diretamente no Claude Desktop (MCP Host) <br>

## Configuração Claude Desktop
```json
{
  "mcpServers": {
    "MemoryTracker": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Projetos\\Python\\mcp-masterclass\\mcp-build-memory-tracker",
        "run",
        "server.py"
      ]
    }
  }
}
```