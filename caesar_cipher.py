# A simple casear cypher that takes text and a shift value and outputs 
# a coded message. Messages can be decoded using a negative value
# (ex. original shift == 5, so decode shift should == -5)

# Used for the shift_word function below
def shift_character(char: str, shift: int) -> str:
    # Set newletter to current character so that characters not in the list will stay the same
    if not char.isalpha():
        return char

    # Determine ASCII base ('A' or 'a')
    base = ord("A") if char.isupper() else ord("a")

    # Calculate shifted ASCII code
    shifted_code = base + (ord(char) - base + shift) % 26
    return chr(shifted_code)

def shift_word(text: str, shift: int) -> str:
    ciphertext = ""
    return "".join(shift_character(char, shift) for char in text)

def run_cypher() -> None:
    plaintext = input("Plaintext: ")
    shift = int(input("Shift value: "))
    print(f"Ciphertext: {shift_word(plaintext, shift)}")

if __name__ == "__main__":
    run_cypher()
