# DeyvinScript – Automate your development environment

DeyvinScript (Apresentando .deyvin como um Script de Automação nomeado de forma querida  (DeyvinScript)
is a tiny domain‑specific language (DSL) for automating
common tasks on your desktop.  It grew out of a simple idea: instead of
repeating the same steps every day, why not write them down in a
portable text file and let your computer do the work?  A `.deyvin`
script can open your favourite applications, tidy up temporary files
and even send you a desktop notification when everything is ready.

This repository contains an interpreter for `.deyvin` files (written in
pure Python), a VS Code syntax highlighting extension and a sample
script to get you started.  The interpreter is intentionally small and
easy to read – feel free to extend it with your own commands.

## Why DeyvinScript?

* **Simple syntax** – each action is defined on a single line beginning
  with `step`.  Arguments are enclosed in double quotes.  Comment
  lines start with `#`.
* **Cross‑platform notifications** – the `notify` command uses the
  optional [`desktop_notifier`](https://pypi.org/project/desktop-notifier/) library when available.  This
  library sends notifications via different backends depending on the
  operating system【211677555979899†L32-L42】.  If `desktop_notifier` is not installed the
  interpreter falls back to `notify-send`, AppleScript or Windows
  toast notifications and finally prints messages to the console.
* **Safe cleaning** – the `clean` command deletes all contents of a
  directory but deliberately avoids deleting the root directory.  The
  implementation uses `shutil.rmtree` to recursively remove
  subdirectories【262490351648928†L313-L320】 and resolves common aliases like
  `temp_folder`, `downloads` and `desktop`.
* **Portable process launching** – the `open` command locates
  executables using `shutil.which`, which searches your `PATH` for
  programs【262490351648928†L449-L454】.  If no executable is found the interpreter
  falls back to running the argument via the shell (or `os.startfile` on
  Windows).

## Getting started

### Prerequisites

DeyvinScript requires Python 3.8+ and works on Linux, macOS and
Windows.  For notifications you can optionally install
[`desktop-notifier`](https://pypi.org/project/desktop-notifier/)【211677555979899†L32-L42】 or
[`win10toast`](https://pypi.org/project/win10toast/) on Windows.

```bash
# optional (for nicer notifications)
pip install desktop-notifier win10toast
```

### Instalação via PyPI

Você pode instalar o DeyvinScript diretamente do PyPI.  Isto torna o
comando `deyvin` disponível no seu sistema, permitindo executar
arquivos `.deyvin` de qualquer lugar.  Para instalar a versão mais
recente (incluindo dependências opcionais para notificações mais
ricas) execute:

```bash
pip install deyvin-script[notify]
```

Sem o sufixo `[notify]` as dependências opcionais não serão
instaladas.  Para instalar apenas os componentes essenciais use:

```bash
pip install deyvin-script
```

### Executando um script

Após a instalação você pode executar um arquivo `.deyvin` com o
comando `deyvin`.  Um script de exemplo está disponível em
`sample.deyvin`:

```bash
# rodar o script de exemplo
deyvin sample.deyvin

# ativar logs detalhados
deyvin -v sample.deyvin
```

Se estiver utilizando o projeto em desenvolvimento (clonado do GitHub)
você ainda pode executar o módulo diretamente com Python:

```bash
python deyvin_script.py sample.deyvin
```

Também é possível criar um alias de shell para abreviar o comando
durante o desenvolvimento, por exemplo em `~/.bashrc` ou
`~/.zshrc`:

```bash
alias deyvin='python3 /path/to/deyvin_script/deyvin_script.py'
```

### Installing the VS Code extension

This repository includes a minimal VS Code extension in
`vscode-deyvin/` that provides syntax highlighting for `.deyvin` files.
To install it locally:

1. Open the command palette in VS Code (`F1` or `Ctrl+Shift+P`).
2. Choose **Developer: Install Extension from VSIX…**.
3. Browse to the `vscode-deyvin` folder and select a packaged VSIX file (you can create it by running `vsce package` inside the `vscode-deyvin` directory).
4. Reload VS Code and open a `.deyvin` file to see syntax
   highlighting.

The extension defines language aliases, file associations and a simple
TextMate grammar for keywords, commands, strings and comments.

## Script syntax

A DeyvinScript file is a UTF‑8 encoded plain text file.  Each
non‑empty line must begin with the word `step` followed by a command
name and one or more arguments in double quotes.  Anything after a
`#` character on a line is considered a comment.  Whitespace is
insignificant outside of quoted strings.

Commands are case‑insensitive.  For example:

```text
step open "firefox"      # launch Firefox
step wait "3"           # wait three seconds
step clean "downloads"  # remove files from your Downloads folder
step notify "Feito!"    # display a notification
```

### Supported commands

| Command | Description | Example |
| --- | --- | --- |
| `open` | Launch an application or open a file/directory.  Uses `shutil.which` to locate the executable【262490351648928†L449-L454】.  If a path is supplied, attempts to open it with the default OS mechanism. | `step open "code"` |
| `clean` | Delete all contents inside a directory using `shutil.rmtree`【262490351648928†L313-L320】.  Accepts aliases `temp_folder`, `downloads`, `desktop` and `cache`.  Does not delete the directory itself. | `step clean "temp_folder"` |
| `notify` | Display a desktop notification.  Uses the `desktop_notifier` library when available【211677555979899†L32-L42】; otherwise falls back to platform‑specific commands or prints to the console. | `step notify "Ambiente pronto"` |
| `wait` | Pause execution for a number of seconds (float). | `step wait "1.5"` |

Experimental commands such as `run`, `copy` and `backup` are included in
`deyvin.commands` but are commented out by default.  You can enable them
by adding them to the `COMMANDS` dictionary or by passing your own
mapping when instantiating the interpreter.

## Extending DeyvinScript

The interpreter can be easily extended to support new commands.  To add
a command, define a new function in `deyvin/commands.py` that accepts
a single string argument and performs the desired action.  Then
register the command either by modifying the `COMMANDS` dictionary or
by supplying a custom mapping when creating the interpreter:

```python
from deyvin.interpreter import Interpreter

def hello(name: str) -> None:
    print(f"Hello, {name}!")

interpreter = Interpreter(commands={"hello": hello})
interpreter.run("script.deyvin")
```

## Caveats and safety

* **Be careful with `clean`** – it will permanently delete files.  The
  implementation refuses to clean the root directory to prevent
  catastrophic mistakes, but you should still review your scripts
  carefully.
* **Notification support depends on your platform** – some systems
  require additional packages (`desktop-notifier` on Linux/macOS,
  `win10toast` on Windows) to display notifications.  When no
  backend is available the message will be printed instead.
* **Experimental commands** – `run`, `copy` and `backup` are provided
  as examples but are disabled by default to avoid accidental misuse.
  Enable them at your own risk.

## License

This project is provided under the MIT License.  See
`LICENSE` for full details.
