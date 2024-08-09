from collections import Counter
import re

def open_file(path: str) -> str:
    with open(path, "r") as file:
        text: str = file.read()
        return text

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text = text.lower()
    words: list[str] = re.findall(r"\b\w+\b", lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common()

def analyse(text: str) -> dict[str, int]:
    print(f"\"{text}\"")
    word_frequencies: list[tuple[str, int]] = get_frequency(text)
    print("Top 5 most common words:")
    for i in range(len(word_frequencies)):
        word: str = word_frequencies[i][0]
        count: int = word_frequencies[i][1]
        print(f"{word}: {count}")
        if i >= 5:
            break
    result: dict[str, int] = {
        "total_characters_including_spaces": len(text),
        "total_characters_excluding_spaces": len(text.replace(" ", "")),
        "total_spaces": text.count(" "),
        "total_words": len(text.split()),
    }

    return result

def main() -> None:
    text: str = open_file("note.txt")
    analysis: dict[str, int] = analyse(text)

    for key, value in analysis.items():
        
        # print(f"{key}: {value}")
        # This is more human readable
        print(f"This text file contains {value} total {key.replace('_', ' ')}.")

if __name__ == "__main__":
    main()