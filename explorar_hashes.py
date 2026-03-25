import hashlib

def contar_bits_diferentes(hash1_bytes, hash2_bytes):
    xor_resultado = bytes(b1 ^ b2 for b1, b2 in zip(hash1_bytes, hash2_bytes))
    return sum(bin(byte).count("1") for byte in xor_resultado)

def main():
    textos = ["MediSoft-v2.1.0", "medisoft-v2.1.0"]

    algoritmos = {
        "MD5": hashlib.md5,
        "SHA-1": hashlib.sha1,
        "SHA-256": hashlib.sha256,
        "SHA3-256": hashlib.sha3_256,
    }

    resultados = {}

    for texto in textos:
        print(f"\nTexto de entrada: {texto}")
        print("-" * 110)
        print(f"{'Algoritmo':<12} {'Bits':<8} {'Hex chars':<10} {'Hash'}")
        print("-" * 110)

        resultados[texto] = {}

        for nombre_alg, hash_func in algoritmos.items():
            hash_obj = hash_func(texto.encode("utf-8"))
            digest_bytes = hash_obj.digest()
            digest_hex = hash_obj.hexdigest()

            resultados[texto][nombre_alg] = {
                "bytes": digest_bytes,
                "hex": digest_hex,
                "bits": len(digest_bytes) * 8,
                "hex_len": len(digest_hex),
            }

            print(f"{nombre_alg:<12} {len(digest_bytes) * 8:<8} {len(digest_hex):<10} {digest_hex}")

    print("\nComparación SHA-256 entre ambos textos")
    print("-" * 110)

    sha256_1 = resultados["MediSoft-v2.1.0"]["SHA-256"]["bytes"]
    sha256_2 = resultados["medisoft-v2.1.0"]["SHA-256"]["bytes"]

    bits_cambiados = contar_bits_diferentes(sha256_1, sha256_2)

    print(f"SHA-256 1: {resultados['MediSoft-v2.1.0']['SHA-256']['hex']}")
    print(f"SHA-256 2: {resultados['medisoft-v2.1.0']['SHA-256']['hex']}")
    print(f"\nCantidad de bits diferentes (usando XOR): {bits_cambiados}")


if __name__ == "__main__":
    main()