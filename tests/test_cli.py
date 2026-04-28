import app.cli_menu as cli


def test_ask_plain_text(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "hello")

    result = cli.ask_plain("Enter text:")
    assert result == "hello"


def test_ask_plain_default(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")

    result = cli.ask_plain("Enter text:", default="default_value")
    assert result == "default_value"


def test_ask_plain_choices(monkeypatch):
    inputs = iter(["2"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = cli.ask_plain(
        "Choose:",
        choices=["A", "B", "C"],
    )

    assert result == "B"


def test_main_caesar_encrypt(monkeypatch):
    monkeypatch.setattr(cli, "wait_for_user", lambda: None)
    inputs = iter([
        "Encrypt (Caesar)",
        "test",
        "5",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr(
        cli,
        "caesar_cipher",
        lambda text, shift, mode: f"{text}-encrypted",
    )

    monkeypatch.setattr(
        cli,
        "ask_with_fallback",
        lambda *args, **kwargs: next(inputs),
    )

    cli.main()


def test_main_rot13_encrypt(monkeypatch):
    monkeypatch.setattr(cli, "wait_for_user", lambda: None)
    inputs = iter([
        "Encrypt (ROT13)",
        "hello",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr(cli, "rot13_encrypt", lambda text: "rot13-result")
    monkeypatch.setattr(cli, "rot13_decrypt", lambda text: "rot13-result")

    monkeypatch.setattr(
        cli,
        "ask_with_fallback",
        lambda *args, **kwargs: next(inputs),
    )

    cli.main()


def test_exit(monkeypatch):
    monkeypatch.setattr(cli, "wait_for_user", lambda: None)
    monkeypatch.setattr(
        cli,
        "ask_with_fallback",
        lambda *args, **kwargs: "Exit",
    )

    result = cli.main()
    assert result is None
