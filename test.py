import random
from sympy import isprime
# pip install sympy
def generate_large_prime(keysize):
    while True:
        num = random.randint(2 ** (keysize - 1), 2 ** keysize - 1)
        if isprime(num):
            return num

def generate_keys(keysize=1024):
    e = d = N = 0
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)
    N = p * q
    phiN = (p - 1) * (q - 1)
    while True:
        e = random.randint(2 ** (keysize - 1), 2 ** keysize - 1)
        if isprime(e) and e < phiN and isprime(phiN // e):
            break
    d = pow(e, -1, phiN)
    return p, q, e, d, N

class RSA(object):
    def __init__(self, keysize=1024):
        self.keysize = keysize
        self.p, self.q, self.e, self.d, self.N = generate_keys(self.keysize)

    def encrypt(self, message):
        cipher = ""
        for char in message:
            m = ord(char)
            c = pow(m, self.e, self.N)
            cipher += str(c) + " "
        return cipher.strip()

    def decrypt(self, cipher):
        message = ""
        parts = cipher.split()
        for part in parts:
            c = int(part)
            m = pow(c, self.d, self.N)
            message += chr(m)
        return message

if __name__ == "__main__":
    print("RSA Encryption/Decryption")

    message = "Đại học công nghiệp"
    rsa = RSA(keysize=32)
    encrypted = rsa.encrypt(message)
    decrypted = rsa.decrypt(encrypted)

    print(f"Message: {message}")
    print(f"e: {rsa.e}")
    print(f"d: {rsa.d}")
    print(f"N: {rsa.N}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

Đoạn mã trên triển khai một lớp `RSA` để thực hiện mã hóa và giải mã thông điệp bằng thuật toán RSA. Dưới đây là giải thích các phần chính của mã:

1. Hàm `generate_large_prime(keysize)`:
   - Hàm này được sử dụng để tạo số nguyên tố lớn. Nó chọn một số ngẫu nhiên trong khoảng từ `2 ** (keysize - 1)` đến `2 ** keysize - 1` và kiểm tra xem số đó có phải là số nguyên tố bằng cách sử dụng hàm `isprime` từ thư viện `sympy`.
   - Đầu vào: kích thước khóa (`keysize`).
   - Đầu ra: số nguyên tố lớn.

2. Hàm `generate_keys(keysize=1024)`:
   - Hàm này được sử dụng để tạo khóa công khai và khóa bí mật cho thuật toán RSA.
   - Đầu vào: kích thước khóa (`keysize`).
   - Đầu ra: các tham số p, q, e, d và N của khóa RSA.

3. Lớp `RSA`:
   - Lớp này đại diện cho một hệ thống RSA và bao gồm các phương thức để mã hóa và giải mã thông điệp.
   - Phương thức `__init__` được sử dụng để khởi tạo một đối tượng RSA với kích thước khóa cho trước. Trong quá trình khởi tạo, các tham số p, q, e, d và N của khóa RSA được tạo bằng cách sử dụng hàm `generate_keys`.
   - Phương thức `encrypt` được sử dụng để mã hóa một thông điệp. Nó mã hóa từng ký tự trong thông điệp thành một số nguyên, sau đó áp dụng phép tính mũ modulo N để tạo mã hóa và trả về chuỗi mã hóa.
   - Phương thức `decrypt` được sử dụng để giải mã một chuỗi mã hóa. Nó tách chuỗi mã hóa thành các phần riêng biệt, sau đó áp dụng phép tính mũ modulo N để giải mã từng phần và trả về thông điệp đã giải mã.

Trong phần cuối của đoạn mã, một đối tượng RSA được tạo và sử dụng để mã hóa và giải mã một thông điệp cụ thể. Kết quả được in ra màn hình, bao gồm thông điệp ban đầu, các tham số khóa công khai và bí mật, thông điệp đã mã hóa và thông điệp đã giải mã.
