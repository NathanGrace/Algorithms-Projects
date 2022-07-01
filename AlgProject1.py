# Algorithms 
# Generate two large pseudo primes p and q, Alg: Fermat’s tests
# Find an e relative prime to (p-1)(q-1), Alg: Euclid’s gcd
# Find d, multiplicative inverse of e in Z(p-1)(q-1), Alg: Extended Euclid
# Output: n = pq, e and d

#RSA in pseudocode
# 1. Setup
# a) Pick two prime numbers p and q
# b) Calculate 𝑛 = 𝑝𝑞 and 𝜑 = (𝑝 − 1)(𝑞 − 1)
# ) Find an e in Z𝜑 relatively prime to 𝜑 as an encryption key
# together with n
# d) Find an d in 𝑍𝜑 , the multiplicative inverse of e as the decryption
# key of e



# Generate two large pseudo prime numbers p and q, run Fermat's tests
import random

# gcd function that we will use later on
def gcd(a=1, b=1):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def randomlist(n = 10):
    a = []
    for i in range(200): #Generates the list of random pseudo prime number canidates stored in 'a'
        x = random.randint(n, 10*n)
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7!= 0 and x % 11 !=0:
            a.append(x)
    return a

# Test list of numbers with thermats test:

def thermat_test(pseudo = [2]):
    p = []
    while len(p) < 2:
        for i in pseudo:
            pseudo_prime = True
            for k in range (50): #Number inside (), determines how many times thermat's is run
                x = random.randint(2, i//2)
                while gcd(x, i) != 1:
                    x = random.randint(2, i//2)
                if pow(x, i-1, i) != 1:
                    pseudo_prime = False
                    break
            if pseudo_prime:
                p.append(i)
        if len(p) < 5:
            pseudo = randomlist()
    return p

# Find p and q
def p_and_q(prime_list = []):
    if len(prime_list) < 2:
        print("At least 2 prime numbers are needed")
        return
    else:
        p = prime_list.pop()
        q = prime_list.pop()
        while p == q:
            q = prime_list.pop()
        return p, q

# Inverse function
def inverse(e, phi):
    e = e % phi; 
    for x in range(1, phi): 
       if ((e * x) % phi == 1): 
           return x 
    return 1


def generate_keypair(p, q):
    n = p*q
    phi = ((p-1)*(q-1))

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = inverse(e, phi) 

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

a = randomlist()
a = thermat_test(a)
p, q = p_and_q(a)



public, private = generate_keypair(p, q)

message = input("Enter the message you wish to encrypt: ")

encrypted_msg = encrypt(public, message)

print(f"{encrypted_msg}")

print (f"Decrypted Message is : {decrypt(private,encrypted_msg)}")




