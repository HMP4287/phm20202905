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

def decrypt(hex_text: str, pri_key: list):
    # p = c^d mod n
    # 2글자씩 리스트로 만들어줌
    cipher_list = [int(hex_text[i:i+2], 16) for i in range(2, len(hex_text), 2)]
    
    plain_bytes = []
    for i in cipher_list:
        plain_bytes.append((i**pri_key[1]) % pri_key[0])
    plain_text = "".join([chr(x) for x in plain_bytes])
    
    return plain_text



if __name__=="__main__":

    p = 11
    q = 13
    n, e, d = setting(p, q)
    
    pri_key = [n, d]
    
    hex_text = "0x4d765050762d2162592d1512043e813e6e6e"
    dec_plain = decrypt(hex_text, pri_key)
    print(dec_plain)
