# 🐍 DeyvinScript (`.deyvin`)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Style: Sênior](https://img.shields.io/badge/Mindset-S%C3%AAnior-orange)](https://youtube.com)

> *"Porque se é para automatizar, que seja com estilo, café do lado e o mindset de quem não quer perder tempo com configuração manual."* ☕

O **DeyvinScript** é uma ferramenta de automação de ambiente de desenvolvimento feita para quem busca eficiência máxima. O projeto nasceu da vontade de dar uma utilidade épica para a extensão `.deyvin`, unindo a versatilidade do Python com a produtividade que todo desenvolvedor almeja.

##  O que é o DeyvinScript?

É uma camada de automação escrita em Python que interpreta arquivos com a extensão customizada `.deyvin`. Ele foi projetado para configurar setups, instalar dependências e preparar seu workflow em segundos, garantindo que seu "Mindset" esteja focado no que importa.

## ✨ Funcionalidades

-   **Interpretação Customizada**: Lê arquivos `.deyvin` com comandos simples.
-   **Setup Ágil**: Instalação de dependências e configuração de ambiente.
-   **Foco em Windows**: Pronto para rodar via scripts automatizados (`.bat`).
-   **Extensível**: Fácil de modificar para incluir novos comandos de automação.

## 📦 Como Usar

