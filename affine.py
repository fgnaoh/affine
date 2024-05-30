def egcd (a, b):
    if a==0:
        return (b,0,1)
    else:
        g,y,x = egcd(b% a ,a)
        return (g, x-(b//a)*y ,y)

def mod_inverse(a,m):
    g,x,y = egcd(a,m)
    if g != 1:
        raise Exception('Nghich dao khong ton tai')
    else:
        return x%m

def affine_cipher(text, key_a, key_b):
    result = ''
    for char in text:
        code_point = ord(char)
        if 0x0021 <= code_point <= 0x007e or 0xFF21 <= code_point<0xFF5E:
            encrypted_code_point = (key_a * (code_point - 0x0020) + key_b)%95 + 0x0020
            result += chr(encrypted_code_point)
        else:
            result += char
    return result

def affine_decipher(text, key_a, key_b):
    result = ''
    for char in text:
        code_point = ord(char)
        if 0x0021 <= code_point <= 0x007e or 0xFF21 <= code_point<0xFF5E:
            decrypted_code_point = (mod_inverse(key_a, 95) * (code_point - 0x0020 - key_b))%95 + 0x0020
            result += chr(decrypted_code_point)
        else:
            result += char
    return result

plaintext = "Faker"
key_a = 3
key_b = 7
encrypted_text = affine_cipher(plaintext,key_a,key_b)
print("Ma hoa: ", encrypted_text)

decrypted_text = affine_decipher(encrypted_text,key_a,key_b)
print("Giai ma: ", decrypted_text)

Hãy giải thích từng hàm trong mã trên:

1. Hàm `egcd(a, b)` (Extended Euclidean Algorithm):
   - Hàm này tính định thức của Euclid mở rộng cho hai số nguyên a và b.
   - Đầu vào: hai số nguyên a và b.
   - Đầu ra: một bộ ba (g, x, y) sao cho g là ước chung lớn nhất của a và b, và x, y là các số nguyên thỏa mãn phương trình ax + by = g.

2. Hàm `mod_inverse(a, m)`:
   - Hàm này tính nghịch đảo modulo của số nguyên a theo modulo m.
   - Đầu vào: hai số nguyên a và m.
   - Đầu ra: nghịch đảo modulo của a theo modulo m. Nếu nghịch đảo không tồn tại (g != 1), hàm sẽ ném một ngoại lệ.

3. Hàm `affine_cipher(text, key_a, key_b)`:
   - Hàm này thực hiện mã hóa văn bản theo phương pháp Affine Cipher.
   - Đầu vào: văn bản cần được mã hóa (text), hai khóa số nguyên key_a và key_b.
   - Đầu ra: văn bản đã được mã hóa.

4. Hàm `affine_decipher(text, key_a, key_b)`:
   - Hàm này thực hiện giải mã văn bản đã được mã hóa bằng Affine Cipher.
   - Đầu vào: văn bản đã được mã hóa (text), hai khóa số nguyên key_a và key_b.
   - Đầu ra: văn bản đã được giải mã.

Trong ví dụ cụ thể, văn bản "Faker" được mã hóa bằng Affine Cipher với key_a = 3 và key_b = 7. Sau đó, văn bản đã được mã hóa được giải mã trở lại để tạo ra văn bản ban đầu. Kết quả sẽ được in ra màn hình.
