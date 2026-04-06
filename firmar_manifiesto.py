from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import os

def main():
    if not os.path.isfile("medisoft_priv.pem"):
        print("No existe medisoft_priv.pem")
        return

    if not os.path.isfile("SHA256SUMS.txt"):
        print("No existe SHA256SUMS.txt")
        return

    with open("medisoft_priv.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    with open("SHA256SUMS.txt", "rb") as f:
        contenido = f.read()

    hash_archivo = SHA256.new(contenido)
    firma = pkcs1_15.new(private_key).sign(hash_archivo)

    with open("SHA256SUMS.sig", "wb") as f:
        f.write(firma)

    print("Firma generada correctamente en SHA256SUMS.sig")

if __name__ == "__main__":
    main()