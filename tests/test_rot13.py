import pytest
from app.cipher import rot13_encrypt, rot13_decrypt


def test_rot13_encrypt_basic():
    assert rot13_encrypt("abc") == "nop"


def test_rot13_decrypt_basic():
    assert rot13_decrypt("nop") == "abc"


def test_rot13_double_encrypt():
    text = "hello"
    assert rot13_encrypt(rot13_encrypt(text)) == text


def test_rot13_encrypt_decrypt_cycle():
    text = "Python"
    encrypted = rot13_encrypt(text)
    decrypted = rot13_decrypt(encrypted)
    assert decrypted == text


def test_rot13_with_uppercase():
    assert rot13_encrypt("AbC") == "NoP"


def test_rot13_with_spaces():
    assert rot13_encrypt("hello world") == "uryyb jbeyq"


def test_rot13_with_symbols():
    assert rot13_encrypt("hello! 123") == "uryyb! 123"


def test_rot13_empty():
    assert rot13_encrypt("") == ""
    assert rot13_decrypt("") == ""


if __name__ == "__main__":
    pytest.main()
