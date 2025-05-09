# Importar librerías necesarias
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# cargar el dataset de vinos
wine = load_wine()
X = wine.data         # características químicas
y = wine.target       # tipo de vino (clase)

# Dividir los datos en conjunto de entrenamiento 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
random_state=42) # cambiar el test_size acorde el porcentaje de pruba deseado (0.2 para 20%)

# crear y entrenar el modelo de regresión logística (multiclase)
model = LogisticRegression(max_iter=4000) 
model.fit(X_train, y_train)

# realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

print("Precision:", accuracy_score(y_test, y_pred))