# Morse Code Converter

A simple Python program that converts English text to Morse code. The program is user-friendly, handles corner cases like empty input and unsupported characters, and allows users to rerun the program without restarting it.

---

## Features

- Converts English text (letters, numbers, and some special characters) into Morse code.
- Handles empty inputs gracefully with a clear message.
- Replaces unsupported symbols with a placeholder (`?`).
- Allows the user to rerun the program or exit at any time.
- Modular design for easy maintenance and enhancement.

---

## Morse Code Reference

The program uses the following Morse code mappings for conversion:

| Character | Morse Code | Character | Morse Code |
|-----------|------------|-----------|------------|
| A         | .-         | N         | -.         |
| B         | -...       | O         | ---        |
| C         | -.-.       | P         | .--.       |
| D         | -..        | Q         | --.-       |
| E         | .          | R         | .-.        |
| F         | ..-.       | S         | ...        |
| G         | --.        | T         | -          |
| H         | ....       | U         | ..-        |
| I         | ..         | V         | ...-       |
| J         | .---       | W         | .--        |
| K         | -.-        | X         | -..-       |
| L         | .-..       | Y         | -.--       |
| M         | --         | Z         | --..       |

Special characters like numbers, punctuation, and spaces are also supported. Unsupported symbols are replaced with `?`.

---

## Usage

### Prerequisites
- Python 3.x installed on your system.

### How to Run
1. Clone or download the script file to your local machine.
2. Open a terminal or command prompt in the program's directory.
3. Run the program using the following command:
   ```bash
   python morse_code_converter.py
   ```

### Input Instructions
- Enter any text in English. The program will convert it to Morse code.
- Type `exit` to quit the program.

---

## Example Usage

### Input:
```plaintext
Enter your text in English (or type 'exit' to quit): Hello World!
```

### Output:
```plaintext
Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--
```

### Input:
```plaintext
Enter your text in English (or type 'exit' to quit): 😊
```

### Output:
```plaintext
Morse Code: ?
```

### Input:
```plaintext
Enter your text in English (or type 'exit' to quit): 
```

### Output:
```plaintext
Input is empty. Please enter valid text.
```

---

## How It Works

1. **Text Input**: Accepts user input and removes leading/trailing whitespace.
2. **Conversion**: Maps each character in the input string to its Morse code equivalent using a predefined dictionary.
3. **Unknown Characters**: Replaces unsupported characters with `?`.
4. **Output**: Displays the Morse code equivalent of the input text.
5. **Repeat**: Allows the user to enter more text or exit the program.

---

## File Structure

- **morse_code_converter.py**: The main script containing the Morse code dictionary, conversion logic, and program flow.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---



---

## Future Enhancements

- Add support for decoding Morse code back to English text.
- Provide an option to save the Morse code output to a file.
- Add a GUI interface for better user experience.

