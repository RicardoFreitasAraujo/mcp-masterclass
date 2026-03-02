# MCP Diversos

- **local**: Um MCP server que irá interagir com arquvp local: notes.txt gravando lendo contaúdo
- **crypto**: MCP Server de CryptoMoeda utilziando API (coigecko) para descobrir o valor da cotação de cda criptomoeda
- **screenshot**: Um MCP Server que irá tirar um print da tela do desktop (utilizando pyautogui)
- **websearch**:MCP Server que irá consultar dados na Web utilizando api/LLM da empresa: Perplexity (http://www.perplexity.ai/)

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


# Configuração Claude Desktop
```json
{
  "mcpServers": {
    "ScreenShot Demo": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Projetos\\Python\\mcp-masterclass\\mcp-server-deepdice-functionally",
        "run",
        "screenshot.py"
      ]
    },
    "Crypto Demo": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Projetos\\Python\\mcp-masterclass\\mcp-server-deepdice-functionally",
        "run",
        "crypto.py"
      ]
    },
    "Other Inputs": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Projetos\\Python\\mcp-masterclass\\mcp-server-deepdice-functionally",
        "run",
        "other_inputs.py"
      ]
    }
  }
}
```