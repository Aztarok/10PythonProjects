morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', "-" : '-....-', "." : '.-.-.-', "?" : '..--..', "!" : '-.-.--', "," :	'--..--', "\'" : '.----.', "/" : '-..-.', "&" : '.-...', ":" : '---...',
    ";" : '-.-.-.', "\"" : '.-..-.',
    "@" : '.--.-.',
    "$" : '...-..-',
    "=" : '-...-',
    "+" : '.-.-.',
    "_" : '..--.-',
    "(" : '-.--.',
    ")" : '-.--.-'

}

def convert_to_morse(text: str) -> str:
    return " ".join(morse_code_dict.get(char.upper(), "") for char in text)

def convert_to_text(morse_code: str) -> str:
    reverse_morse_code_dict: dict[str, str] = {value: key for key, value in morse_code_dict.items()}
    return "".join(reverse_morse_code_dict.get(char, "") for char in morse_code.split())

def main() -> None:
    morse_or_text: bool = input("Convert to morse or text? (m/t): ").lower() == "m"
    print(morse_or_text)
    if morse_or_text:
        morse_code: str = input("Enter morse code: ")
        output: str = convert_to_text(morse_code)
        print(output)
    else:
        user_input: str = input("Enter Text: ")
        output: str = convert_to_morse(user_input)
        print(output)

if __name__ == "__main__":
    main()