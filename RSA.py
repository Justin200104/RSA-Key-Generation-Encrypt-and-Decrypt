import random

#Extended Euclidean Algorithm to find the modular inverse
def extendedEuclideanAlgorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extendedEuclideanAlgorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modInverse(a, m):
    gcd, x, y = extendedEuclideanAlgorithm(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

#Function to calculate the modular exponentiation using the repeated square-and-multiply algorithm
def repeatedSquareAndMultiply(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:  # If the exponent is odd
            result = (result * base) % modulus
        exponent = exponent >> 1  # Divide the exponent by 2
        base = (base * base) % modulus
    return result

#Function to generate a large prime number using the Miller-Rabin Primality Test
def generateLargePrime(bits, k=5):
    while True:
        prime_candidate = random.getrandbits(bits)
        if millerRabinPrimalityTest(prime_candidate, k):
            return prime_candidate

#Miller-Rabin Primality Test function
def millerRabinPrimalityTest(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    #Write n-1 as 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    def checkComposite(d, n):
        a = random.randint(2, n - 2)
        x = repeatedSquareAndMultiply(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        if not checkComposite(d, n):
            return False
    return True

#RSA Key Generation
def rsaKeygen(bits):
    p = generateLargePrime(bits)
    q = generateLargePrime(bits)
    n = p * q
    phiN = (p - 1) * (q - 1)
    
    e = random.randrange(2, phiN)
    gcd, _, _ = extendedEuclideanAlgorithm(e, phiN)
    while gcd != 1:  # Use the extendedEuclideanAlgorithm here
        e = random.randrange(2, phiN)
        gcd, _, _ = extendedEuclideanAlgorithm(e, phiN)
    
    d = modInverse(e, phiN)  # Compute the modular inverse using the Extended Euclidean Algorithm
    
    return (n, e), d

# RSA Encryption
def rsaEncrypt(publicKey, plaintext):
    n, e = publicKey
    return repeatedSquareAndMultiply(plaintext, e, n)

# RSA Decryption
def rsaDecrypt(privateKey, publicKey, ciphertext):
    n, e = publicKey
    return repeatedSquareAndMultiply(ciphertext, privateKey, n)

#Test the RSA implementation
bits = 64
publicKey, privateKey = rsaKeygen(bits)
x = 1111

#Encrypt the message
ciphertext = rsaEncrypt(publicKey, x)
print(f"Encrypted message: {ciphertext}")

#Decrypt the message
decryptedMessage = rsaDecrypt(privateKey, publicKey, ciphertext)
print(f"Decrypted message: {decryptedMessage}")

#Verification
print(f"Original message: {x}")
print(f"Decryption successful: {x == decryptedMessage}")