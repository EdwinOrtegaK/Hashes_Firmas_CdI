import hashlib
import os

def calcular_sha256(ruta_archivo):
    sha256 = hashlib.sha256()

    with open(ruta_archivo, "rb") as archivo:
        while True:
            bloque = archivo.read(4096)
            if not bloque:
                break
            sha256.update(bloque)

    return sha256.hexdigest()

def leer_manifiesto(nombre_manifiesto):
    registros = []

    with open(nombre_manifiesto, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(maxsplit=1)
            if len(partes) != 2:
                continue

            hash_esperado, nombre_archivo = partes
            registros.append((hash_esperado, nombre_archivo))

    return registros

def main():
    nombre_manifiesto = "SHA256SUMS.txt"

    if not os.path.isfile(nombre_manifiesto):
        print("No existe el archivo SHA256SUMS.txt")
        return

    registros = leer_manifiesto(nombre_manifiesto)

    print("Verificación de integridad del paquete")
    print("-" * 70)

    correctos = 0
    incorrectos = 0

    for hash_esperado, nombre_archivo in registros:
        if not os.path.isfile(nombre_archivo):
            print(f"[NO ENCONTRADO] {nombre_archivo}")
            incorrectos += 1
            continue

        hash_actual = calcular_sha256(nombre_archivo)

        if hash_actual.lower() == hash_esperado.lower():
            print(f"[OK]         {nombre_archivo}")
            correctos += 1
        else:
            print(f"[ALTERADO]   {nombre_archivo}")
            print(f"  Esperado: {hash_esperado}")
            print(f"  Actual:   {hash_actual}")
            incorrectos += 1

    print("-" * 70)
    print(f"Archivos correctos:   {correctos}")
    print(f"Archivos incorrectos: {incorrectos}")

if __name__ == "__main__":
    main()