# Hashes_Firmas_CdI

## Respuesta Parte 1 - Comparación de algoritmos

1. ¿Cuántos bits cambiaron entre los dos hashes SHA-256? Usen XOR para contarlos. ¿Qué propiedad demuestra esto?

R/ Entre los dos SHA-256 obtenidos para las cadenas "MediSoft-v2.1.0" y "medisoft-v2.1.0" cambiaron 120 bits al comparar ambos valores mediante una operación XOR y contar los bits 1 del resultado. Esto demuestra el efecto avalancha de las funciones hash criptográficas, ya que al hacer un cambio mínimo en el mensaje, aunque sea la mayúscula en la primera letra, produce una salida completamente distinta. Esta propiedad es fundamental en seguridad porque evita que pequeñas modificaciones en el mensaje generen hashes parecidos, lo que dificulta la predicción de patrones y fortalece la detección de alteraciones.

2. Con base en la longitud en bits, explica por qué MD5 es considerado inseguro para integridad de archivos.

R/ MD5 es considerado inseguro para integridad de archivos porque genera solo 128 bits, por lo tanto ofrece una salida mucho menor como algoritmos modernos así como SHA-256, que produce 256 bits. Al tener una salida más corta, la probabilidad de colisiones entre hashes es mayor, siendo que sea más fácil encontrar dos archivos distintos que produzcan el mismo hash. Además MD5 tiene debilidades criptográficas conocidas y colisiones prácticas demostradas, donde un atacante puede manipular archivos sin que el cambio sea detectado.