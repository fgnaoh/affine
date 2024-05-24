import random

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_large_prime(keysize):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if is_prime(num):
            return num

def rabin_miller(n, d):
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n)  # a^d%n
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False

def is_prime_rabin_miller(n):
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False

    # Find r and d such that n = 2^r * d + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform Rabin-Miller primality tests
    for _ in range(20):  # Adjust this number to increase/decrease accuracy
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_keys(keysize=1024):
    e = d = N = 0

    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)

    N = p * q
    phiN = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if is_prime_rabin_miller(e) and e < phiN and is_prime_rabin_miller(phiN // e):
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

    message = input("Enter a message: ")
    rsa = RSA(keysize=32)
    encrypted = rsa.encrypt(message)
    decrypted = rsa.decrypt(encrypted)

    print(f"Message: {message}")
    print(f"e: {rsa.e}")
    print(f"d: {rsa.d}")
    print(f"N: {rsa.N}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")