import hashlib
import os
import getpass
# Limpiamos terminal para mostrar el script correctamente
os.system('clear')
# Mostramos el banner del script policial
with open("banner_police.txt", "r") as f:
    banner = f.read()
    print(banner)
# Nombre + salt en el cifrado con Sha256
clave = getpass.getpass('Introduce la contraseña: ').encode('utf-8')
salt = str(9843670983456938453).encode('utf-8')
# Lista vacía para guardar las diferentes entradas generadas
hashed_values = []
# Acceso al sistema mediante la clave "clave1"
if clave != "" and clave == "clave1".encode('utf-8'):
    # Nombres de criminales en el archivo criminales.txt
    with open("criminales.txt", "r") as c:
        # Realizamos lectura del archivo y generamos hashes
        for line in c:
            crim = line.strip()
            nombre = str(crim).encode('utf-8')
            cadena = nombre + salt + clave
            hash_obj = hashlib.sha256(cadena)
            hash_value = hash_obj.hexdigest()
            # Tupla con el nombre del criminal, salt y hashing
            hashed_store = (nombre.decode('utf-8'), hash_value)
            # Mostramos las entradas a registrar en pantalla
            print(hashed_store)
            # Guardamos las entradas en la lista vacía inicial
            hashed_values.append(hashed_store)
            # Abrimos la base de datos de criminales y hashes
            with open("hashed_criminals.txt", "a") as h:
                # Escribimos en la base de datos las nuevas entradas
                h.write(f"{hashed_store[0]},{hashed_store[1]}\n")
else:
    # En caso de fallar la contraseña mostramos el mensaje
    print('Contraseña inválida...')


