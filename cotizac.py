from flask import Flask, render_template
import datetime
import random # Importamos esto solo para simular cambios de precio al probar

app = Flask(__name__)

def obtener_precios_lme():
    """
    Función para obtener precios. 
    NOTA: Aquí es donde conectarías tu script de scraping real.
    Por ahora, genero datos de prueba para que veas que la web funciona.
    """
    fecha_hoy = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Estos son datos de ejemplo. 
    # Cuando tengas tu script de scraping listo, reemplazarás esto.
    datos = [
        {
            'metal': 'Cobre (Copper)', 
            'precio': f"{random.uniform(8500, 9700):,.2f}", 
            'fecha': fecha_hoy
        },
        {
            'metal': 'Aluminio (Aluminium)', 
            'precio': f"{random.uniform(2100, 2500):,.2f}", 
            'fecha': fecha_hoy
        }
    ]
    return datos

@app.route('/')
def pagina_principal():
    # 1. Obtenemos la lista de precios
    mis_datos = obtener_precios_lme()
    
    # 2. Se la enviamos al archivo HTML que creaste antes
    # Flask buscará 'index.html' automáticamente dentro de la carpeta 'templates'
    return render_template('index.html', datos=mis_datos)

if __name__ == '__main__':
    # debug=True permite que si haces cambios en el código, se actualice solo
    app.run(debug=True, port=5000)
