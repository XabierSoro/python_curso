print("CALCULADORA DE IVA")
precio = float(input("Introduce el precio sin IVA ")) 
porcentaje = 21 # Este es el valor del IVA, 21%
iva = (precio*porcentaje)/100
total = precio + iva
print (f"El precio sin IVA es {precio} € ")
print(f"El IVA es de {iva} € ")
print(f"El precio con IVA es de {total} € ")
print(f'completed in {total:.2f}')
