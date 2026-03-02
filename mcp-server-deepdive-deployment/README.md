# MCP Server

- MCP server de tewstes para ser exportado via GITHUB
- **__init__.py** => No python serve principalmente para marcar um diretório como um pacote. permitiando que os módulos
dentro dele sejam importados por outros scripts
- **__main__.py** => No python serve como ponto de entrada principal para execução de um pacote (uma pasta com
módulos). Quando você utiliza o comando python -m nome_do_pacote, o Python procura automaticamente por esse arauivo
dentro da pasta para executá-lo.


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

## No arquivo 'pyproject.toml' adicionar para UVX
```
[project.scripts]
mcp-server = "mcpserver.__main__:main"

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

## Instalar MCP Server localmente à partir da url do github
```sh
uvx --from git+https://github.com/henryhabib/mcpserverexample.git mcp-server 
```


# Installation Steps

To install the `add_tool` MCP server, run the following command:

```json
{
  "mcpServers": {
    "add_tool": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/henryhabib/mcpserverexample.git",
        "mcp-server"
      ]
    }
  }
}
```

This will fetch and set up the `mcp-server` from the specified GitHub repository.