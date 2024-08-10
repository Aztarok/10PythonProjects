from difflib import SequenceMatcher
from datetime import datetime

class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses
    
    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()

    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity: float = 0.0
        best_match: str = "Sorry, I didn\'t understand that."

        for response in self.responses:
            similarity: float = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = self.responses[response]

        return best_match, highest_similarity

    def run(self) -> None:
        print(f"Hello, My name is {self.name}, how can I help you today?")

        while True:
            user_input: str = input("You: ")
            response, similarity = self.get_best_response(user_input)
            
            if response == "GET_TIME":
                response = f"The time is {datetime.now():%H:%M}"

            if user_input.lower() == "bye":
                print(f"{self.name}: {response} (Similarity: {similarity:.2%})")
                break

            if similarity < 0.5:
                print(f"{self.name}: Sorry, I didn\'t understand what you wrote. Please try with a different message.")
            else:
                print(f"{self.name}: {response} (Similarity: {similarity:.2%})")

def main() -> None:
    responses: dict[str, str] = {
        "hello": "Hello! How are you today?",
        "hi": "Hey! Nice to meet you!",
        "how are you": "I am doing well, thank you!",
        "what time is it": "GET_TIME",
        "bye": "Goodbye! Have a nice day!",
        "I want to leave": "Type bye if you want to stop chatting :(",
    }
    chatbot: ChatBot = ChatBot("Alex", responses)
    chatbot.run()

if __name__ == "__main__":
    main()