import sympy

# Part 1: Functions for elliptic curve
P = 23  # Modulus
A = 1   # Coefficient a
B = 1   # Coefficient b

def is_quadratic_residue(n, p):
    """Checks if n is a quadratic residue modulo p."""
    return pow(n, (p - 1) // 2, p) == 1

def find_points_on_curve(a, b, p):
    """Finds all points (x, y) on the elliptic curve y^2 = x^3 + ax + b (mod p)."""
    points = []
    for x in range(p):
        rhs = (x**3 + a * x + b) % p
        if is_quadratic_residue(rhs, p):
            y = sympy.sqrt_mod(rhs, p)
            points.append((x, y))
            if y != 0:
                points.append((x, p - y))
    return points

def find_point_order(G, a, b, p):
    """Finds the order of a point G on the elliptic curve."""
    current = G
    n = 1
    while True:  # Loop until we reach the point at infinity
        current = elliptic_add(current, G, a, b, p)
        n += 1
        if current == (None, None):
            break
        if n > p + 1:  # Avoid infinite loops by bounding iterations
            raise ValueError("Order calculation failed, possible implementation error.")
    return n

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

# Find points and test order for G = (17, 25)
points = find_points_on_curve(A, B, P)
print("Points on the curve:", points)

G = (17, 25)
order = find_point_order(G, A, B, P)
print(f"Order of point {G}: {order}")
