# RSA Encryption and Attacks Module

This Python module provides a simple implementation of the RSA encryption algorithm along with a few methods to attempt decryption using different attack techniques. This module is intended for educational purposes to demonstrate how RSA works and some common ways to attack it.

## Features
- **Encryption and Decryption**: Basic RSA encryption and decryption with a public/private key pair.
- **Brute Force Attack**: Attempts to decrypt the message by factorizing the modulus \( n \) with brute force.
- **Fermat Factorization**: An optimized factorization method effective if the prime factors \( p \) and \( q \) of \( n \) are close to each other.
- **Timing Attack**: A conceptual timing attack that shows the time taken for decryption.
- **Low Exponent Attack**: Attempts decryption if the public exponent \( e \) is set to a low value (e.g., 3).

## Requirements
- Python 3.x

## Usage

### Installation
Simply clone this repository or copy the `rsa_module.py` file to your project directory.

### Importing the Module

To use the `RSA` class in your project, import it from the module file:

```python
from rsa_module import RSA  # replace rsa_module with your filename
```

### Example Usage

Below is an example demonstrating how to use the RSA class for encryption, decryption, and various attack methods.

```python
# Import the RSA class
from rsa_module import RSA

# Initialize the RSA object with two small prime numbers
rsa = RSA(61, 53)  # For larger security, use bigger primes

# Encrypt a plaintext message
plaintext = "HELLO"
ciphertext = rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext back to plaintext
decrypted_text = rsa.decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)

# Attempt different attack methods
print("Brute Force Attack:", rsa.brute_force_factorization(ciphertext))
print("Fermat Factorization Attack:", rsa.fermat_factorization(ciphertext))
print("Timing Attack:", rsa.timing_attack(ciphertext))
print("Low Exponent Attack:", rsa.low_exponent_attack(ciphertext))
```

### Running as a Standalone Script

You can also run the file directly to see a demonstration of the RSA encryption, decryption, and attacks. Open a terminal and run:

```bash
python rsa_module.py
```

### Functions

#### `RSA.__init__(self, p, q)`
Initializes the RSA object with two prime numbers \( p \) and \( q \). Generates public and private keys based on \( p \) and \( q \).

#### `RSA.encrypt(self, plaintext)`
Encrypts a plaintext string using the public key.

- **Arguments**:
  - `plaintext` (str): The text to encrypt.
- **Returns**:
  - List of integers representing the ciphertext.

#### `RSA.decrypt(self, ciphertext)`
Decrypts a list of integers (ciphertext) back to plaintext using the private key.

- **Arguments**:
  - `ciphertext` (list of int): The encrypted message.
- **Returns**:
  - `str`: Decrypted plaintext message.

#### `RSA.brute_force_factorization(self, ciphertext)`
Attempts to decrypt the ciphertext by factorizing the modulus \( n \) using brute force.

#### `RSA.fermat_factorization(self, ciphertext)`
Attempts to decrypt the ciphertext using Fermat's factorization method, which is effective if \( p \) and \( q \) are close.

#### `RSA.timing_attack(self, ciphertext)`
Demonstrates a conceptual timing attack, returning the time taken for decryption.

#### `RSA.low_exponent_attack(self, ciphertext)`
Attempts to decrypt the ciphertext using a low-exponent attack if the public exponent \( e \) is set to a low value (e.g., 3).

## Note
This RSA implementation is simplified and not suitable for real-world cryptographic security. It is designed for learning and demonstration purposes only.

## License
This project is licensed under the GNU GPL v3.0 License.
