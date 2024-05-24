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

