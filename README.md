# Agenda_2026
Realizar una Agenda Personalizada

## Descripción
Este proyecto genera un calendario en Excel para el año 2026 con todas las características necesarias para una agenda personalizada.

## Características
- Calendario completo del año 2026
- Una hoja por cada mes
- Días de la semana en español
- Formato visual atractivo con colores
- Fines de semana resaltados
- Fácil de usar y personalizar

## Requisitos
- Python 3.7 o superior
- openpyxl

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/sebastianbarrionuevo-tech/Agenda_2026.git
cd Agenda_2026
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Opción 1: Script básico
Ejecuta el script para generar el calendario:
```bash
python crear_calendario.py
```

Esto creará un archivo llamado `Calendario_2026.xlsx` en el directorio actual.

### Opción 2: Script interactivo con ejemplos
Para usar el script con más opciones:
```bash
python ejemplo_uso.py
```

Este script te permite:
- Generar el calendario básico
- Generar un calendario con eventos personalizados de ejemplo
- Ver información detallada del año 2026
- Ejecutar todas las opciones anteriores

## Estructura del Calendario
- **12 hojas**: Una por cada mes del año
- **Días de la semana**: Lunes a Domingo
- **Formato**: Fechas organizadas por semanas
- **Colores**: Fines de semana resaltados en gris

## Personalización
Puedes modificar el script `crear_calendario.py` para:
- Cambiar los colores
- Ajustar el tamaño de las celdas
- Agregar eventos o notas
- Modificar el formato del calendario
