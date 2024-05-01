import pytest
from password_checker.password_checker import password_is_valid


def test_password_exists():
    with pytest.raises(ValueError, match=r"Password should exist"):
        password_is_valid("")


def test_password_length():
    with pytest.raises(
        ValueError, match=r"Password should be longer than 8 characters"
    ):
        password_is_valid("eyqter ")


def test_password_contains_special_character():
    with pytest.raises(
        ValueError, match=r"Password should have at least one special character"
    ):
        password_is_valid("ahdyQW 45Tfh")


def test_password_contains_whitespace_character():
    with pytest.raises(
        ValueError, match=r"Password should have at least one whitespace character"
    ):
        password_is_valid("gatRWT63g@")


def test_password_contains_numbers():
    with pytest.raises(ValueError, match=r"Password should have at least one digit"):
        password_is_valid("gdwhvQWAR *^")


def test_password_contains_lowercase_letter():
    with pytest.raises(
        ValueError, match=r"Password should have at least one lowercase letter"
    ):
        password_is_valid("QRETR546 725%$")


def test_password_contains_uppercase_letter():
    with pytest.raises(
        ValueError, match=r"Password should have at least one uppercase letter"
    ):
        password_is_valid("usytevh 23@!cvh")


def test_password_is_valid(caplog):
    password_is_valid("QWErty 3#7")
    assert "User password is valid" in caplog.text
