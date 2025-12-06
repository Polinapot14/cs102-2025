def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
            continue
        elif char.islower():
            ascii_ = ord(char)
            # a и b - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 97
            b = 26
            new_ascii_ = (((ascii_ - a) + shift) % b) + a
            ciphertext += chr(new_ascii_)
        else:
            ascii_ = ord(char)
            # a и b - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 65
            b = 26
            new_ascii_ = (((ascii_ - a) + shift) % b) + a
            ciphertext += chr(new_ascii_)

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    for char in ciphertext:
        if not char.isalpha():
            plaintext += char
            continue
        elif char.islower():
            ascii_ = ord(char)
            # a и b - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 97
            b = 26
            new_ascii_ = (((ascii_ - a) - shift) % b) + a
            plaintext += chr(new_ascii_)
        else:
            ascii_ = ord(char)
            # a и b - это числа, используемые в формуле для получаения
            # ascii-кода после сдвига
            a = 65
            b = 26
            new_ascii_ = (((ascii_ - a) - shift) % b) + a
            plaintext += chr(new_ascii_)

    return plaintext
