# Renombrador de archivos

Script en Python que añade un prefijo a todos los archivos `.txt` de una
carpeta. Es un mini-proyecto para practicar el manejo de archivos con
`pathlib`.

## Qué hace

- Recorre los archivos `.txt` de la carpeta `pruebas/`.
- A cada uno le añade el prefijo `importante_` al principio del nombre.
- Va mostrando los renombrados y, al final, lista la carpeta.

## Cómo ejecutarlo

```bash
python renombrador.py
```

Para volver a probarlo desde cero, crea de nuevo algunos `.txt` dentro
de `pruebas/`.

## Aprendido con este proyecto

- `pathlib`: `Path`, `__file__`, `parent`, `glob`, `with_name`, `rename`, `iterdir`
- Renombrar archivos en lote

## Aviso (lección de diseño)

Este script **no es idempotente**: si lo ejecutas dos veces, añade el
prefijo otra vez (`nota.txt` → `importante_nota.txt` → `importante_importante_nota.txt`).
Es un buen recordatorio de por qué conviene diseñar scripts que se puedan
re-ejecutar sin estropear los datos.
