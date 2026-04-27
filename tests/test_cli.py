import pytest
import app.cli_menu as cli
from app.cipher import caesar_cipher, rot13_encrypt, rot13_decrypt


def test_ask_plain_text(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "hello")

    result = cli.ask_plain("Введите текст:")
    assert result == "hello"


def test_ask_plain_default(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")

    result = cli.ask_plain("Введите текст:", default="default_value")
    assert result == "default_value"


def test_ask_plain_choices(monkeypatch):
    inputs = iter(["2"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = cli.ask_plain(
        "Выбери:",
        choices=["A", "B", "C"]
    )

    assert result == "B"


def test_main_caesar_encrypt(monkeypatch):
    inputs = iter([
        "Szyfruj (Caesar)",  # action
        "test",              # text
        "5"                 # shift
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr(cli, "caesar_cipher", lambda t, s, mode: f"{t}-encrypted")

    monkeypatch.setattr(cli, "ask_with_fallback", lambda *args, **kwargs: next(inputs))

    cli.main()


def test_main_rot13_encrypt(monkeypatch):
    inputs = iter([
        "Szyfruj (ROT13)",
        "hello"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr(cli, "rot13_encrypt", lambda t: "rot13-result")
    monkeypatch.setattr(cli, "rot13_decrypt", lambda t: "rot13-result")

    monkeypatch.setattr(cli, "ask_with_fallback", lambda *args, **kwargs: next(inputs))

    cli.main()


def test_exit(monkeypatch):
    monkeypatch.setattr(cli, "ask_with_fallback", lambda *args, **kwargs: "Wyjdź")

    result = cli.main()
    assert result is None

