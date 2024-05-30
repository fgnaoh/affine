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

Đoạn mã trên triển khai hai hàm `caesar_cipher_encrypt` và `caesar_cipher_decrypt` để thực hiện mã hóa và giải mã văn bản bằng phương pháp Caesar Cipher.

1. Hàm `caesar_cipher_encrypt(text, shift)`:
   - Hàm này thực hiện mã hóa văn bản theo phương pháp Caesar Cipher.
   - Đầu vào: văn bản cần được mã hóa (`text`) và số lượng ký tự dịch chuyển (`shift`).
   - Đầu ra: văn bản đã được mã hóa.

2. Hàm `caesar_cipher_decrypt(text, shift)`:
   - Hàm này thực hiện giải mã văn bản đã được mã hóa bằng Caesar Cipher.
   - Đầu vào: văn bản đã được mã hóa (`text`) và số lượng ký tự dịch chuyển (`shift`).
   - Đầu ra: văn bản đã được giải mã.

Trong ví dụ cụ thể, văn bản "KHOA CÔNG Nghệ thông Tin" được mã hóa bằng Caesar Cipher với `shift = 3`. Sau đó, văn bản đã được mã hóa được giải mã trở lại để tạo ra văn bản ban đầu. Kết quả sẽ được in ra màn hình.
