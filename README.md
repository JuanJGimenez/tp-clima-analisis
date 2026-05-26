Análisis de Datos Climáticos — Mar del Plata
Alumno: Gimenez Juan Jose

Integrantes

P1 - Líder y Organizador (Rol. Hugo)
P2 - Desarrollador Técnico (Rol: Paco)
P3 - Revisor y QA (Rol: Luis)

Escenario elegido: Escenario A — Análisis de Datos Climáticos

Análisis de estadísticas climatológicas históricas de la estación
Mar del Plata Aero para el período 1981-2010.

Dataset utilizado:

Fuente: Servicio Meteorológico Nacional de Argentina (SMN)
Archivo: datos/estadisticas.txt

Instrucciones para ejecutar el script:

1. Clonar el repositorio:
bash
   git clone https://github.com/JuanJGimenez/tp-clima-analisis.git

2. Abrir Google Colab y subir el notebook `.ipynb`
3. Asegurarse de que el archivo `datos/estadisticas.txt` esté presente
4. Ejecutar el script desde una celda:
bash
   !python scripts/analisis_climatico.py

5. Los resultados se guardan automáticamente en `/resultados`

Estructura del repositorio:

tp-clima-analisis/
├── datos/
│   └── estadisticas.txt
├── scripts/
│   └── analisis_climatico.py
├── resultados/
│   ├── indicadores.txt
│   └── grafico_temperatura.png
├── README.md
└── .gitignore

Cátedra: 

Organización Empresarial — UTN · Tecnicatura Universitaria en Programación · 2026