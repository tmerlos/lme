import requests
import os
from datetime import datetime

# --- CONFIGURACIÓN ---
API_KEY = os.getenv("MY_API_KEY") 
BASE_URL = "https://commodities-api.com/api/latest"

def actualizar_web(precio_cobre, precio_aluminio):
    """Genera un archivo index.html con los precios"""
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # El contenido HTML entre las comillas triples
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Precios LME</title>
        <style>
            body {{ font-family: sans-serif; text-align: center; padding: 50px; background: #f0f2f5; }}
            .box {{ background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #1a73e8; }}
            .precio {{ font-size: 24px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Cotización Metales LME</h1>
            <p>Última actualización: {fecha}</p>
            <p class="precio">Cobre: ${precio_cobre:,.2f} USD/ton</p>
            <p class="precio">Aluminio: ${precio_aluminio:,.2f} USD/ton</p>
        </div>
    </body>
    </html>
    """
    
    # Escribir el archivo (Asegúrate de que esta línea esté indentada dentro de la función)
    with open("index.html", "w", encoding='utf-8') as f:
        f.write(html_content)

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
            p_cobre = 1 / rates['LME-XCU']
            p_aluminio = 1 / rates['LME-ALU']
            
            # Llamamos a la función
            actualizar_web(p_cobre, p_aluminio)
            print("Web actualizada con éxito.")
        else:
            print("Error en API:", data.get('error'))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    obtener_datos()
