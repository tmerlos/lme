import yfinance as yf
from datetime import datetime

def generar_html(precio_cobre, precio_aluminio):
    """Esta función crea el archivo que verás en internet"""
    fecha_actual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Precios LME en Vivo</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .container {{ background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; border-top: 8px solid #2c3e50; }}
            h1 {{ color: #2c3e50; margin-bottom: 0.5rem; }}
            .date {{ color: #7f8c8d; margin-bottom: 2rem; font-size: 0.9rem; }}
            .metal-card {{ display: flex; justify-content: space-between; align-items: center; background: #f8f9fa; padding: 1rem 2rem; margin: 10px 0; border-radius: 10px; min-width: 300px; }}
            .metal-name {{ font-weight: bold; color: #34495e; font-size: 1.2rem; }}
            .metal-price {{ color: #2980b9; font-size: 1.5rem; font-weight: bold; }}
            .unit {{ font-size: 0.8rem; color: #95a5a6; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Cotizaciones LME</h1>
            <div class="date">Última actualización: {fecha_actual} (Retraso 30min)</div>
            
            <div class="metal-card">
                <span class="metal-name">COBRE</span>
                <div>
                    <span class="metal-price">${precio_cobre:,.2f}</span>
                    <span class="unit">USD/t</span>
                </div>
            </div>

            <div class="metal-card">
                <span class="metal-name">ALUMINIO</span>
                <div>
                    <span class="metal-price">${precio_aluminio:,.2f}</span>
                    <span class="unit">USD/t</span>
                </div>
            </div>
            
            <p style="margin-top: 2rem; font-size: 0.7rem; color: #bdc3c7;">Datos obtenidos automáticamente vía Yahoo Finance</p>
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("¡Archivo index.html generado con éxito!")

def obtener_datos_mercado():
    print("Obteniendo datos de mercado...")
    try:
        # HG=F es el futuro del cobre (Comex/LME proxy)
        # ALI=F es el futuro del aluminio
        cobre = yf.Ticker("HG=F")
        aluminio = yf.Ticker("ALI=F")

        # Precio actual (último cierre)
# ... (al final de tu script)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Proceso finalizado con éxito.")
# ... (esto va al final de tu función donde generas el HTML)
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_template)
        print("ÉXITO: Archivo index.html escrito correctamente.")
    except Exception as e:
        print(f"ERROR al escribir el archivo: {e}")

if __name__ == "__main__":
    obtener_datos_mercado()
