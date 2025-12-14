# Guía de Inicio Rápido - Agenda 2026

## 🚀 Instalación y Primer Uso

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar el ejemplo de demostración
```bash
python example_usage.py
```

Este comando creará:
- Una base de datos con datos de ejemplo (`data/agenda.db`)
- Un archivo Excel exportado (`data/agenda_export.xlsx`)
- Una plantilla Excel (`templates/agenda_template.xlsx`)

### 3. Usar la aplicación interactiva
```bash
cd src
python agenda.py
```

## 📖 Tutoriales Rápidos

### Tutorial 1: Agregar un contacto

1. Ejecuta `python src/agenda.py`
2. Selecciona opción `1` (Gestión de Contactos)
3. Selecciona opción `3` (Agregar contacto)
4. Ingresa la información solicitada
5. ¡Listo! Tu contacto ha sido guardado

### Tutorial 2: Crear un evento

1. Ejecuta `python src/agenda.py`
2. Selecciona opción `2` (Gestión de Eventos)
3. Selecciona opción `3` (Agregar evento)
4. Ingresa título: `Reunión importante`
5. Ingresa fecha inicio: `2026-01-15 14:00`
6. Completa los demás campos
7. ¡Tu evento ha sido creado!

### Tutorial 3: Agregar una tarea

1. Ejecuta `python src/agenda.py`
2. Selecciona opción `3` (Gestión de Tareas)
3. Selecciona opción `4` (Agregar tarea)
4. Ingresa título: `Revisar documentos`
5. Selecciona prioridad: `Alta`, `Media` o `Baja`
6. Ingresa fecha de vencimiento: `2026-01-20`
7. ¡Tu tarea ha sido creada!

### Tutorial 4: Exportar a Excel

1. Ejecuta `python src/agenda.py`
2. Selecciona opción `4` (Exportar a Excel)
3. Ingresa nombre de archivo o presiona Enter para usar el predeterminado
4. Abre el archivo Excel generado para ver tus datos

### Tutorial 5: Editar datos en Excel e importar

1. Exporta tus datos a Excel (Tutorial 4)
2. Abre el archivo Excel con Microsoft Excel, LibreOffice Calc, o Google Sheets
3. Edita los datos directamente en Excel:
   - Agrega nuevas filas (deja el ID vacío para nuevos registros)
   - Modifica datos existentes
   - **No elimines las columnas de encabezado**
4. Guarda el archivo
5. Ejecuta `python src/agenda.py`
6. Selecciona opción `5` (Importar desde Excel)
7. Ingresa la ruta del archivo Excel
8. ¡Los cambios se sincronizarán con la base de datos!

## 💡 Comandos rápidos desde terminal

```bash
# Crear una plantilla nueva
python src/agenda.py --template mi_plantilla.xlsx

# Exportar datos actuales
python src/agenda.py --export mi_backup.xlsx

# Importar datos de un archivo
python src/agenda.py --import datos_nuevos.xlsx
```

## 📝 Formato de fechas

- **Fechas**: `YYYY-MM-DD` (ejemplo: `2026-01-15`)
- **Fechas con hora**: `YYYY-MM-DD HH:MM` (ejemplo: `2026-01-15 14:30`)

## 🎯 Consejos Útiles

1. **Respaldo regular**: Exporta tus datos a Excel regularmente como respaldo
2. **Prioridades**: Usa `Alta`, `Media`, o `Baja` para tareas
3. **Búsqueda**: Usa la función de búsqueda para encontrar contactos rápidamente
4. **Excel**: Puedes abrir los archivos exportados con cualquier programa de hojas de cálculo
5. **Base de datos**: El archivo `data/agenda.db` contiene todos tus datos

## ⚠️ Importante

- No modifiques manualmente el archivo `agenda.db`
- Al importar desde Excel, deja el campo ID vacío para nuevos registros
- Las columnas en Excel deben mantener el mismo orden que la plantilla
- Siempre haz una copia de seguridad antes de importar datos masivos

## 🆘 Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'openpyxl'"
**Solución**: Ejecuta `pip install -r requirements.txt`

### Error: "No such file or directory"
**Solución**: Asegúrate de estar en el directorio correcto del proyecto

### Los cambios en Excel no se importan
**Solución**: Verifica que las columnas coincidan con la plantilla y que los formatos de fecha sean correctos

### No puedo ver mis datos
**Solución**: Verifica que estés usando el mismo archivo de base de datos (`data/agenda.db`)

## 📞 Obtener Ayuda

Para ver todas las opciones disponibles:
```bash
python src/agenda.py --help
```

¡Disfruta tu nueva agenda electrónica personalizada! 🎉
