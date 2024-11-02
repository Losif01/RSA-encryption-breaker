
import math
import time

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self.find_e(self.phi)
        self.d = self.mod_inverse(self.e, self.phi)
    
    def find_e(self, phi):
        e = 2
        while e < phi:
            if math.gcd(e, phi) == 1:
                return e
            e += 1
        return None

    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, plaintext):
        return [pow(ord(char), self.e, self.n) for char in plaintext]

    def decrypt(self, ciphertext):
        return ''.join([chr(pow(char, self.d, self.n)) for char in ciphertext])

    #breaking RSA using brute force (funny enough, RSA was made specifically to combat brute force lol)
    def brute_force_factorization(self, ciphertext):
        for i in range(2, self.n):
            if self.n % i == 0:
                p, q = i, self.n // i
                phi = (p - 1) * (q - 1)
                d = self.mod_inverse(self.e, phi)
                return ''.join([chr(pow(char, d, self.n)) for char in ciphertext])
        return "Brute-force factorization failed."

    def fermat_factorization(self, ciphertext):
        x = math.isqrt(self.n) + 1
        y2 = x * x - self.n
        while not math.isqrt(y2) ** 2 == y2:
            x += 1
            y2 = x * x - self.n
        y = math.isqrt(y2)
        p, q = x - y, x + y
        if p * q == self.n:
            phi = (p - 1) * (q - 1)
            d = self.mod_inverse(self.e, phi)
            return ''.join([chr(pow(char, d, self.n)) for char in ciphertext])
        return "Fermat factorization failed."

    def timing_attack(self, ciphertext):
        #This is a conceptual example; in reality, timing attacks require careful hardware measurements
        start_time = time.time()
        try:
            decrypted_text = self.decrypt(ciphertext)
        except Exception as e:
            decrypted_text = "Timing Attack Failed"
        end_time = time.time()
        duration = end_time - start_time
        return decrypted_text, f"Time taken for decryption (in seconds): {duration}"

    def low_exponent_attack(self, ciphertext):
        #If e = 3 and plaintext < n^(1/e), we can decrypt without private key
        if self.e == 3:
            plaintext_numerical = [round(pow(char, 1/3)) for char in ciphertext]
            return ''.join([chr(int(p)) for p in plaintext_numerical])
        return "Low exponent attack failed: e is not low enough."

if __name__ == "__main__":
    rsa = RSA(61, 53)  #demo usage
    plaintext = "HELLO"
    ciphertext = rsa.encrypt(plaintext)

    print("Original Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted (Normal):", rsa.decrypt(ciphertext))
    print("Brute Force Attack:", rsa.brute_force_factorization(ciphertext))
    print("Fermat Factorization Attack:", rsa.fermat_factorization(ciphertext))
    print("Timing Attack:", rsa.timing_attack(ciphertext))
    print("Low Exponent Attack:", rsa.low_exponent_attack(ciphertext))
