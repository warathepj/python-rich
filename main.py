from rich import print
from rich.progress import Progress
from rich.table import Table
from rich.tree import Tree
from rich.syntax import Syntax
from rich.markdown import Markdown
import time

# Basic styled print with emoji
print("[bold magenta]Welcome to the Rich Library Demo![/bold magenta] :rocket:")

# Progress bar demonstration
print("\n[underline]Progress Bar Example:[/underline]")
with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100)
    while not progress.finished:
        progress.update(task, advance=0.5)
        time.sleep(0.02)

# Table creation
table = Table(title="[bold green]Sample Table[/bold green]")
table.add_column("ID", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Email", justify="right", style="green")
table.add_row("1", "Alice", "alice@example.com")
table.add_row("2", "Bob", "bob@example.com")
table.add_row("3", "Charlie", "charlie@example.com")
print("\n")
print(table)

# Tree structure demonstration
tree = Tree("🌍 [bold yellow]World[/bold yellow]")
asia = tree.add("🌏 Asia")
europe = tree.add("🌍 Europe")
asia.add("[red]China[/red]").add("[green]Beijing[/green]")
asia.add("[blue]India[/blue]").add("[green]New Delhi[/green]")
europe.add("[magenta]France[/magenta]").add("[green]Paris[/green]")
print("\n")
print(tree)

# Syntax highlighting
code = '''
def greet(name):
    """A simple greeting function"""
    print(f"Hello, {name}!")

greet("World")
'''
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
print("\n[underline]Syntax Highlighting Example:[/underline]")
print(syntax)

# Markdown rendering
markdown_text = """
# Rich Markdown Support

## Basic Formatting
- **Bold text**
- *Italic text*
- `Code snippets`

## Lists
1. First item
2. Second item
3. Third item

[Link to Rich repository](https://github.com/Textualize/rich)
"""
print("\n[underline]Markdown Rendering:[/underline]")
print(Markdown(markdown_text))