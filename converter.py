from typing import Callable


class Converter:

    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.symbols = [".", ",", ":", "?", "'", "-", "/", "(", ")", '"', "!", "@", "=", "&", ";", "+", "_", "$"]
        self.morse_alphabet = {
            "letters": [".-", "-...", "-.-.", '-..', '.', "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."],
            "numbers": [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"],
            "symbols": {
                ".": ".-.-.-",
                ",": "--..--",
                ":": "---...",
                "?": "..--..",
                "'": ".----.",
                "-": "-....-",
                "/": "-..-.",
                ")": "-.--.-",
                "(": "-.--.",
                '"': ".-..-.",
                "!": "-.-.--",
                "@": ".--.-.",
                "=": "-...-",
                "&": ".-...",
                ";": "-.-.-.",
                "+": ".-.-.",
                "_": "..--.-",
                "$": "...-..-"
            }
        }


    # MORSE SECTION

    def convert_to_morse(self, text: str):
        new_message = ""

        for char in text.lower():
            if char == " ":
                new_message += "    "

            #   The rules for international morse code are that words are separated by 7 spaces and letters by 3,
            #   Since 3 spaces are added after every letter, and it's way too verbose to add a condition to each
            #   if to check whether the next character is a space and to then not add the 3 spaces and instead add 7,
            #   I decided to just add 4 if there's a space.

            if char in self.alphabet:
                letter_idx = self.alphabet.index(char)
                morse_letter = self.morse_alphabet["letters"][letter_idx]
                new_message += morse_letter
                new_message += "   "
            if char in self.numbers:
                num_idx = self.numbers.index(char)
                morse_num = self.morse_alphabet["numbers"][num_idx]
                new_message += morse_num
                new_message += "   "
            if char in self.symbols:
                morse_sym = self.morse_alphabet["symbols"][char]
                new_message += morse_sym
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

            if item in self.morse_alphabet["letters"]:
                item_idx = self.morse_alphabet["letters"].index(item)
                letter = self.alphabet[item_idx]
                new_message += letter
            if item in self.morse_alphabet["numbers"]:
                item_idx = self.morse_alphabet["numbers"].index(item)
                number = self.numbers[item_idx]
                new_message += number
            if item in self.morse_alphabet["symbols"].values():
                for key, value in self.morse_alphabet["symbols"].items():
                    if item == value:
                        new_message += key
            if item == "|":
                new_message += " "

        return new_message

    # END OF MORSE SECTION

    @staticmethod
    def convert(text: str, cipher: Callable) -> str:
        converted_text = cipher(text)
        return converted_text

    @staticmethod
    def convert_from(code: str, decoder):
        converted_text = decoder(code)
        return converted_text
