import os


def count_words_and_sentences(file_path: str) -> tuple[int, int]:
    """
    This function reads the content of a ".txt" file and returns the number of words and sentences in the file.

    Args:
        file_path: Path to the ".txt" file.

    Returns:
        Tuple: Number of words (int) and number of sentences (int).
    """
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read the file content
            text = file.read()
            words = 0
            sentences = 0
            for word in text.split():
                if word:
                    words += 1

            for punctuation in [".", "!", "?", "..."]:
                sentences += text.count(punctuation)

            return words, sentences
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


def main():
    # Get the file path
    file_path = os.path.join("text.txt")

    # Count words and sentences
    word_count, sentence_count = count_words_and_sentences(file_path)

    # Print the results
    if word_count is not None and sentence_count is not None:
        print("Number of words in the file:", word_count)
        print("Number of sentences in the file:", sentence_count)


if __name__ == "__main__":
    main()
