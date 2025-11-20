def encrypt_vigenere(plaintext: str, keyword: str) -> str:
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
            # 97, 26 - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            shift = ord(keyword[i]) - 97
            x = ord(char)
            new_x = (((x - 97) + shift) % 26) + 97
            ciphertext += chr(new_x)
        else:
            # 97, 65 и 26 - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            shift = ord(keyword[i]) - 97
            x = ord(char)
            new_x = (((x - 65) + shift) % 26) + 65
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
            # 97, 26 - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            shift = ord(keyword[i]) - 97
            x = ord(char)
            new_x = (((x - 97) - shift) % 26) + 97
            plaintext += chr(new_x)
        else:
            # 97, 65 и 26 - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            shift = ord(keyword[i]) - 97
            x = ord(char)
            new_x = (((x - 65) - shift) % 26) + 65
            plaintext += chr(new_x)

    return plaintext
