from collections import Counter
import re

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text = text.lower()
    words: list[str] = re.findall(r"\b\w+\b", lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common()
def enter_text(text) -> None:
    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    for word, count in word_frequencies:
        print(f"{word}: {count}")
def main() -> None:
    file_check: bool = input("Are you entering text from a file? (y/n): ").lower() == "y"
    if file_check:
        filename: str = input("Enter the filename: ").strip()
        file = open(filename, "r")
        enter_text(file.read())
        
    else:
        text: str = input("Enter your text: ").strip()
        enter_text(text)
        

if __name__ == "__main__":
    main()