def decrypt_poly_shift(ciphertext: str, odd_shift: int, even_shift: int) -> str:
    plaintext = ""
    a_ord = ord("а")
    big_a_ord = ord("А")
    russian_delta = ord("Я") - ord("А") + 1

    for index, elem in enumerate(ciphertext):
        if "а" <= elem <= "я" or "А" <= elem <= "Я":
            register = a_ord if elem.islower() else big_a_ord
            shift = odd_shift if index % 2 == 1 else even_shift
            element_code = (ord(elem) - shift - register) % russian_delta + register
            plaintext += chr(element_code)
        else:
            plaintext += elem

    return plaintext
