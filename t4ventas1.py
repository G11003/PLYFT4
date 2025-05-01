import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parte 1: Arreglo de ventas por semana
ventas_semana = np.array([150, 200, 170, 220, 300, 250, 190])
print("Ventas por semana:", ventas_semana)

# Operaciones con arreglos
print("Promedio de ventas:", np.mean(ventas_semana))
print("Ventas máxima:", np.max(ventas_semana))
print("Ventas mínima:", np.min(ventas_semana))

# Parte 2: Lectura del archivo CSV
datos_ventas = pd.read_csv(r"C:\Users\gd11e\OneDrive\Documentos\8 semestre\Prog Logica y Funcional\T4\ventas.csv", encoding='utf-8')
print("\nDatos de ventas:\n", datos_ventas)

# Parte 3: Agregar columna de Ventas Totales
datos_ventas['Ventas Totales'] = datos_ventas['Unidades Vendidas'] * datos_ventas['Precio Unitario']
print("\nVentas Totales:\n", datos_ventas[['Producto', 'Ventas Totales']])

# Parte 4: Grafica de pastel de unidades vendidas
colores = ['#ED014B', '#C501ED', '#01CDED', '#D1ED01'] 
plt.pie(datos_ventas['Unidades Vendidas'], 
        labels=datos_ventas['Producto'], 
        colors=colores, 
        autopct='%1.1f%%', 
        startangle=140)

plt.title('Proporción de Unidades Vendidas por Producto')
plt.axis('equal') 
plt.tight_layout()
plt.show()
