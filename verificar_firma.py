from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import os

def main():
    if not os.path.isfile("medisoft_pub.pem"):
        print("No existe medisoft_pub.pem")
        return

    if not os.path.isfile("SHA256SUMS.txt"):
        print("No existe SHA256SUMS.txt")
        return

    if not os.path.isfile("SHA256SUMS.sig"):
        print("No existe SHA256SUMS.sig")
        return

    with open("medisoft_pub.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    with open("SHA256SUMS.txt", "rb") as f:
        contenido = f.read()

    with open("SHA256SUMS.sig", "rb") as f:
        firma = f.read()

    hash_archivo = SHA256.new(contenido)

    try:
        pkcs1_15.new(public_key).verify(hash_archivo, firma)
        print("Firma válida: el archivo es auténtico")
    except (ValueError, TypeError):
        print("Firma inválida: el archivo fue modificado o no es auténtico")

if __name__ == "__main__":
    main()