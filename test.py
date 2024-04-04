import pytest
import os
from main import count_words_and_sentences


@pytest.fixture
def txt_file(tmp_path):
    # Create a temporary text file
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w') as file:
        file.write("This is a test sentence. Another test sentence! How many words are here?")
    return file_path


@pytest.mark.parametrize("input_text, expected_words, expected_sentences", [
    ("", 0, 0),
    ("This is a test.", 4, 1),
    ("One. Two! Three?", 3, 3),
    ("No spaces", 2, 1)
])
def test_count_words_and_sentences(tmp_path, input_text, expected_words, expected_sentences):
    # Create a temporary text file with the input text
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w') as file:
        file.write(input_text)

    # Call the function and check the result
    words, sentences = count_words_and_sentences(file_path)
    assert words == expected_words
    assert sentences == expected_sentences


def test_count_words_and_sentences_with_fixture(txt_file):
    # Call the function with the fixture and check the result
    words, sentences = count_words_and_sentences(txt_file)
    assert words == 10
    assert sentences == 3
