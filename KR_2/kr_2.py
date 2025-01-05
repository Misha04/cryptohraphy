import sympy

# Parameters for the elliptic curve and base point
P = 127  # Modulus
A = -1   # Coefficient a
B = 3    # Coefficient b
G = (79, 40)  # Base point for encryption (Q in the task)

# Function to add two points on the elliptic curve
def elliptic_add(P, Q, a, b, p):
    """Adds two points P and Q on the elliptic curve."""
    if P == (None, None):
        return Q
    if Q == (None, None):
        return P

    x1, y1 = P
    x2, y2 = Q

    if P == Q:
        if y1 == 0:
            return (None, None)
        m = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
    elif x1 == x2:
        return (None, None)
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

# Function to multiply a point by a scalar on the elliptic curve
def scalar_multiply(k, P, a, b, p):
    """Multiplies a point P by a scalar k on the elliptic curve."""
    result = (None, None)  # Point at infinity
    temp = P
    while k:
        if k & 1:
            result = elliptic_add(result, temp, a, b, p)
        temp = elliptic_add(temp, temp, a, b, p)
        k >>= 1
    return result

# Function to check if a point lies on the elliptic curve
def is_point_on_curve(point, a, b, p):
    """Checks if a point lies on the elliptic curve."""
    if point == (None, None):
        return True
    x, y = point
    return (y**2 % p) == ((x**3 + a * x + b) % p)

# Task 1: Check if points are on the curve
P1 = (75, 6)
P2 = (79, 40)

print("Checking if points are on the curve:")
print(f"P1 {P1} on curve: {is_point_on_curve(P1, A, B, P)}")
print(f"P2 {P2} on curve: {is_point_on_curve(P2, A, B, P)}")

# Task 2: Add two points
print("\nAdding points P1 and P2:")
P_sum = elliptic_add(P1, P2, A, B, P)
print(f"P1 + P2 = {P_sum}")

# ElGamal Encryption

def elgamal_keygen(a, b, p, G):
    """Generates ElGamal private and public keys."""
    private_key = sympy.randprime(1, p - 1)
    public_key = scalar_multiply(private_key, G, a, b, p)
    return private_key, public_key

def elgamal_encrypt(msg_point, public_key, a, b, p, G):
    """Encrypts a message point using ElGamal encryption."""
    k = sympy.randprime(1, p - 1)
    C1 = scalar_multiply(k, G, a, b, p)
    C2 = elliptic_add(msg_point, scalar_multiply(k, public_key, a, b, p), a, b, p)
    return C1, C2

def elgamal_decrypt(ciphertext, private_key, a, b, p):
    """Decrypts a ciphertext using ElGamal encryption."""
    C1, C2 = ciphertext
    shared_secret = scalar_multiply(private_key, C1, a, b, p)
    decrypted_point = elliptic_add(C2, (shared_secret[0], -shared_secret[1] % p), a, b, p)
    return decrypted_point

# Task 3: ElGamal Encryption and Decryption
msg_point = P1  # Using P1 as the message point
private_key, public_key = elgamal_keygen(A, B, P, G)

print("\nPrivate key:", private_key)
print("Public key:", public_key)

ciphertext = elgamal_encrypt(msg_point, public_key, A, B, P, G)
print("Ciphertext:", ciphertext)

decrypted_point = elgamal_decrypt(ciphertext, private_key, A, B, P)
print("Decrypted point:", decrypted_point)

# Check if decrypted point matches the original message
assert decrypted_point == msg_point, "Decryption failed!"
