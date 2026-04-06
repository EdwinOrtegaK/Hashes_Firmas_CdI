
# Hashes, Integridad y Firmas Digitales

## Descripción general
Este laboratorio tiene como objetivo comprender y aplicar conceptos fundamentales de seguridad informática, incluyendo:

- Funciones hash (SHA-256 y SHA-1)
- Verificación de contraseñas con Have I Been Pwned (HIBP)
- Integridad de archivos mediante hashes
- Firmas digitales con RSA
- Validación de autenticidad e integridad

## Conceptos clave

- **Hash (SHA-256):** Garantiza integridad
- **Firma digital (RSA):** Garantiza autenticidad
- **HIBP API:** Permite verificar si contraseñas han sido comprometidas

## Archivos del proyecto

- `generar_manifiesto.py` → genera hashes de archivos
- `verificar_paquete.py` → verifica integridad
- `generar_claves.py` → genera claves RSA
- `firmar_manifiesto.py` → firma el manifiesto
- `verificar_firma.py` → valida la firma digital
- `SHA256SUMS.txt` → hashes de archivos
- `SHA256SUMS.sig` → firma digital
- `medisoft_pub.pem` → clave pública

## Ejecución paso a paso

### Crear archivos de prueba

```bash
Set-Content config.txt "configuracion"
Set-Content version.txt "v2.1.0"
Set-Content datos.csv "1,2,3"
Set-Content manual.txt "manual usuario"
Set-Content update.log "update ok"
```

### Generar manifiesto de hashes

```bash
python generar_manifiesto.py config.txt version.txt datos.csv manual.txt update.log
```

Resultados esperados:

- Se crea SHA256SUMS.txt
- Cada archivo tiene su hash SHA-256

### Verificar integridad

```bash
python verificar_paquete.py
```

Resultado esperado:

```
[OK] config.txt
[OK] version.txt
[OK] datos.csv
[OK] manual.txt
[OK] update.log
```

### Generar claves RSA

```bash
python generar_claves.py
```

Resultados esperados:
- `medisoft_priv.pem`
- `medisoft_pub.pem`

### Firmar el manifiesto

```bash
python firmar_manifiesto.py
```

Resultado esperado:
- `SHA256SUMS.sig`

### Verificar firma digital

```bash
python verificar_firma.py
```

Resultado esperado:

```
Firma válida: el archivo es auténtico
```

## Pruebas realizadas

### Caso 1: Sistema intacto

```bash
python verificar_firma.py
python verificar_paquete.py
```

Resultado:
- Firma válida  
- Todos los archivos correctos  

### Caso 2: Modificación del manifiesto

```bash
Add-Content SHA256SUMS.txt "cambio malicioso"
python verificar_firma.py
```

Resultado esperado:
- Firma inválida  

### Caso 3: Modificación de archivo

```bash
Add-Content config.txt "cambio"
python verificar_firma.py
python verificar_paquete.py
```

Resultados esperados:

- Firma válida
- `verificar_paquete.py` detecta archivo alterado

## Análisis de resultados

### Comparación de algoritmos (SHA-256)

Se detectaron cambios significativos entre hashes debido al efecto avalancha, demostrando la sensibilidad de SHA-256 ante pequeños cambios.

### Seguridad de MD5

MD5 es inseguro debido a su baja longitud (128 bits) y colisiones conocidas, mientras que SHA-256 es más robusto.

### Verificación con HIBP

Se utilizó SHA-1 parcial (k-anonymity) para consultar la API sin exponer completamente los hashes.

### Validación de firma digital

- La firma protege el manifiesto  
- La integridad protege los archivos  

## Respuesta a Preguntas

### Respuesta Parte 1 - Comparación de algoritmos

1. ¿Cuántos bits cambiaron entre los dos hashes SHA-256? Usen XOR para contarlos. ¿Qué propiedad demuestra esto?

R/ Entre los dos SHA-256 obtenidos para las cadenas "MediSoft-v2.1.0" y "medisoft-v2.1.0" cambiaron 120 bits al comparar ambos valores mediante una operación XOR y contar los bits 1 del resultado. Esto demuestra el efecto avalancha de las funciones hash criptográficas, ya que al hacer un cambio mínimo en el mensaje, aunque sea la mayúscula en la primera letra, produce una salida completamente distinta. Esta propiedad es fundamental en seguridad porque evita que pequeñas modificaciones en el mensaje generen hashes parecidos, lo que dificulta la predicción de patrones y fortalece la detección de alteraciones.

2. Con base en la longitud en bits, explica por qué MD5 es considerado inseguro para integridad de archivos.

R/ MD5 es considerado inseguro para integridad de archivos porque genera solo 128 bits, por lo tanto ofrece una salida mucho menor como algoritmos modernos así como SHA-256, que produce 256 bits. Al tener una salida más corta, la probabilidad de colisiones entre hashes es mayor, siendo que sea más fácil encontrar dos archivos distintos que produzcan el mismo hash. Además MD5 tiene debilidades criptográficas conocidas y colisiones prácticas demostradas, donde un atacante puede manipular archivos sin que el cambio sea detectado.

### Respuesta Parte 5 - Validar firma

1. Al alterar los archivos ¿porque la firma es valida? y  ¿que sucede al ejecutar verificar_paquete.py?

R/ La firma es válida porque fue generada sobre el archivo SHA256SUMS.txt, el cual no fue modificado en una de las pruebas. Aunque el archivo config.txt fue el alterado, el manifiesto firmado permanece intacto, por lo que la verificación con la clave pública sigue siendo correcta. Ahora bien al ejecutar verificar_paquete.py, el sistema detecta que el archivo config.txt fue modificado, ya que su hash SHA-256 actual no coincide con el registrado en SHA256SUMS.txt. Por lo tanto, se marca como [ALTERADO], mientras que los demás archivos permanecen correctos.

## Notas de seguridad

1. El archivo SHA256SUMS.txt se incluye en el repositorio únicamente con fines demostrativos como parte del laboratorio. En un entorno de producción, este archivo sería generado automáticamente durante el proceso de distribución del software.
2. La clave privada (`medisoft_priv.pem`) no se incluye en el repositorio por razones de seguridad.

