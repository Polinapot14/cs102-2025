=def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    new_keyword = ""
    while len(new_keyword) < len(plaintext):
        new_keyword += keyword
    keyword = new_keyword.lower()

    for i, char in enumerate(plaintext):
        if not char.isalpha():
            ciphertext += char
            continue
        elif char.islower():
            # a, b - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 97
            b = 26
            shift = ord(keyword[i]) - a
            x = ord(char)
            new_x = (((x - a) + shift) % b) + a
            ciphertext += chr(new_x)
        else:
            # a, b и c - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 97
            b = 65
            c = 26
            shift = ord(keyword[i]) - a
            x = ord(char)
            new_x = (((x - b) + shift) % c) + b
            ciphertext += chr(new_x)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    new_keyword = ""
    while len(new_keyword) < len(ciphertext):
        new_keyword += keyword
    keyword = new_keyword.lower()

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if not char.isalpha():
            plaintext += char
            continue
        elif char.islower():
            # a, b - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 97
            b = 26
            shift = ord(keyword[i]) - a
            x = ord(char)
            new_x = (((x - a) - shift) % b) + a
            plaintext += chr(new_x)
        else:
            # a, b и c - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 97
            b = 65
            c = 26
            shift = ord(keyword[i]) - a
            x = ord(char)
            new_x = (((x - b) - shift) % c) + b
            plaintext += chr(new_x)

    return plaintext
