from pathlib import Path

carpeta = Path(__file__).parent / "pruebas"

for archivo in carpeta.glob("*.txt"):
    nuevo_nombre = archivo.with_name("importante_" + archivo.name)
    print(f"Renombrando: {archivo.name} -> {nuevo_nombre.name}")
    archivo.rename(nuevo_nombre)

print("Listo. Archivos en la carpeta:")
for archivo in carpeta.iterdir():
    print(" -", archivo.name)