from flask import Flask, jsonify
import pandas as pd

# Cargar los datos desde el archivo CSV
data = pd.read_csv('data/vacunas_sarampion_panama.csv')

# Inicializar la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la raíz de la API
@app.route('/')
def index():
    return "Bienvenido a la API de vacunación contra el sarampión en niños de Panamá."

# Definir una ruta para obtener todos los datos
@app.route('/vacunacion')
def get_vacunacion():
    # Convertir los datos a formato JSON y devolverlos como respuesta
    return jsonify(data.to_dict(orient='records'))

# Definir una ruta para obtener los datos de un año específico
@app.route('/vacunacion/<int:year>')
def get_vacunacion_por_anio(year):
    # Filtrar los datos por el año especificado
    filtered_data = data[data['Year'] == year]
    
    # Verificar si hay datos disponibles para el año especificado
    if filtered_data.empty:
        return f"No se encontraron datos para el año {year}."
    
    # Convertir los datos a formato JSON y devolverlos como respuesta
    return jsonify(filtered_data.to_dict(orient='records'))

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
