# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', 
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.', ' ': '/'  
}

def text_to_morse(text):
    """
    Converts English text to Morse code.
    Handles unknown symbols and empty input gracefully.
    """
    if not text.strip():  # Check for empty or whitespace-only input
        return "Input is empty. Please enter valid text."
    
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Placeholder for unknown symbols
    
    return ' '.join(morse_code)

def main():
    
    while True:
        # Get user input
        user_input = input("Enter your text in English (or type 'exit' to quit): ").strip()
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Convert to Morse code and display result
        morse_code = text_to_morse(user_input)
        print(f"Morse Code: {morse_code}\n")

if __name__ == "__main__":
    main()
