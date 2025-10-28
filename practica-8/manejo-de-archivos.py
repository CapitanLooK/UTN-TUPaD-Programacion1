archivo_productos = "productos.txt"

productos = []
with open(archivo_productos, "r", encoding="utf-8") as f:
    for linea in f:
        partes = linea.strip().split(",")
        if len(partes) == 3:
            nombre = partes[0]
            precio = float(partes[1])
            cantidad = int(partes[2])
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

print("Productos actuales:")
for prod in productos:
    print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")

agregar = input("¿Desea agregar un producto? (s/n): ").lower()
if agregar == "s":
    nombre = input("Ingrese nombre del producto: ").strip()
    precio = input("Ingrese precio: ").strip()
    cantidad = input("Ingrese cantidad: ").strip()
    if nombre and precio.replace('.', '', 1).isdigit() and cantidad.isdigit():
        precio = float(precio)
        cantidad = int(cantidad)
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        with open(archivo_productos, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{precio},{cantidad}\n")
        print("Producto agregado correctamente.")
    else:
        print("Datos invalidos. No se agrego el producto.")

buscar = input("Ingrese el nombre de un producto para buscar: ").strip()
encontrado = False
for prod in productos:
    if prod["nombre"].lower() == buscar.lower():
        print(f"Encontrado: Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("No se encontro el producto.")

with open(archivo_productos, "w", encoding="utf-8") as f:
    for prod in productos:
        f.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")
print("Archivo actualizado con todos los productos.")