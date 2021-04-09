# Set p, q
# n = p * q
# phi(n) = (p - 1) * (q - 1)
# find e: gcd(phi(n), e) = 1, 1 < e < phi(n)
# find d: e * d mod phi(n) = 1, 1 < d < phi(n)
# encrypt
# decrypt

# import math
from math import gcd

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

def decrypt(cipher_list: list, pri_key: list):
    # p = c^d mod n
    # to_list 해줘야함, 내가 과제할때는 16진수 문자열로 받음 
    plain_bytes = []
    for i in cipher_list:
        plain_bytes.append((i**pri_key[1]) % pri_key[0])
    plain_text = "".join([chr(x) for x in plain_bytes])
    
    return plain_text

def decrypt_str(hex_text: str, pri_key: list):
    # p = c^d mod n
    # to_list 해줘야함, 내가 과제할때는 16진수 문자열로 받음 
    # 2글자씩 리스트로 만들어줌
    cipher_list = [int(hex_text[i:i+2], 16) for i in range(2, len(hex_text), 2)]
    
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
#     도전과제 p와q, plain이 다르며 p,q를 다르게해서 암호화했으므로 p와 q를 찾아내라
#  반복을해서 p와 q를 찾아내고 복호화해라 

    
    # hex_text = "0x4d765050762d2162592d1512043e813e6e6e"
    # prime_list = prime_list(1000)
    # for i in range(0, len(prime_list)):
    #     for j in range(i, len(prime_list)):
    #         p = prime_list[i]
    #         q = prime_list[j]
    #         n, e, d = setting(p, q)
    #         # pub_key = [n, e]
    #         pri_key = [n, d]
    #         dec_plain = decrypt_str(hex_text, pri_key)
    #         print(dec_plain)


    p = 11
    q = 13
    n, e, d = setting(p, q)
    
    pub_key = [n, e]
    pri_key = [n, d]
    
    plain = "hello word"
    cipher = encrypt(plain, pub_key)
    print(cipher)
#   암호화 된 값 

#   cipher->16진수로 변환 할 것 
    # hex_list = []
    # hex_list.append(hex(i).split("x")[-1])
    # for i in cipher:
         # hex_list.append("{:02x}".format(i))
         # print(hex_list)
    # print("0x" + "".join(hex_list))
    # hex_text = "0x" + "".join(hex_list)
    # print(hex_text)
    # dec_plain = decrypt(cipher, pri_key)
    hex_text = "0x4d765050762d2162592d1512043e813e6e6e"
    hex_text = ""
    dec_plain = decrypt_str(hex_text, pri_key)
    print(dec_plain)
    
    # print("-------------------------------------------")
    # prime_list = prime_list(1000)
    # print(prime_list)
    
# #     에라토스테네스의 체 알고리즘으로 소수 두쌍 넣어서 구현
    
    
    
    
    