import hashlib
import urllib.request
import urllib.error

PASSWORDS = ["admin", "123456", "hospital", "medisoft2024"]

def sha256_hex(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest().upper()

def sha1_hex(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest().upper()

def consultar_hibp_por_sha1(sha1_hash: str) -> int:
    prefijo = sha1_hash[:5]
    sufijo_objetivo = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefijo}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "HashesFirmasCdI/1.0"
        }
    )

    # Prompt con el que se le pregunto a ChatGPT para obtener este codigo
    # Necesito en Python hacer una consulta a la API de Have I Been Pwned usando el modelo k-anonymity. 
    # Quiero enviar los primeros 5 caracteres de un hash SHA-1 y luego comparar localmente los sufijos 
    # para encontrar coincidencias. Hazlo usando urllib y sin librerías externas.
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            contenido = response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"Error HTTP al consultar HIBP para prefijo {prefijo}: {e}")
        return -1
    except urllib.error.URLError as e:
        print(f"Error de conexión al consultar HIBP para prefijo {prefijo}: {e}")
        return -1

    for linea in contenido.splitlines():
        partes = linea.strip().split(":")
        if len(partes) != 2:
            continue

        sufijo_api, conteo = partes
        if sufijo_api.upper() == sufijo_objetivo:
            return int(conteo)

    return 0

def main():
    print("Verificación de contraseñas comunes contra HIBP")
    print("-" * 100)
    print(f"{'Contraseña':<15} {'SHA-256':<64} {'SHA-1':<40} {'Apariciones HIBP':>18}")
    print("-" * 100)

    for password in PASSWORDS:
        hash_sha256 = sha256_hex(password)
        hash_sha1 = sha1_hex(password)
        apariciones = consultar_hibp_por_sha1(hash_sha1)

        print(
            f"{password:<15} {hash_sha256:<64} {hash_sha1:<40} {apariciones:>18}"
        )

if __name__ == "__main__":
    main()