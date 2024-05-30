import random 

def gcd(a, b):
	if a < b:
		return gcd(b, a)
	elif a % b == 0:
		return b
	else:
		return gcd(b, a % b)

def gen_key(q):
	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)
	return key

def power(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c;
		y = (y * y) % c
		b = int(b / 2)

	return x % c

def encrypt(msg, q, h, g):
	en_msg = []
	k = gen_key(q)  
	s = power(h, k, q)
	p = power(g, k, q)
	
	for i in range(0, len(msg)):
		en_msg.append(msg[i])

	print("g^k used : ", p)
	print("g^ak used : ", s)
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])

	return en_msg, p

def decrypt(en_msg, p, key, q):
	dr_msg = []
	h = power(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))	
	return dr_msg

def main():
	msg = 'Đại học Công Nghiệp'
	print("Original Message :", msg)

	q = random.randint(pow(10, 20), pow(10, 50))
	g = random.randint(2, q)

	key = gen_key(q)  
	h = power(g, key, q)
	print("g used : ", g)
	print("g^a used : ", h)

	en_msg, p = encrypt(msg, q, h, g)
	print("Encrypted Message:", en_msg) 
	dr_msg = decrypt(en_msg, p, key, q)
	dmsg = ''.join(dr_msg)
	print("Decrypted Message :", dmsg)

if __name__ == '__main__':
	main()

Đoạn mã trên triển khai một hệ thống mã hóa và giải mã thông điệp bằng thuật toán ElGamal. Dưới đây là giải thích các phần chính của mã:

1. Hàm `gcd(a, b)`:
   - Hàm này tính ước chung lớn nhất của hai số nguyên `a` và `b` bằng thuật toán Euclid.
   - Đầu vào: hai số nguyên `a` và `b`.
   - Đầu ra: ước chung lớn nhất của `a` và `b`.

2. Hàm `gen_key(q)`:
   - Hàm này tạo một khóa ngẫu nhiên trong khoảng từ `10^20` đến `q`, đảm bảo rằng khóa được chọn có ước chung lớn nhất với `q` là 1 (điều kiện cần để khóa có thể được sử dụng cho mã hóa ElGamal).
   - Đầu vào: số nguyên `q`.
   - Đầu ra: khóa được tạo.

3. Hàm `power(a, b, c)`:
   - Hàm này tính giá trị `a^b mod c` bằng thuật toán lũy thừa nhị phân.
   - Đầu vào: ba số nguyên `a`, `b` và `c`.
   - Đầu ra: giá trị của `a^b mod c`.

4. Hàm `encrypt(msg, q, h, g)`:
   - Hàm này thực hiện quá trình mã hóa một thông điệp bằng thuật toán ElGamal.
   - Đầu vào: thông điệp cần mã hóa (`msg`), số nguyên `q` và hai khóa công khai `h` và `g`.
   - Đầu ra: một danh sách chứa các phần tử đã được mã hóa.

5. Hàm `decrypt(en_msg, p, key, q)`:
   - Hàm này thực hiện quá trình giải mã một danh sách các phần tử đã được mã hóa thành thông điệp gốc.
   - Đầu vào: danh sách các phần tử đã mã hóa (`en_msg`), số nguyên `p`, khóa bí mật (`key`) và `q`.
   - Đầu ra: một danh sách chứa các ký tự trong thông điệp đã giải mã.

6. Hàm `main()`:
   - Hàm này là hàm chính của chương trình. Nó tạo một thông điệp ban đầu, tạo số nguyên ngẫu nhiên `q` và `g`, tạo khóa bí mật `h`, mã hóa thông điệp và giải mã thông điệp.
   - Đầu ra: thông điệp ban đầu, thông điệp đã mã hóa và thông điệp đã giải mã được in ra màn hình.

Quá trình mã hóa và giải mã của thuật toán ElGamal trong đoạn mã trên được thực hiện như sau:
- Bước 1: Tạo số nguyên ngẫu nhiên `q` và `g`.
- Bước 2: Tạo khóa bí mật `h` bằng cách tính `g^key mod q`, với `key` là khóa bí mật được tạo ngẫu nhiên.
- Bước 3: Mã hóa thông điệp bằng cách thực hiện các phép tính trên từng ký tự trong thông điệp:
  - Tạo một khóa ngẫu nhiên `k` bằng `gen_key(q)`.
  - Tính `s = h^k mod q`.
  - Tính `p = g^k mod q`.
  - Mã hóa ký tự bằng cách nhân `s` với giá trị số nguyên tương ứng với ký tự đó (sử dụng hàm `ord(en_msg[i])`).
  - Kết quả mã hóa được lưu trong danh sách `en_msg`.
- Bước 4: Giải mã danh sách các phần tử đã mã hóa bằng cách thực hiện các phép tính:
  - Tính `h = p^key mod q`.
  - Giải mã mỗi phần tử trong danh sách bằng cách chia cho `h` và chuyển đổi kết quả thành ký tự tương ứng (sử dụng hàm `chr(int(en_msg[i]/h))`).
  - Kết quả giải mã được lưu trong danh sách `dr_msg`.

Cuối cùng, kết quả ban đầu, thông điệp đã mã hóa và thông điệp đã giải mã được in ra màn hình.
