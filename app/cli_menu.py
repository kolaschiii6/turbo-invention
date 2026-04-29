import time
import questionary
from app.cipher import caesar_cipher, rot13_decrypt, rot13_encrypt
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.table import Table
from rich.align import Align

console = Console()

BANNER = r"""
 _____         _     _____                       _   _
|_   _|____  _| |_  | ____|_ __   ___ _ __ _   _| |_(_) ___  _ __
  | |/ _ \ \/ / __| |  _| | '_ \ / __| '__| | | | __| |/ _ \| '_ \
  | |  __/>  <| |_  | |___| | | | (__| |  | |_| | |_| | (_) | | | |
  |_|\___/_/\_\\__| |_____|_| |_|\___|_|   \__, |\__|_|\___/|_| |_|
                                           |___/
"""

ACTIONS = [
    "Encrypt (Caesar)",
    "Decrypt (Caesar)",
    "Encrypt (ROT13)",
    "Decrypt (ROT13)",
    "About",
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


def show_header():
    console.clear()
    console.print(Align.center(f"[bold cyan]{BANNER}[/bold cyan]"))
    console.print(
        Align.center(
            "[dim]Caesar cipher & ROT13 — turbo-invention CLI[/dim]\n"
        )
    )


def show_about():
    body = (
        "[bold]Caesar cipher[/bold] — shifts every letter by N positions in the alphabet.\n"
        "  Example: shift=3 → 'abc' becomes 'def'.\n\n"
        "[bold]ROT13[/bold] — a Caesar cipher with a fixed shift of 13.\n"
        "  Applying ROT13 twice returns the original text.\n\n"
        "[dim]Tip: only Latin letters are transformed, other characters stay as-is.[/dim]"
    )
    console.print(
        Panel(body, title="About", border_style="cyan", padding=(1, 2))
    )


def render_result(action, original, result, shift):
    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold cyan", justify="right")
    table.add_column()

    table.add_row("Action:", f"[white]{action}[/white]")
    if shift is not None:
        table.add_row("Shift:", f"[white]{shift}[/white]")
    table.add_row("Length:", f"[white]{len(original)} chars[/white]")
    table.add_row("Original:", f"[yellow]{original}[/yellow]")
    table.add_row("Result:", f"[bold green]{result}[/bold green]")

    return Panel(
        table,
        title="Result",
        subtitle=f"[dim]{action}[/dim]",
        border_style="green",
        padding=(1, 2),
    )


def main():
    while True:
        show_header()

        action = ask_with_fallback(
            "What do you want to do?",
            choices=ACTIONS,
        )

        if action == "Exit" or action is None:
            console.print("[bold cyan]Goodbye![/bold cyan]")
            wait_for_user()
            break

        if action == "About":
            show_about()
            wait_for_user()
            continue

        text = ask_with_fallback("Enter text:")
        if text is None:
            continue

        if not text.strip():
            console.print("[bold red]Error: text is empty — nothing to process.[/bold red]")
            wait_for_user()
            continue

        result = ""
        shift_value = None

        if "Caesar" in action:
            shift_str = ask_with_fallback("Enter shift (number):", default="3")

            try:
                shift = int(shift_str)
            except (ValueError, TypeError):
                console.print(
                    f"[bold red]Error: shift must be a whole number (got '{shift_str}').[/bold red]"
                )
                wait_for_user()
                continue

            shift_value = shift
            mode = "encrypt" if "Encrypt" in action else "decrypt"
            result = caesar_cipher(text, shift, mode=mode)

        elif "ROT13" in action:
            if "Encrypt" in action:
                result = rot13_encrypt(text)
            else:
                result = rot13_decrypt(text)

        for step in track(range(10), description=f"[green]Processing ({action})..."):
            time.sleep(0.05)

        console.print(render_result(action, text, result, shift_value))
        wait_for_user()


if __name__ == "__main__":
    main()
