def caesar_cipher_encrypt(text, shift):
    result = ''
    for char in text:
        code_point = ord(char)
        if 0x0021 <= code_point <= 0x007e or 0xFF21 <= code_point < 0xFF5E:
            encrypted_code_point = (code_point - 0x0020 + shift) % 95 + 0x0020
            result += chr(encrypted_code_point)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    result = ''
    for char in text:
        code_point = ord(char)
        if 0x0021 <= code_point <= 0x007e or 0xFF21 <= code_point < 0xFF5E:
            decrypted_code_point = (code_point - 0x0020 - shift) % 95 + 0x0020
            result += chr(decrypted_code_point)
        else:
            result += char
    return result

# Example usage
plaintext = "KHOA CÔNG Nghệ thông Tin"
shift = 3
encrypted_text = caesar_cipher_encrypt(plaintext, shift)
print("Ma hoa: ", encrypted_text)

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Giai ma: ", decrypted_text)