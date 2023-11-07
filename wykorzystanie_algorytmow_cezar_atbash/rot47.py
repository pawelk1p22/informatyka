def rot47(text):
    result = ''
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 47) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 47) % 26 + ord('a'))
        elif '0' <= char <= '9':
            result += chr((ord(char) - ord('0') + 47) % 10 + ord('0'))
        else:
            result += char
    return result
