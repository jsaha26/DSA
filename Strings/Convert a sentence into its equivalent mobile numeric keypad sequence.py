def sentence_to_keypad_sequence(input_str):
    # Define the mapping of characters to keypad numbers
    char_to_number = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
        ' ': '0'
    }
    
    # Initialize the result sequence as a list
    result = []
    
    # Convert the input string to uppercase to handle both uppercase and lowercase characters
    input_str = input_str.upper()
    
    # Iterate through the input string and construct the sequence
    for char in input_str:
        if char in char_to_number:
            if result and result[-1] == char_to_number[char][0]:
                result.append(' ' + char_to_number[char])
            else:
                result.append(char_to_number[char])
    
    # Join the list into a single string
    return ''.join(result)
