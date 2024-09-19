# RSA Key Generation, Encryption, and Decryption

**Description:**  
This project implements the RSA cryptosystem, which is widely used in secure communication. RSA involves generating a pair of keys – a public key for encryption and a private key for decryption.

## Key Concepts:

1. **Key Generation:**
   - Two large prime numbers (`p` and `q`) are generated.
   - Their product `n = p * q` forms part of both the public and private keys.
   - The Euler’s Totient (`phiN = (p-1) * (q-1)`) is calculated.
   - A public exponent `e` is chosen such that `1 < e < phiN`, and the GCD of `e` and `phiN` is 1.
   - The private key `d` is computed as the modular inverse of `e` modulo `phiN`, ensuring that `e * d ≡ 1 (mod phiN)`.

2. **RSA Encryption:**
   - The public key `(n, e)` is used to encrypt a message `m` using the formula:  
     ```
     c = m^e % n
     ```
   - This ensures that the message can only be decrypted using the corresponding private key.

3. **RSA Decryption:**
   - The private key `d` is used to decrypt the ciphertext `c` using the formula:  
     ```
     m = c^d % n
     ```
   - This retrieves the original message `m`.

4. **Modular Arithmetic:**
   - The project uses the Repeated Square-and-Multiply algorithm to efficiently compute large powers during encryption and decryption.
   - The Extended Euclidean Algorithm is used to calculate the modular inverse for generating the private key.

## Testing Example:
- A 64-bit key pair is generated.
- A message `1111` is encrypted and then decrypted to verify the implementation.

## Conclusion:
This project demonstrates the fundamental principles of RSA, including secure key generation, encryption, and decryption using modular arithmetic. RSA is essential in modern cryptography for securing communications.
