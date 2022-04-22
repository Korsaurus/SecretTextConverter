from typing import Callable


class Converter:

    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.morse_alphabet = {
                "a": ".-", "b": "-...", "c": "-.-.", "d": '-..', "e": '.', "f": "..-.", "g": "--.", "h": "....",
                "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ".": ".-.-.-", ",": "--..--",
                ":": "---...", "?": "..--..", "'": ".----.", "-": "-....-", "/": "-..-.", ")": "-.--.-", "(": "-.--.",
                '"': ".-..-.", "!": "-.-.--", "@": ".--.-.", "=": "-...-", "&": ".-...", ";": "-.-.-.", "+": ".-.-.",
                "_": "..--.-", "$": "...-..- "
            }

    # MORSE SECTION

    def convert_to_morse(self, text: str):
        new_message = ""

        for char in text.lower():
            if char == " ":
                new_message += "    "

            #   The rules for international morse code are that words are separated by 7 spaces and letters by 3,

            if char != " ":
                new_message += self.morse_alphabet[char]
                new_message += "   "
        return new_message

    def format_morse(self, code: str):

        # Formats it so if there are 4 or more spaces a | is added to the list to later be replaced by a space
        # in the final string

        # Without the follow line unless there's a space at the end of the inputted morse code, it won't add the final
        # "letter" to the list. This is just a simple way to make sure the last letter is always added
        code += " "
        space_counter = 0
        formatted_code = []
        current_word = ""
        for idx, char in enumerate(code):
            if space_counter >= 4 and char != " ":
                formatted_code.append("|")
                space_counter = 0
            if char != " ":
                current_word += char
                space_counter = 0
            if char == " " and current_word:
                formatted_code.append(current_word)
                current_word = ""
            # The space counter needs to be in a separate condition in order to make sure it doesn't get messed with.
            if char == " ":
                space_counter += 1
        return formatted_code

    def convert_from_morse(self, code: str):
        new_message = ""
        formatted_code = self.format_morse(code)
        print(formatted_code)

        for item in formatted_code:
            for key, value in self.morse_alphabet.items():
                if item == value:
                    new_message += key
            if item == "|":
                new_message += " "

        return new_message

    # END OF MORSE SECTION

    @staticmethod
    def encode(text: str, cipher: Callable) -> str:
        converted_text = cipher(text)
        return converted_text

    @staticmethod
    def decode(code: str, decoder):
        converted_text = decoder(code)
        return converted_text
