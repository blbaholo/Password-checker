from password_checker.password_checker import password_strength


def test_incorrect_password_length():
    assert password_strength("wasq") == "invalid"


def test_password_exists():
    assert password_strength("") == "invalid"


def test_output_for_3_conditions_met():
    assert password_strength("awerviyua") == "weak"


def test_output_for_4_conditions_met():
    assert password_strength("awerviQua") == "medium"


def test_output_for_5_conditions_met():
    assert password_strength("awer1viQua") == "medium"


def test_output_for_6_conditions_met():
    assert password_strength("#wer1viQua") == "strong"


def test_output_for_7_conditions_met():
    assert password_strength("#wer1 viQua") == "strong"
