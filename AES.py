from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_text(plain_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text.hex()

def decrypt_text(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(bytes.fromhex(encrypted_text))
    unpadded_text = unpad(decrypted_text, AES.block_size)
    return unpadded_text.decode('utf-8')

# Khóa AES có độ dài 16 byte (128 bit)
key = get_random_bytes(16)

# Chuỗi cần mã hóa
plain_text = "Đại học"

# Mã hóa chuỗi
encrypted_text = encrypt_text(plain_text, key)
print("Chuỗi đã mã hóa:", encrypted_text)

# Giải mã chuỗi
decrypted_text = decrypt_text(encrypted_text, key)
print("Chuỗi đã giải mã:", decrypted_text)