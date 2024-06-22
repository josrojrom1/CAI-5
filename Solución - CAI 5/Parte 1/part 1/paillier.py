from Crypto.Util.number import getPrime
from Crypto.Util.number import getRandomInteger
from gmpy2 import mpz
import math
def generate_keypair(bits):
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    g = n + 1
    lambda_ = (p - 1) * (q - 1)
    mu = pow(lambda_, -1, n)
    return n, g, lambda_, mu
def encrypt(n, g, m):
    r = getRandomInteger(n)
    c = pow(g, m, n**2) * pow(r, n, n**2) % (n**2)
    return c
def decrypt(n, lambda_, mu, c):
    return ((pow(c, lambda_, n**2) - 1) * pow(n, -1, n**2) * mu) % n
def sum_gastos(n, g, c1, c2):
    return (c1 * c2) % (n**2)
def main():
    n, g, lambda_, mu = generate_keypair(1024)
    # Pasajero 1
    gasto1 = 1250
    c1 = encrypt(n, g, gasto1)
    # Pasajero 2
    gasto2 = 1500
    c2 = encrypt(n, g, gasto2)
    # Suma homomórfica
    c_sum = sum_gastos(n, g, c1, c2)
    # Obtener el resultado
    gasto_total = decrypt(n, lambda_, mu, c_sum)
    print("Gasto total: ", gasto_total)
if __name__ == "__main__":
    main()
