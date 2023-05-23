from .main import process_line, MSG_MULTIPLE_DE_5, MSG_RIEN_A_AFFICHER

def test_process_line_multiple_of_5():
    assert process_line("some line", 5) == MSG_MULTIPLE_DE_5

def test_process_line_contains_substitution_character():
    assert process_line("some line with $spaces$", 1) == "some_line_with_$spaces$" 

def test_process_line_ends_with_period():
    assert process_line("some line.", 2) == "some line."

def test_process_line_json():
    assert process_line('{"key": "value"}', 2) == '{"key": "value", "pair": true}'

def test_process_line_invalid_json():
    assert process_line('{invalid}', 4) == MSG_RIEN_A_AFFICHER

def test_process_line_default():
    assert process_line("some other line", 6) == MSG_RIEN_A_AFFICHER
