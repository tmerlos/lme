import requests
import os
from datetime import datetime

# --- CONFIGURACIÓN ---
# Usamos os.getenv para mayor seguridad en GitHub
API_KEY = os.getenv("MY_API_KEY") 
BASE_URL = "https://commodities-api.com/api/latest"

def actualizar_web(precio_cobre, precio_aluminio):
    """Genera un archivo index.html con los precios"""
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Precios Metales LME</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; padding: 50px; }}
            .card {{ background: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; padding: 20px; min-width: 300px; }}
            h1 {{ color: #333; }}
            .precio {{ font-size: 28px; color: #2c3e50; font-weight: bold; }}
            .fecha {{ color: #7f8c8d; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Cotización Metales LME</h1>
            <p class="fecha">Última actualización: {fecha}</p>
            <hr>
            <p><strong>Cobre:</strong> <span class="precio">${precio_cobre:,.2f} USD/t</span></p>
            <p><strong>Aluminio:</strong> <span class="precio">${precio_aluminio:,.2f} USD/t</span></p>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding='utf-8') as f:
        f.write(html_content)
    print("Archivo index.html actualizado.")

def obtener_datos():
    params = {
        'access_key': API_KEY,
        'base': 'USD',
        'symbols': 'LME-XCU,LME-ALU'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get('success'):
            rates = data['rates']
            # Convertimos a precio por tonelada
            p_cobre = 1 / rates['LME-XCU']
            p_aluminio = 1 / rates['LME-ALU']
            
            # LLAMAMOS A LA FUNCIÓN PARA CREAR EL HTML
            actualizar_web(p_cobre, p_aluminio)
        else:
            print("Error en la API:", data.get('error'))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    obtener_datos()
