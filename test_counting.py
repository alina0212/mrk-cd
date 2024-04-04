import pytest
import os
from main import count_words_and_sentences


@pytest.fixture(scope="module")
def create_test_files():
    """
    Creates test files (empty.txt, single_word.txt, multiple_words_no_punctuation.txt, multiple_words_with_punctuation.txt)
    before tests and removes them afterward.
    """
    file_paths = [
        "empty.txt",
        "single_word.txt",
        "multiple_words_no_punctuation.txt",
        "multiple_words_with_punctuation.txt",
    ]
    # Записуємо вміст файлів
    with open("empty.txt", "w") as file:
        pass  # Нічого не записуємо, файл залишається порожнім

    with open("single_word.txt", "w") as file:
        file.write("Hello!")

    with open("multiple_words_no_punctuation.txt", "w") as file:
        file.write("This is a test.")

    with open("multiple_words_with_punctuation.txt", "w") as file:
        file.write("This is a test. Hello, world!")

    yield  # Execute tests

    for file_path in file_paths:
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist


@pytest.mark.parametrize(
    "file_path, expected_words, expected_sentences",
    [
        ("empty.txt", 0, 0),
        ("single_word.txt", 1, 1),
        ("multiple_words_no_punctuation.txt", 4, 1),
        ("multiple_words_with_punctuation.txt", 6, 2),
    ],
)
def test_count_words_and_sentences(file_path, expected_words, expected_sentences, create_test_files):
    words_count, sentences_count = count_words_and_sentences(file_path)
    assert words_count == expected_words
    assert sentences_count == expected_sentences


