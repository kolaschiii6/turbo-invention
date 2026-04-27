import time
import questionary
from app.cipher import caesar_cipher, rot13_decrypt, rot13_encrypt
from prompt_toolkit.output.win32 import NoConsoleScreenBufferError
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

console = Console()

ACTIONS = [
    "Szyfruj (Caesar)",
    "Deszyfruj (Caesar)",
    "Szyfruj (ROT13)",
    "Deszyfruj (ROT13)",
    "Wyjdź",
]


def ask_with_fallback(message, choices=None, default=None):
    try:
        if choices is not None:
            return questionary.select(message, choices=choices).ask()
        return questionary.text(message, default=default or "").ask()
    except NoConsoleScreenBufferError:
        return ask_plain(message, choices=choices, default=default)


def ask_plain(message, choices=None, default=None):
    if choices is None:
        prompt = f"{message} "
        if default is not None:
            prompt += f"[{default}] "

        value = input(prompt).strip()
        return value if value else default

    console.print(f"\n[bold cyan]{message}[/bold cyan]")
    for index, choice in enumerate(choices, start=1):
        console.print(f"{index}. {choice}")

    while True:
        value = input("Wybierz numer: ").strip()

        try:
            selected_index = int(value)
        except ValueError:
            console.print("[bold red]Błąd: wpisz numer z listy.[/bold red]")
            continue

        if 1 <= selected_index <= len(choices):
            return choices[selected_index - 1]

        console.print("[bold red]Błąd: wybrano nieprawidłową opcję.[/bold red]")


def main():
    console.print(Panel.fit("[bold blue]Szyfrowanie haseł[/bold blue]", border_style="cyan"))

    action = ask_with_fallback(
        "Co chcesz zrobić?",
        choices=ACTIONS,
    )

    if action == "Wyjdź" or action is None:
        console.print("[bold red]Do widzenia![/bold red]")
        return

    text = ask_with_fallback("Wprowadź tekst:")
    if text is None:
        return

    result = ""

    if "Caesar" in action:
        shift_str = ask_with_fallback("Wprowadź przesunięcie (liczbę):", default="3")

        try:
            shift = int(shift_str)
        except (ValueError, TypeError):
            console.print("[bold red]Błąd: Przesunięcie musi być liczbą![/bold red]")
            return

        mode = "encrypt" if "Szyfruj" in action else "decrypt"
        result = caesar_cipher(text, shift, mode=mode)

    elif "ROT13" in action:
        if "Szyfruj" in action:
            result = rot13_encrypt(text)
        else:
            result = rot13_decrypt(text)

    for step in track(range(10), description=f"[green]Przetwarzanie ({action})..."):
        time.sleep(0.05)

    console.print(
        Panel(
            f"[bold yellow]Twój tekst:[/bold yellow]\n\n{result}",
            title="Sukces",
            border_style="green",
        )
    )


if __name__ == "__main__":
    main()
