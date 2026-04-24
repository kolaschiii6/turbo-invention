import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
import questionary
console = Console()
def main():
    console.print(Panel.fit("[bold blue]Szyfrowanie haseł[/bold blue]", border_style="cyan"))
    action = questionary.select(
        "Co chcesz zrobić?",
        choices=[
            "Szyfruj tekst",
            "Deszyfruj tekst",
            "Wyjdź"
        ]
    ).ask()
if action == "Wyjdź":
        console.print("[bold red]Do widzenia![/bold red]")
        return
    text = questionary.text("Wprowadź tekst:").ask()
    for step in track(range(10), description=f"[green]Przetwarzanie ({action})..."):
        time.sleep(0.1)
    console.print(Panel(f"[bold yellow]Twój tekst:[/bold yellow]\n\n{text}", title="Sukces", border_style="green"))
if __name__ == "__main__":
    main()
