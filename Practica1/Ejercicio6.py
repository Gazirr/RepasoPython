Productos = [
    ("Manzana",0.50),
    ("Platano",0.30),
    ("Naranja",0.40),
    ("Pera",0.60),
    ("Mango",1.20)
]

print(f"{'Producto':<15} | {'Precio (€)':<10}")

for nombre,precio in Productos:
    print(f"{nombre:<15} | {precio:<10.2f}")