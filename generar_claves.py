from Crypto.PublicKey import RSA

def generar_par_claves(bits: int = 3072):
    if bits < 2048:
        raise ValueError("RSA requiere al menos 2048 bits por seguridad.")
    
    private_key = RSA.generate(bits)
    public_key = private_key.publickey()

    private_pem = private_key.export_key(format="PEM")
    public_pem = public_key.export_key(format="PEM")

    with open("medisoft_priv.pem", "wb") as private_file:
        private_file.write(private_pem)

    with open("medisoft_pub.pem", "wb") as public_file:
        public_file.write(public_pem)

if __name__ == '__main__':
    generar_par_claves(2048)
    print("Claves generadas: medisoft_priv.pem y medisoft_pub.pem")