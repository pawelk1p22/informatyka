def bacon_cipher(text):
    # Słownik z przyporządkowaniem liter do ciągów A i B
    bacon_dict = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB',
        'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB',
        'I': 'ABAAA', 'K': 'ABAAB', 'L': 'ABABA', 'M': 'ABABB',
        'N': 'ABBAA', 'O': 'ABBAB', 'P': 'ABBBA', 'Q': 'ABBAA',
        'R': 'ABBAB', 'S': 'ABBBA', 'T': 'ABBBA', 'U': 'BAAAA',
        'V': 'BAAAB', 'W': 'BAABA', 'X': 'BAABB', 'Y': 'BABAA',
        'Z': 'BABAB'
    }

    text = text.upper()
    encrypted_text = ""

    for char in text:
        if char == ' ':
            encrypted_text += ' '
        elif char in bacon_dict:
            encrypted_text += bacon_dict[char] + ' '

    return encrypted_text
