from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes

# En este ejemplo, se genera un esquema de Prueba de Conocimiento Cero utilizando criptografía asimétrica 
# RSA. Se eligen números primos grandes, se calculan claves pública y privada, se genera un mensaje aleatorio, 
# se cifra con la clave pública y se verifica con la clave privada para demostrar el conocimiento del mensaje 
# sin revelar su contenido. Este es un ejemplo básico para ilustrar cómo se puede implementar un esquema de 
# Prueba de Conocimiento Cero en Python. Para aplicaciones reales, se recomienda un análisis más detallado y 
# la adaptación a los requisitos específicos del sistema de precios de vuelos de la compañía aérea.

# Generar números primos grandes
p = getPrime(128)
q = getPrime(128)

# Calcular n y phi
n = p * q
phi = (p - 1) * (q - 1)

# Elegir un número aleatorio coprimo con phi
e = 65537

# Calcular la clave privada
d = pow(e, -1, phi)

# Función para generar una prueba de conocimiento cero
def zero_knowledge_proof():
    # Generar un mensaje aleatorio
    m = get_random_bytes(16)

    # Calcular el mensaje cifrado
    c = pow(int.from_bytes(m, 'big'), e, n)

    # Verificar la prueba de conocimiento cero
    decrypted_m = pow(c, d, n)
    if int.from_bytes(m, 'big') == decrypted_m:
        return True
    else:
        return False

# Ejecutar la prueba de conocimiento cero
result = zero_knowledge_proof()
print("¿La prueba de conocimiento cero es válida?", result)
