import random
from sympy import isprime

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
