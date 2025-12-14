# Agenda Electrónica Personalizada 2026

Una agenda electrónica completa desarrollada en Python con integración de Excel y base de datos SQLite para gestionar contactos, eventos y tareas.

## 📋 Características

- **Gestión de Contactos**: Agregar, buscar, actualizar y eliminar contactos con información completa (nombre, teléfono, email, dirección, notas)
- **Gestión de Eventos**: Organizar eventos y citas con fechas, ubicaciones, recordatorios y asociación con contactos
- **Gestión de Tareas**: Administrar tareas pendientes con prioridades (Alta, Media, Baja) y fechas de vencimiento
- **Integración con Excel**: Exportar e importar datos desde/hacia archivos Excel para fácil edición
- **Base de Datos SQLite**: Almacenamiento persistente y confiable de toda la información
- **Interfaz de línea de comandos**: Menús interactivos fáciles de usar

## 🚀 Instalación

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clone el repositorio:
```bash
git clone https://github.com/sebastianbarrionuevo-tech/Agenda_2026.git
cd Agenda_2026
```

2. Instale las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Modo Interactivo

Para iniciar la aplicación en modo interactivo:

```bash
cd src
python agenda.py
```

Esto mostrará el menú principal donde puede:
1. Gestionar contactos
2. Gestionar eventos
3. Gestionar tareas
4. Exportar datos a Excel
5. Importar datos desde Excel
6. Crear plantilla de Excel

### Modo Línea de Comandos

#### Crear una plantilla de Excel:
```bash
python src/agenda.py --template templates/mi_agenda.xlsx
```

#### Exportar datos a Excel:
```bash
python src/agenda.py --export data/agenda_export.xlsx
```

#### Importar datos desde Excel:
```bash
python src/agenda.py --import data/agenda_import.xlsx
```

## 📁 Estructura del Proyecto

```
Agenda_2026/
├── src/
│   ├── agenda.py         # Aplicación principal con interfaz CLI
│   ├── database.py       # Gestión de base de datos SQLite
│   └── excel_manager.py  # Integración con Excel
├── data/                 # Directorio para archivos de base de datos y exportaciones
├── templates/            # Plantillas de Excel
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo
```

## 🗄️ Estructura de la Base de Datos

### Tabla: contactos
- `id`: Identificador único
- `nombre`: Nombre del contacto (requerido)
- `apellido`: Apellido del contacto
- `telefono`: Número de teléfono
- `email`: Correo electrónico
- `direccion`: Dirección física
- `notas`: Notas adicionales
- `fecha_creacion`: Fecha de creación
- `fecha_actualizacion`: Fecha de última actualización

### Tabla: eventos
- `id`: Identificador único
- `titulo`: Título del evento (requerido)
- `descripcion`: Descripción del evento
- `fecha_inicio`: Fecha y hora de inicio (requerido)
- `fecha_fin`: Fecha y hora de fin
- `ubicacion`: Ubicación del evento
- `contacto_id`: Relación con contacto
- `recordatorio`: Minutos antes para recordatorio
- `completado`: Estado de completado (0/1)
- `fecha_creacion`: Fecha de creación

### Tabla: tareas
- `id`: Identificador único
- `titulo`: Título de la tarea (requerido)
- `descripcion`: Descripción de la tarea
- `prioridad`: Prioridad (Alta, Media, Baja)
- `fecha_vencimiento`: Fecha de vencimiento
- `completado`: Estado de completado (0/1)
- `fecha_creacion`: Fecha de creación
- `fecha_completado`: Fecha de completado

## 📊 Formato de Excel

El sistema utiliza archivos Excel con tres hojas:

1. **Contactos**: Con columnas para ID, Nombre, Apellido, Teléfono, Email, Dirección, Notas
2. **Eventos**: Con columnas para ID, Título, Descripción, Fecha Inicio, Fecha Fin, Ubicación, ID Contacto, Recordatorio, Completado
3. **Tareas**: Con columnas para ID, Título, Descripción, Prioridad, Fecha Vencimiento, Completado, Fecha Completado

## 🔧 Ejemplos de Uso

### Agregar un contacto:
1. Ejecutar la aplicación
2. Seleccionar opción "1. Gestión de Contactos"
3. Seleccionar opción "3. Agregar contacto"
4. Ingresar los datos solicitados

### Crear un evento:
1. Ejecutar la aplicación
2. Seleccionar opción "2. Gestión de Eventos"
3. Seleccionar opción "3. Agregar evento"
4. Ingresar título, fecha y otros datos

### Exportar a Excel para edición:
1. Ejecutar la aplicación
2. Seleccionar opción "4. Exportar a Excel"
3. Ingresar el nombre del archivo o usar el predeterminado
4. Abrir el archivo Excel generado
5. Editar los datos en Excel
6. Importar de vuelta usando opción "5. Importar desde Excel"

## 🛠️ Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación principal
- **SQLite**: Base de datos relacional ligera
- **openpyxl**: Biblioteca para leer y escribir archivos Excel
- **argparse**: Para procesamiento de argumentos de línea de comandos

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue o pull request para sugerencias o mejoras.

## 📧 Contacto

Para preguntas o sugerencias, por favor contacte al desarrollador a través de GitHub.

## 🔜 Funcionalidades Futuras

- Interfaz gráfica (GUI) con tkinter o PyQt
- Sincronización con Google Calendar
- Notificaciones de recordatorios
- Búsqueda avanzada y filtros
- Exportación a PDF
- Respaldo automático en la nube
