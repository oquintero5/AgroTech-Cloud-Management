import datetime

# --- CONFIGURACIÓN DE LA FINCA ---
# Registro de Potreros (1 al 7)
# 'dias_limite' define cuántos días puede estar el ganado antes de rotar
potreros = {
    f"Potrero {i}": {
        "ocupado": False, 
        "fecha_entrada": None, 
        "dias_limite": 5
    } for i in range(1, 8)
}

# Simulación: El ganado entró al Potrero 1 hace 6 días
potreros["Potrero 1"]["ocupado"] = True
potreros["Potrero 1"]["fecha_entrada"] = (datetime.datetime.now() - datetime.timedelta(days=6)).strftime("%Y-%m-%d")

def controlar_rotacion():
    """Analiza qué potreros necesitan movimiento de ganado."""
    hoy = datetime.datetime.now()
    alertas = []
    
    print(f"--- REPORTE DE ROTACIÓN - {hoy.strftime('%d/%m/%Y')} ---")
    
    for i in range(1, 8):
        nombre = f"Potrero {i}"
        p = potreros[nombre]
        
        if p["ocupado"]:
            entrada = datetime.datetime.strptime(p["fecha_entrada"], "%Y-%m-%d")
            dias_alla = (hoy - entrada).days
            
            if dias_alla >= p["dias_limite"]:
                siguiente = i + 1 if i < 7 else 1
                msg = f"🔴 {nombre}: ALERTA CRÍTICA. Lleva {dias_alla} días. Mover al Potrero {siguiente} inmediatamente."
            else:
                msg = f"🟢 {nombre}: ESTADO OPTIMO. Lleva {dias_alla} días. Quedan {p['dias_limite'] - dias_alla} días."
            alertas.append(msg)
            
    return alertas

if __name__ == "__main__":
    reporte = controlar_rotacion()
    for linea in reporte:
        print(linea)
