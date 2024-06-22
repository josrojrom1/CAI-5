import hashlib
import os
import getpass
import time
# Limpiamos terminal de anteriores tareas
os.system('clear')
# Mostramos banner de inicialización del script
with open("banner_fly.txt", "r") as f:
    banner = f.read()
    print(banner)
# Nombre + salt en el cifrado con Sha256
clave = getpass.getpass('Introduce la contraseña: ').encode('utf-8')
salt = str(9843670983456938453).encode('utf-8')
# Algoritmo de comprobación de coincidencias viajero/criminal
if clave != "" and clave == "clave1".encode('utf-8'):
    inicio = time.time()# Inicio para la pruena de tiempo de ejecución
    # Pasajeros del actual viaje
    with open("viajeros.txt", "r") as c:
        for line in c:
            l = line.strip()
            nombre = str(l).encode('utf-8')
            cadena = nombre + salt + clave
            hash_obj = hashlib.sha256(cadena)
            hash_value = hash_obj.hexdigest()
            # Guardamos el hashing del pasajero dado
            hashed_store = hash_value
            # Mostramos por pantalla los hashes generados
            print(hashed_store)
            # Abrimos lista de criminales compartida por la policía
            with open("hashed_criminals.txt", "r") as h:
                for line in h:
                    # Separamos en variables el nombre y el hash
                    c_hash = line.strip().split(",")[1]
                    c_name = line.strip().split(",")[0]
                    # si coinciden el hash del pasajero y el del criminal
                    if c_hash == hashed_store:
                        print("\n")
                        print("¡POSIBLE CRIMINAL!\n")
                        print(f"Nombre: {c_name}\n")
                        print(f"HASH: {c_hash}\n")
                        fin = time.time()
                        tiempo_ejecucion = fin - inicio
                        print("Tiempo de ejecución: ", tiempo_ejecucion, "segundos")
else:
    # Mensaje de fallo de autenticación por contraseña incorrecta
    print('Contraseña inválida...')


