import pytest
from app.cipher import caesar_cipher


#SZYFROWANIE
def test_caesar_encrypt_basic():
    assert caesar_cipher("abc", 1) == "bcd"


def test_caesar_encrypt_wrap():
    assert caesar_cipher("xyz", 3) == "abc"


def test_caesar_encrypt_with_spaces():
    assert caesar_cipher("abc xyz", 2) == "cde zab"


def test_caesar_encrypt_empty():
    assert caesar_cipher("", 5) == ""


def test_caesar_encrypt_large_shift():
    assert caesar_cipher("abc", 27) == "bcd"


#DESZYFROWANIE
def test_caesar_decrypt_basic():
    assert caesar_cipher("bcd", 1, "decrypt") == "abc"


def test_caesar_decrypt_wrap():
    assert caesar_cipher("abc", 3, "decrypt") == "xyz"


def test_caesar_decrypt_with_spaces():
    assert caesar_cipher("cde zab", 2, "decrypt") == "abc xyz"


def test_caesar_decrypt_empty():
    assert caesar_cipher("", 10, "decrypt") == ""


#SKOMPLIKOWANE
def test_encrypt_decrypt_cycle():
    text = "hello world"
    shift = 5
    encrypted = caesar_cipher(text, shift)
    decrypted = caesar_cipher(encrypted, shift, "decrypt")
    assert decrypted == text


def test_encrypt_decrypt_different_shifts():
    text = "python"
    for shift in range(1, 10):
        assert caesar_cipher(caesar_cipher(text, shift), shift, "decrypt") == text

if __name__ == "__main__":
    pytest.main()