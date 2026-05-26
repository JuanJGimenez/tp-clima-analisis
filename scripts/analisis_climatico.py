import os
import pandas as pd
import matplotlib.pyplot as plt

# rutas relativas
CARPETA_DATOS      = "datos"
CARPETA_RESULTADOS = "resultados"
os.makedirs(CARPETA_RESULTADOS, exist_ok=True)

ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "estadisticas.txt")
ESTACION      = "MAR DEL PLATA AERO"
MESES         = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]

print("--- TPCA-2: Análisis climático Mar del Plata (1981-2010) ---")

try:
    # carga del dataset
    # se usa header=5 porque las primeras 5 filas del archivo son
    # encabezados informativos del SMN, no datos reales
    df = pd.read_csv(ARCHIVO_DATOS, sep="\t", encoding="latin-1", header=5)
    df.columns = ["Estacion", "Variable"] + MESES

    # Filtrar estación Mar del Plata
    mdp = df[df["Estacion"] == ESTACION].copy()


    # extraer variables por posición dentro de la estación
    # se filtra por posición (iloc) en lugar de por nombre de variable
    # porque el archivo tiene caracteres especiales (tildes) que
    # varían según el encoding del sistema
    # se usa pd.to_numeric con errors="coerce" para convertir "S/D"
    # (sin dato) a NaN en lugar de generar un error
    filas = mdp.reset_index(drop=True)
    temp_media = pd.to_numeric(filas.loc[0, MESES], errors="coerce")
    temp_max   = pd.to_numeric(filas.loc[1, MESES], errors="coerce")
    temp_min   = pd.to_numeric(filas.loc[2, MESES], errors="coerce")
    precip     = pd.to_numeric(filas.loc[6, MESES], errors="coerce")

    # indicadores
    print(f"Temperatura promedio anual : {temp_media.mean():.1f} °C")
    print(f"Temperatura máxima         : {temp_max.max():.1f} °C")
    print(f"Temperatura mínima         : {temp_min.min():.1f} °C")
    print(f"Precipitación promedio     : {precip.mean():.1f} mm")

    # guardar indicadores
    with open(os.path.join(CARPETA_RESULTADOS, "indicadores.txt"), "w") as f:
        f.write(f"Estacion: {ESTACION}\n")
        f.write(f"Periodo: 1981-2010\n")
        f.write(f"Temperatura promedio anual : {temp_media.mean():.1f} C\n")
        f.write(f"Temperatura maxima         : {temp_max.max():.1f} C\n")
        f.write(f"Temperatura minima         : {temp_min.min():.1f} C\n")
        f.write(f"Precipitacion promedio     : {precip.mean():.1f} mm\n")
    print("✓ Indicadores guardados.")

    # gráfico
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # gráfico de temperatura
    # se grafican las 3 temperaturas juntas para visualizar
    # la amplitud térmica mensual de Mar del Plata
    ax1.plot(MESES, temp_media, color="darkred",  marker="o", label="Temperatura media")
    ax1.plot(MESES, temp_max,   color="orange",   marker="o", label="Temperatura máxima")
    ax1.plot(MESES, temp_min,   color="steelblue", marker="o", label="Temperatura mínima")
    ax1.set_title("Evolución mensual de temperatura — Mar del Plata (1981-2010)")
    ax1.set_ylabel("Temperatura (°C)")
    ax1.legend()
    ax1.grid(alpha=0.3)

    # Gráfico de precipitaciones
    ax2.bar(MESES, precip, color="steelblue", alpha=0.7)
    ax2.set_title("Precipitación mensual — Mar del Plata (1981-2010)")
    ax2.set_ylabel("Precipitación (mm)")
    ax2.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_RESULTADOS, "grafico_temperatura.png"), dpi=150)
    plt.close()
    print("✓ Gráfico guardado.")

except FileNotFoundError:
    print(f"Error: No se encontró {ARCHIVO_DATOS}")
except Exception as e:
    print(f"Error inesperado: {e}")