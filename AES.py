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

Hàm encrypt_text nhận vào hai tham số plain_text (chuỗi văn bản cần mã hóa) và key (khóa AES). Trong hàm này, một đối tượng AES mới được tạo với khóa được cung cấp. Văn bản cần mã hóa được chuyển thành dạng bytes và được đệm (pad) để đảm bảo có đúng kích thước khối AES. Sau đó, văn bản được mã hóa bằng cách sử dụng phương thức encrypt của đối tượng AES và kết quả được trả về dưới dạng chuỗi hex.

Hàm decrypt_text nhận vào hai tham số encrypted_text (chuỗi đã được mã hóa) và key (khóa AES). Trong hàm này, một đối tượng AES mới được tạo với khóa được cung cấp. Chuỗi đã được mã hóa được chuyển thành dạng bytes và giải mã bằng cách sử dụng phương thức decrypt của đối tượng AES. Sau đó, văn bản giải mã được bỏ đệm (unpad) và chuyển về dạng chuỗi văn bản.

Sau khi định nghĩa các hàm, đoạn code tiếp theo tạo một khóa AES ngẫu nhiên với độ dài 16 byte (128 bit) bằng cách sử dụng get_random_bytes(16). Đoạn văn bản cần mã hóa là "Đại học". Hàm encrypt_text được gọi với văn bản cần mã hóa và khóa AES để mã hóa văn bản và trả về chuỗi đã mã hóa. Chuỗi đã mã hóa được in ra màn hình.

Sau đó, hàm decrypt_text được gọi với chuỗi đã mã hóa và khóa AES để giải mã chuỗi. Kết quả giải mã được in ra màn hình.
