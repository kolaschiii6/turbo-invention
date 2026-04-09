from rich.console import Console
from rich.panel import Panel
console = Console()
def main():
    console.print(Panel.fit("[bold blue]Szyfrowanie haseł[/bold blue]", border_style="cyan"))
if __name__ == "__main__":
    main()
