from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
# cài pip install pycryptodome
def encrypt_text(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text.hex()

def decrypt_text(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(bytes.fromhex(encrypted_text))
    unpadded_text = unpad(decrypted_text, DES.block_size)
    return unpadded_text.decode('utf-8')

# Khóa DES có độ dài 8 byte (64 bit)
key = get_random_bytes(8)

# Chuỗi cần mã hóa
plain_text = "Đại học"

# Mã hóa chuỗi
encrypted_text = encrypt_text(plain_text, key)
print("Chuỗi đã mã hóa:", encrypted_text)

# Giải mã chuỗi
decrypted_text = decrypt_text(encrypted_text, key)
print("Chuỗi đã giải mã:", decrypted_text)