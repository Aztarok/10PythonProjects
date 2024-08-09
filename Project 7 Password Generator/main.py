import secrets
import string

class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # Get characters from string module
        self.base_characters: str = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation
    
    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))
        
        return "".join(password)
    
    def strength(self) -> str:
        strength: str = "weak"

        if (self.use_uppercase and self.use_symbols) and self.length > 16:
            strength = "strong"
        elif (self.use_uppercase or self.use_symbols) and self.length > 12:
            strength = "medium"
        
        return strength
    
def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=True)
    for i in range(10):
        generated: str = password.generate()
        strength: str = password.strength()
        print(f"Generated password: {generated} ({len(generated)} chars) Strength of password: ({strength})")

if __name__ == "__main__":
    main()