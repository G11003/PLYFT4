import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parte 1: Arreglo de productividad semanal
productividad = np.array([75, 80, 90, 85, 70])
print("Productividad semanal:", productividad)

# Cálculos
print("Promedio de productividad:", np.mean(productividad))
print("Productividad máxima:", np.max(productividad))

# Parte 2: Lectura del archivo empleados.csv
datos_empleados = pd.read_csv(r"C:\Users\gd11e\OneDrive\Documentos\8 semestre\Prog Logica y Funcional\T4\empleados.csv", encoding='utf-8')

# Agregar columna Bono (10% del salario)
datos_empleados['Bono'] = datos_empleados['Salario'] * 0.10
print("\nDatos de empleados con Bono:\n", datos_empleados)  # Solo este print se mantiene

# Parte 3: Filtrar empleados del departamento Ventas
empleados_ventas = datos_empleados[datos_empleados['Departamento'] == 'Ventas']
print("\nEmpleados del departamento Ventas:")
print(empleados_ventas[['Nombre', 'Salario', 'Bono']])  # Mostramos solo las columnas relevantes

# Gráfico de barras con salarios
plt.figure(figsize=(10, 6))
plt.bar(datos_empleados['Nombre'], datos_empleados['Salario'], color='#A1A613')

# Titulo y etiquetas
plt.title('Salario de Empleados', fontsize=16)
plt.xlabel('Empleados', fontsize=12)
plt.ylabel('Salario ($)', fontsize=12)
plt.xticks(rotation=90) 

# Mostrar grafico
plt.tight_layout()
plt.show()