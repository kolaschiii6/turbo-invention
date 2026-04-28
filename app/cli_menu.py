import time
import questionary
from app.cipher import caesar_cipher, rot13_decrypt, rot13_encrypt
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

console = Console()

ACTIONS = [
    "Encrypt (Caesar)",
    "Decrypt (Caesar)",
    "Encrypt (ROT13)",
    "Decrypt (ROT13)",
    "Exit",
]


def ask_with_fallback(message, choices=None, default=None):
    try:
        if choices is not None:
            return questionary.select(message, choices=choices).ask()
        return questionary.text(message, default=default or "").ask()
    except Exception:
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
        value = input("Select a number: ").strip()

        try:
            selected_index = int(value)
        except ValueError:
            console.print("[bold red]Error: enter a number from the list.[/bold red]")
            continue

        if 1 <= selected_index <= len(choices):
            return choices[selected_index - 1]

        console.print("[bold red]Error: enter a number from the list.[/bold red]")


def wait_for_user():
    input("\nPress Enter to finish...")


def main():
    console.print(Panel.fit("[bold blue]Password Encryption[/bold blue]", border_style="cyan"))

    action = ask_with_fallback(
        "What do you want to do?",
        choices=ACTIONS,
    )

    if action == "Exit" or action is None:
        console.print("[bold red]Goodbye![/bold red]")
        wait_for_user()
        return

    text = ask_with_fallback("Enter text:")
    if text is None:
        wait_for_user()
        return

    result = ""

    if "Caesar" in action:
        shift_str = ask_with_fallback("Enter shift (number):", default="3")

        try:
            shift = int(shift_str)
        except (ValueError, TypeError):
            console.print("[bold red]Error: Shift must be a number![/bold red]")
            wait_for_user()
            return

        mode = "encrypt" if "Encrypt" in action else "decrypt"
        result = caesar_cipher(text, shift, mode=mode)

    elif "ROT13" in action:
        if "Encrypt" in action:
            result = rot13_encrypt(text)
        else:
            result = rot13_decrypt(text)

    for step in track(range(10), description=f"[green]Processing ({action})..."):
        time.sleep(0.05)

    console.print(
        Panel(
            f"[bold yellow]Your text:[/bold yellow]\n\n{result}",
            title="Success",
            border_style="green",
        )
    )
    wait_for_user()


if __name__ == "__main__":
    main()
