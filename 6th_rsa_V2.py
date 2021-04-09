import sys
from math import gcd

# Set p, q  q랑 p를 구해야 한다 ! p 랑 q만 구하면 나머지는 알아서 착착 돌아간다
# p와 q는 각각 3자리수의(100-999) "소수"이다. 
# 소수 구하는 알고리즘은 이미 "에라토스테네스의 체" 알고리즘을 이용해 구현됐다
# 즉,! prime_list 함수에 1000을 준다면 1000까지 모든 소수를 리스트에 담아 리턴해준다.
# 예시)
# [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
# 이 리스트 안에 p q가 각각 있을 것이다. "hex_text"라는 16진수로 암호화 된 문자열이 있는데 올바른 p q를 구한다면 decrypt함수에 넣은 결과 값이 예를들어 "Hellow word" 이런 결과 값이 나올 것이다. 이 결과값을 찾는게 목표 

# 
# n = p * q 
# phi(n) = (p - 1) * (q - 1)
# find e: gcd(phi(n), e) = 1, 1 < e < phi(n)
# find d: e * d mod phi(n) = 1, 1 < d < phi(n)
# encrypt
# decrypt



def setting(p: int, q: int):
    n = p * q
    phi_n = (p-1) * (q-1)
    e = find_e(phi_n)
    d = find_d(phi_n, e)
    return n, e, d

def find_e(phi_n: int):
    e = 0
    for i in range(2, phi_n):
        if gcd(phi_n, i) == 1:
            e = i
            break
    return e
def find_d(phi_n: int, e: int):
    d = 0
    for i in range(2, phi_n):
        if(e * i) % phi_n == 1:
            d = i
            break
    return d

def encrypt(plain_text: str, pub_key: list):
    # c = p^e mod n
    plain_bytes = [ord(x) for x in plain_text]
    cipher_bytes = []
    for i in plain_bytes:
        cipher_bytes.append((i** pub_key[1]) % pub_key[0])
    return cipher_bytes

def decrypt(hex_text: str, pri_key: list):
    # p = c^d mod n
    # to_list 해줘야함, 내가 과제할때는 16진수 문자열로 받음 
    cipher_list = [int(hex_text[i:i+8], 16) for i in range(2, len(hex_text), 8)]
    plain_bytes = []
    for i in cipher_list:
        plain_bytes.append((i**pri_key[1]) % pri_key[0])
    plain_text = "".join([chr(x) for x in plain_bytes])
    
    return plain_text

def decrypt_str(hex_text: str, pri_key: list):
    # p = c^d mod n
    # to_list 해줘야함, 내가 과제할때는 16진수 문자열로 받음 
    # 2글자씩 리스트로 만들어줌
    cipher_list = [hex_text[i:i+8] for i in range(2, len(hex_text), 8)]
    plain_bytes = []
    for i in cipher_list:
        plain_bytes.append((i**pri_key[1]) % pri_key[0])
    plain_text = "".join([chr(x) for x in plain_bytes])
    
    return plain_text
# 1000까지
def prime_list(n): 
    sieve = [True] * n
    
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

if __name__=="__main__":
    sys.stdout = open('stdout.txt', 'w')
    hex_text = "0x0003b971000114f60001caef0002e6c900043e9e00043e9e0003a6210004702100047bf40003b101000352ce00030c960003a62100043e9e00043e9e0003a6210002e6c90001bdf8000352ce0003142d0002e6c9000114f60001caef00047bf40003b1010002c0730003b101000355f6000355f6"

    prime_list = prime_list(1000)
    prime_list = prime_list[25::]
    # print("length")
    # print(len(prime_list))
    # print(prime_list)
    # dec_plain = []

    print("Start".encode('utf-8', 'surrogatepass').decode('utf-8'))
    for i in range(0, len(prime_list)):
        p = prime_list[i]
        for j in range(i, len(prime_list)):
            q = prime_list[j]
            n, e, d = setting(p, q)
            pri_key = [n, d]
            print(decrypt(hex_text,pri_key).encode('utf-8', 'surrogatepass').decode('utf-8'))            
    print("End".encode('utf-8', 'surrogatepass').decode('utf-8'))
    sys.stdout.close()
    