### 1. Instalação
Baixe a versão mais recente diretamente na nossa página de releases:
👉 [DeyvinScript Releases](https://github.com/Gustavo-de-Lima-G-000-Akiko-Yuuuki/Deyvin.Script/releases)

### 2. Configuração
1. extraia o arquivo `.zip`
1. Abra o arquivo `config.deyvin` em qualquer editor de texto.
2. O comportamento da automação é definido no arquivo `config.deyvin`.
3. Modifique as instruções de acordo com a necessidade do seu projeto.
4. Salve o arquivo.

### 3. Execução
Para rodar a mágica, basta executar o arquivo batch incluído:
```bash
Run_Python.bat
```
*O comando interno executado é:*
```powershell
python.exe -s deyvin_script.py config.deyvin
```

### 4. Resultado
Agora é só sentar, tomar um gole de café e ver o Python trabalhar por você. (Sim, existem outras formas, mas esta é a que gostei de fazer no domingo).

## 📄 Estrutura do Projeto

-   `deyvin_script.py`: O coração do projeto (o interpretador).
-   `config.deyvin`: Onde você define sua automação.
-   `Run_Python.bat`: Atalho para quem não quer digitar comandos no terminal.

## 🤝 Contribuindo

Sentiu falta de alguma feature "Sênior"? Sinta-se à vontade para abrir uma **Issue** ou enviar um **Pull Request**. Toda ajuda para tornar o workflow mais épico é bem-vinda!

---
*Feito com ☕ e Python em homenagem ao Mano Deyvin.*
---
---
*SEM GPT e COM DESCULPAS: DeyvinScript (Apresentando .deyvin queria um uso para essa extensao .deyvin entao aqui esta pode ser que futuramente mude mas o Mano Deyvin adora python então de forma querida, gosto de java mas nao tenho paciencia para Java mas tenho muita para c++/c, assembly, pyton, etc*
---

# WIKI DeyvinScript – Automatize seu ambiente de desenvolvimento

DeyvinScript é uma linguagem de domínio específico (DSL) criada para automatizar tarefas comuns no seu computador. A ideia é simples: em vez de repetir manualmente as mesmas etapas todos os dias, você descreve o procedimento em um arquivo de texto `.deyvin` e deixa o interpretador executá‑las por você. Um script `.deyvin` consegue abrir aplicativos, limpar diretórios temporários e até enviar uma notificação na área de trabalho quando tudo estiver concluído.

Este repositório inclui:
- **Interpretador em Python** – o núcleo que lê e executa arquivos `.deyvin`. O código é pequeno e fácil de entender, facilitando a criação de novos comandos.
- **Extensão para VS Code** – oferece realce de sintaxe para arquivos `.deyvin`, tornando mais fácil ler e escrever scripts.
- **Exemplo de script** – um arquivo `sample.deyvin` que demonstra comandos básicos para você começar.

## Por que usar o DeyvinScript?

- **Sintaxe simples** – cada ação é definida em uma única linha que começa com `step`, seguida do nome do comando e dos argumentos entre aspas duplas. Linhas em branco ou iniciadas com `#` são ignoradas.
- **Notificações multiplataforma** – o comando `notify` utiliza `desktop_notifier` quando a biblioteca está instalada. Caso contrário, o interpretador recorre a utilitários nativos (`notify‑send`, AppleScript ou `win10toast`) e, se nada estiver disponível, imprime a mensagem no console【211677555979899†L32-L42】.
- **Limpeza segura de pastas** – o comando `clean` remove todos os arquivos e subdiretórios de um diretório alvo, mas se recusa a apagar a pasta raiz para evitar acidentes. A implementação usa `shutil.rmtree` e aceita atalhos como `temp_folder`, `downloads` e `desktop`【262490351648928†L313-L320】.
- **Abertura de processos de forma portátil** – o comando `open` localiza executáveis utilizando `shutil.which` (buscando no `PATH`) e, se não encontrar, tenta abrir o argumento via shell ou com `os.startfile` no Windows【262490351648928†L449-L454】.

Esses recursos tornam o DeyvinScript ideal para configurar seu ambiente de trabalho com um único comando, agilizando a rotina diária.

## Começando

### Pré‑requisitos

- Python **3.8** ou superior.
- Linux, macOS ou Windows.

Para receber notificações mais ricas, é recomendável instalar opcionalmente as bibliotecas `desktop-notifier` e `win10toast`:

```bash
pip install desktop-notifier win10toast
```

### Instalação via PyPI (Pendente)

Instale a última versão através do PyPI. O comando `deyvin` ficará disponível globalmente:

```bash
# com dependências opcionais de notificação
pip install deyvin-script[notify]

# apenas a biblioteca principal
pip install deyvin-script
```

### Executando um script `.deyvin`

Uma vez instalado, você pode executar scripts `.deyvin` de qualquer lugar:

```bash
deyvin config.deyvin
# ou com log detalhado
deyvin -v config.deyvin
```

Se estiver desenvolvendo localmente (clonando o repositório), execute diretamente com Python:

```bash
python deyvin_script.py config.deyvin
```

Também é possível criar um alias no seu shell para encurtar o comando durante o desenvolvimento:

```bash
alias deyvin='python3 /caminho/para/deyvin_script/deyvin_script.py'
```

### Instalando a extensão do VS Code

A pasta `vscode-deyvin/` contém uma extensão simples que adiciona realce de sintaxe para arquivos `.deyvin`. Para instalá‑la manualmente:

1. Gere um arquivo `.vsix` rodando `vsce package` dentro de `vscode-deyvin`.
2. No VS Code, pressione `F1` ou `Ctrl+Shift+P` e selecione **Developer: Install Extension from VSIX…**.
3. Escolha o `.vsix` gerado e reinicie o VS Code.

A extensão associa a extensão de arquivo `.deyvin` a uma gramática TextMate que destaca palavras‑chave (`step`), comandos (`open`, `clean`, `notify`, `wait`), strings entre aspas e comentários.

## Sintaxe dos scripts

Um script DeyvinScript é um arquivo de texto UTF‑8. Cada linha relevante deve começar com `step` e o nome de um comando. Os argumentos ficam entre aspas duplas. Comentários iniciados com `#` são ignorados. Linhas vazias são puladas.

Exemplo:

```text
step open "code"              # abre o Visual Studio Code (ou editor padrão)
step open "chrome"           # abre o navegador Firefox
step wait "2"                # aguarda 2 segundos
#step clean "temp_folder"     # limpa o diretório temporário do sistema
step notify "Segue lá o Maninho: https://www.youtube.com/@manodeyvin" # exibe uma notificação ou imprime no console

```

### Comandos suportados

| Comando | Descrição | Exemplo |
| ------- | --------- | ------- |
| `open`  | Abre um programa, arquivo ou diretório. Procura o executável no `PATH`; se um caminho é passado, tenta abri‑lo com o mecanismo padrão do SO【262490351648928†L449-L454】. | `step open "code"` |
| `clean` | Remove todo o conteúdo de uma pasta usando `shutil.rmtree`【262490351648928†L313-L320】. Aceita aliases (`temp_folder`, `downloads`, `desktop`, `cache`). Não remove a pasta em si. | `step clean "temp_folder"` |
| `notify` | Exibe uma notificação de área de trabalho, usando `desktop_notifier` quando disponível【211677555979899†L32-L42】; caso contrário imprime no console. | `step notify "Tudo pronto"` |
| `wait`   | Pausa a execução por um número de segundos (pode ser decimal). | `step wait "1.5"` |

Comandos experimentais como `run`, `copy` e `backup` estão implementados em `deyvin.commands` mas vêm desabilitados. Você pode habilitá‑los adicionando‑os à tabela `COMMANDS` ao criar o interpretador ou passando um dicionário personalizado.

## Estendendo o DeyvinScript

É possível criar seus próprios comandos sem alterar o núcleo. Basta definir uma função em `deyvin/commands.py` que receba uma string e realize a ação desejada, e registrar essa função ao instanciar o interpretador:

```python
from deyvin.interpreter import Interpreter

def hello(nome: str) -> None:
    print(f"Olá, {nome}!")

interprete = Interpreter(commands={"hello": hello})
interprete.run("config.deyvin")
```

## Cuidados e segurança

- **Atenção ao usar `clean`** – o comando apaga arquivos de forma permanente. Embora haja proteção contra apagar diretórios raiz, revise seus scripts antes de executá‑los.
- **Dependências de notificação** – para notificar corretamente em cada sistema operacional você pode precisar instalar `desktop-notifier` (Linux/macOS) ou `win10toast` (Windows).
- **Comandos experimentais** – `run`, `copy` e `backup` são exemplos avançados e não estão ativados por padrão. Utilize com cautela ao habilitá‑los.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
