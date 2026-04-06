import hashlib
import os
import sys

def calcular_sha256(ruta_archivo):
    sha256 = hashlib.sha256()

    with open(ruta_archivo, "rb") as archivo:
        while True:
            bloque = archivo.read(4096)
            if not bloque:
                break
            sha256.update(bloque)

    return sha256.hexdigest()

def main():
    if len(sys.argv) < 6:
        print("Uso: python generar_manifiesto.py <archivo1> <archivo2> <archivo3> <archivo4> <archivo5> [más archivos...]")
        return

    archivos = sys.argv[1:]
    nombre_manifiesto = "SHA256SUMS.txt"

    with open(nombre_manifiesto, "a", encoding="utf-8") as manifiesto:
        for ruta in archivos:
            if not os.path.isfile(ruta):
                print(f"No se encontró el archivo: {ruta}")
                continue

            hash_archivo = calcular_sha256(ruta)
            nombre_archivo = os.path.basename(ruta)

            manifiesto.write(f"{hash_archivo} {nombre_archivo}\n")
            print(f"Agregado al manifiesto: {nombre_archivo}")

    print(f"\nManifiesto actualizado correctamente en {nombre_manifiesto}")

if __name__ == "__main__":
    main()