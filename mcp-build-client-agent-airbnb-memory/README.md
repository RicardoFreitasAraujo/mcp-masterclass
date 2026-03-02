# MCP Clients Diversos 

- **client**: MCP Client de Agente conversacional onde conecta em uma LLM da OpenAI
e disponibiliza tools de 2 servidores MCP para LLM integrar:  **Airbnb** e o **Memory Tracker (projeto local da solução)**
Neste chat, envia o prompt do uruário para LLM, no retorno da LLm valida se precisar chamar algum tool, caso sim chamar a 
tool e informa o retorno da tool para LLM.


- **chat_ui.py**: Uma interface para Chat conversacional feito em StreamLit, onde chama
o mesmo agent do **server**
```streamlit run chat_ui.py``` => rodar aplicação streamlint

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