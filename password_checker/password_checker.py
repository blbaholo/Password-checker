import re
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

file_handler = logging.FileHandler("errors.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def password_exists(user_input):
    if user_input == "":
        return False
    return True


def password_length(user_input):
    if len(user_input) <= 8:
        return False
    return True


def password_whitespace_char_check(user_input):
    whitespace_char = r" "
    if re.search(whitespace_char, user_input) == None:
        return False
    return True


def password_special_char_check(user_input):
    special_char = r"[-,!.~`)(*_@;#$+%/><}{^=&:]"
    if re.search(special_char, user_input) == None:
        return False
    return True


def password_digits_check(user_input):
    numbers = r"\d"
    if re.search(numbers, user_input) == None:
        return False
    return True


def password_lowercase_letter_check(user_input):
    lowercase_letter = r"[a-z]"
    if re.search(lowercase_letter, user_input) == None:
        return False
    return True


def password_uppercase_letter_check(user_input):
    uppercase_letter = r"[A-Z]"
    if re.search(uppercase_letter, user_input) == None:
        return False
    return True


def checking_errors(user_input):
    counter = 0
    if password_exists(user_input):
        counter += 1
    if password_length(user_input):
        counter += 1
    if password_whitespace_char_check(user_input):
        counter += 1
    if password_special_char_check(user_input):
        counter += 1
    if password_digits_check(user_input):
        counter += 1
    if password_lowercase_letter_check(user_input):
        counter += 1
    if password_uppercase_letter_check(user_input):
        counter += 1
    return counter


def log_message():
    return logger.debug("User password is not valid")


def password_is_valid(user_input):
    if not password_exists(user_input):
        log_message()
        logger.error("Password should exist")
        raise ValueError("Password should exist")
    if not password_length(user_input):
        log_message()
        logger.error("Password should be longer than 8 characters")
        raise ValueError("Password should be longer than 8 characters")
    if not password_whitespace_char_check(user_input):
        log_message()
        logger.error("Password should have at least one whitespace character")
        raise ValueError("Password should have at least one whitespace character")
    if not password_special_char_check(user_input):
        log_message()
        logger.error("Password should have at least one special character")
        raise ValueError("Password should have at least one special character")
    if not password_digits_check(user_input):
        log_message()
        logger.error("Password should have at least one digit")
        raise ValueError("Password should have at least one digit")
    if not password_lowercase_letter_check(user_input):
        log_message()
        logger.error("Password should have at least one lowercase letter")
        raise ValueError("Password should have at least one lowercase letter")
    if not password_uppercase_letter_check(user_input):
        log_message()
        logger.error("Password should have at least one uppercase letter")
        raise ValueError("Password should have at least one uppercase letter")
    return logger.debug("User password is valid")


def password_strength(user_input):
    if not password_exists(user_input) or not password_length(user_input):
        return "invalid"
    if checking_errors(user_input) == 3:
        return "weak"
    if checking_errors(user_input) >= 4 and checking_errors(user_input) < 6:
        return "medium"
    if checking_errors(user_input) >= 6:
        return "strong"
