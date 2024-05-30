import random

def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a % b ==0:
        return b
    else:
        return gcd(b,a%b)

def genkey(p):
    key = random.randint(pow(10,20),p)
    while gcd(p,key) !=1 :
        key = random.randint(pow(10,20),p)
    
    return key

def power(a,b,n):
    bi=[]
    while b>0:
        bi.insert(0,b%2)
        b=int(b/2)

    f=1
    for i in bi:
        f=(f*f %n)
        if i==1:
            f=(f*a)%n
    return f

def encrypt(msg, q,h,g):
    en_msg = []
    
    x = genkey(q)
    s = power(h ,x ,q)
    p = power(g,x,q)

    for i in range(0, len(en_msg)):
        en_msg.append(msg[i])

    print("g^k used : ",p)
    print("g^ak used : ",s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s*ord(en_msg[i])
    
    return en_msg, p

def decrypt(en_msg, p, key , q):
    dr_msg = []
    h = power(p , key ,q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))

    return dr_msg

msg="HAUIvn_CS1"
msg = input("Nhập kí tự mã hóa: ")
print("Thông điệp :", msg)

q = random.randint(pow(10,20), pow(10,50))
g = random.randint(2,q)
#pri key
key = genkey(q)
h = power(g,key,q)
print("g used: ",g)
print("g^a used: ",h)

en_msg, p = encrypt(msg, q ,h, g)
dr_msg= decrypt(en_msg , p ,key ,q)
dmsg = ''.join(dr_msg)
print("giải mã: ",dr_msg)
