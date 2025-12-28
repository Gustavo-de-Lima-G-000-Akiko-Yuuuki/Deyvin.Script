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

Aqui está o conteúdo organizado e formatado em **Markdown** padrão para o GitHub, utilizando as melhores práticas de documentação (tabelas, blocos de código, alertas e ícones).

Você pode copiar o código abaixo e colar diretamente no seu arquivo `README.md`.

---



### 🛠️ Regras Gerais

Para manter a simplicidade e legibilidade, o interpretador segue estas diretrizes:

*   **Instruções:** Cada linha de comando válida deve obrigatoriamente iniciar com a palavra-chave `step`.
*   **Argumentos:** Os valores passados aos comandos devem estar entre aspas duplas (`"`).
*   **Comentários:** Linhas iniciadas com `#` são ignoradas pelo interpretador.
*   **Espaçamento:** Linhas vazias são ignoradas automaticamente para facilitar a organização visual.
*   **Case Insensitivity:** Os nomes dos comandos não diferenciam maiúsculas de minúsculas (`OPEN` é o mesmo que `open`).

---

### 1. Exemplos Práticos
```markdown
#### 1. Exemplo Básico
Ideal para entender o funcionamento inicial.
```bash
step open "code"              # Abre o Visual Studio Code (ou editor padrão)
step open "chrome"            # Abre o navegador
step wait "2"                 # Aguarda 2 segundos
# step clean "temp_folder"    # Linha comentada (não será executada)
step notify "Siga o Maninho: https://www.youtube.com/@manodeyvin"
```

#### 2. Setup de Ambiente de Trabalho
Automatize a abertura de todas as suas ferramentas de uma vez.
```bash
# Ambiente de trabalho padrão
step notify "Preparando ambiente..."

step open "chrome"
step open "code"
step open "explorer"          # No Windows, abre o Explorador de Arquivos
step wait "1"

step open "C:/Projetos"       # Abre um diretório específico
step notify "Ambiente pronto 🚀"
```

#### 3. Rotina de Limpeza
Mantenha seu sistema leve antes de começar a codar.
```bash
# Limpeza rápida antes de iniciar o dia
step notify "Iniciando limpeza do sistema"

step clean "temp_folder"
step clean "downloads"
step wait "0.5"

step notify "Limpeza concluída"
```

---

### 📖 Comandos Suportados

| Comando | Descrição | Exemplo |
| :--- | :--- | :--- |
| `open` | Abre um programa, arquivo ou diretório. Procura no PATH ou usa o mecanismo padrão do SO. | `step open "code"` |
| `clean` | Remove o conteúdo de uma pasta (sem apagar a raiz). Aceita aliases (veja abaixo). | `step clean "temp_folder"` |
| `notify` | Exibe uma notificação de sistema ou mensagem no console. | `step notify "Tudo pronto"` |
| `wait` | Pausa a execução por N segundos (aceita valores decimais). | `step wait "1.5"` |

#### 📂 Aliases de Diretórios Reconhecidos
Ao usar o comando `clean`, você pode utilizar atalhos para pastas comuns:
*   `temp_folder`: Pasta temporária do sistema.
*   `downloads`: Pasta de downloads do usuário.
*   `desktop`: Área de trabalho.
*   `cache`: Diretórios comuns de cache (dependente do SO).

---

### 🧪 Comandos Experimentais
> [!CAUTION]
> **Atenção:** Os comandos abaixo já estão implementados, mas vêm desabilitados por padrão no dicionário `COMMANDS` para garantir a segurança do sistema.

| Comando | Função |
| :--- | :--- |
| `run` | Executa comandos diretos do terminal/sistema. |
| `copy` | Copia arquivos ou diretórios de origem para destino. |
| `backup` | Cria cópias de segurança simples de pastas selecionadas. |

Para habilitá-los, adicione a função correspondente ao dicionário de comandos no núcleo do interpretador.

---

### 🧩 Estendendo o DeyvinScript

O DeyvinScript foi projetado para ser **extensível**. Você pode criar novos comandos em Python e injetá-los no interpretador sem tocar no código base.

#### Exemplo: Criando um comando personalizado
```python
from deyvin.interpreter import Interpreter

# 1. Defina a função Python
def hello(nome: str) -> None:
    print(f"Olá, {nome}!")

# 2. Registre no interpretador
interprete = Interpreter(commands={
    "hello": hello
})

interprete.run("meu_script.deyvin")
```

**No seu arquivo `.deyvin`:**
```bash
step hello "Maninho"
```

---

### 💡 Boas Práticas

1.  **Responsabilidade Única:** Cada comando deve fazer apenas uma coisa bem feita.
2.  **Segurança:** Evite comandos destrutivos sem validação prévia.
3.  **Feedback:** Sempre use `notify` em scripts longos para saber em que pé está a execução.
4.  **Simplicidade:** Prefira nomes de comandos curtos e intuitivos.

---

### 🗺️ Roadmap de Evolução
Futuras implementações previstas para a linguagem:
- [ ] Suporte a variáveis (`set`).
- [ ] Verificações condicionais (`if exists`).
- [ ] Logs estruturados para depuração.
- [ ] Extensão oficial para VS Code (Highlighting).

## Cuidados e segurança

- **Atenção ao usar `clean`** – o comando apaga arquivos de forma permanente. Embora haja proteção contra apagar diretórios raiz, revise seus scripts antes de executá‑los.
- **Dependências de notificação** – para notificar corretamente em cada sistema operacional você pode precisar instalar `desktop-notifier` (Linux/macOS) ou `win10toast` (Windows).
- **Comandos experimentais** – `run`, `copy` e `backup` são exemplos avançados e não estão ativados por padrão. Utilize com cautela ao habilitá‑los.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
