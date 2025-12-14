"""
Example usage of the Agenda 2026 system
This script demonstrates how to use the agenda programmatically
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from database import AgendaDatabase
from excel_manager import ExcelManager


def example_usage():
    """Demonstrate the usage of the agenda system"""
    
    print("="*60)
    print("    EJEMPLO DE USO - AGENDA ELECTRÓNICA 2026")
    print("="*60)
    
    # Initialize database
    print("\n1. Inicializando base de datos...")
    db = AgendaDatabase("data/agenda.db")
    print("   ✓ Base de datos creada")
    
    # Add sample contacts
    print("\n2. Agregando contactos de ejemplo...")
    contact1_id = db.add_contact(
        nombre="Juan",
        apellido="Pérez",
        telefono="+54 11 1234-5678",
        email="juan.perez@email.com",
        direccion="Av. Corrientes 1234, Buenos Aires",
        notas="Cliente importante"
    )
    print(f"   ✓ Contacto agregado: Juan Pérez (ID: {contact1_id})")
    
    contact2_id = db.add_contact(
        nombre="María",
        apellido="González",
        telefono="+54 11 8765-4321",
        email="maria.gonzalez@email.com",
        direccion="Calle Florida 567, Buenos Aires",
        notas="Proveedor"
    )
    print(f"   ✓ Contacto agregado: María González (ID: {contact2_id})")
    
    contact3_id = db.add_contact(
        nombre="Carlos",
        apellido="Rodríguez",
        telefono="+54 11 5555-1234",
        email="carlos.rodriguez@email.com",
        direccion="Av. Santa Fe 890, Buenos Aires"
    )
    print(f"   ✓ Contacto agregado: Carlos Rodríguez (ID: {contact3_id})")
    
    # Add sample events
    print("\n3. Agregando eventos de ejemplo...")
    event1_id = db.add_event(
        titulo="Reunión de equipo",
        descripcion="Reunión mensual del equipo de desarrollo",
        fecha_inicio="2026-01-15 10:00",
        fecha_fin="2026-01-15 11:30",
        ubicacion="Sala de conferencias",
        contacto_id=contact1_id,
        recordatorio=30
    )
    print(f"   ✓ Evento agregado: Reunión de equipo (ID: {event1_id})")
    
    event2_id = db.add_event(
        titulo="Presentación de proyecto",
        descripcion="Presentación del proyecto final al cliente",
        fecha_inicio="2026-01-20 14:00",
        fecha_fin="2026-01-20 16:00",
        ubicacion="Oficina del cliente",
        contacto_id=contact2_id,
        recordatorio=60
    )
    print(f"   ✓ Evento agregado: Presentación de proyecto (ID: {event2_id})")
    
    event3_id = db.add_event(
        titulo="Conferencia anual",
        descripcion="Conferencia anual de tecnología",
        fecha_inicio="2026-02-10 09:00",
        fecha_fin="2026-02-10 18:00",
        ubicacion="Centro de Convenciones",
        recordatorio=120
    )
    print(f"   ✓ Evento agregado: Conferencia anual (ID: {event3_id})")
    
    # Add sample tasks
    print("\n4. Agregando tareas de ejemplo...")
    task1_id = db.add_task(
        titulo="Revisar código del proyecto",
        descripcion="Realizar code review del módulo de autenticación",
        prioridad="Alta",
        fecha_vencimiento="2026-01-10"
    )
    print(f"   ✓ Tarea agregada: Revisar código del proyecto (ID: {task1_id})")
    
    task2_id = db.add_task(
        titulo="Actualizar documentación",
        descripcion="Actualizar la documentación del API",
        prioridad="Media",
        fecha_vencimiento="2026-01-18"
    )
    print(f"   ✓ Tarea agregada: Actualizar documentación (ID: {task2_id})")
    
    task3_id = db.add_task(
        titulo="Preparar informe mensual",
        descripcion="Preparar informe de actividades del mes",
        prioridad="Alta",
        fecha_vencimiento="2026-01-31"
    )
    print(f"   ✓ Tarea agregada: Preparar informe mensual (ID: {task3_id})")
    
    task4_id = db.add_task(
        titulo="Organizar escritorio",
        descripcion="Ordenar y limpiar el área de trabajo",
        prioridad="Baja",
        fecha_vencimiento="2026-01-12"
    )
    print(f"   ✓ Tarea agregada: Organizar escritorio (ID: {task4_id})")
    
    # Display contacts
    print("\n5. Listando contactos...")
    contacts = db.get_contacts()
    print(f"   Total de contactos: {len(contacts)}")
    for c in contacts:
        print(f"   - {c['nombre']} {c['apellido']} ({c['email']})")
    
    # Display events
    print("\n6. Listando eventos...")
    events = db.get_events()
    print(f"   Total de eventos: {len(events)}")
    for e in events:
        print(f"   - {e['titulo']} - {e['fecha_inicio']}")
    
    # Display tasks
    print("\n7. Listando tareas...")
    tasks = db.get_tasks()
    print(f"   Total de tareas: {len(tasks)}")
    for t in tasks:
        status = "✓" if t['completado'] else "✗"
        print(f"   {status} [{t['prioridad']}] {t['titulo']}")
    
    # Mark a task as complete
    print("\n8. Marcando tarea como completada...")
    db.mark_task_complete(task4_id, 1)
    print(f"   ✓ Tarea '{task4_id}' marcada como completada")
    
    # Search contacts
    print("\n9. Buscando contactos...")
    search_results = db.get_contacts("María")
    print(f"   Resultados para 'María': {len(search_results)}")
    for c in search_results:
        print(f"   - {c['nombre']} {c['apellido']}")
    
    # Export to Excel
    print("\n10. Exportando datos a Excel...")
    excel = ExcelManager(db)
    excel.export_to_excel("data/agenda_export.xlsx")
    print("   ✓ Datos exportados a 'data/agenda_export.xlsx'")
    
    # Create template
    print("\n11. Creando plantilla de Excel...")
    excel.create_template("templates/agenda_template.xlsx")
    print("   ✓ Plantilla creada en 'templates/agenda_template.xlsx'")
    
    # Close database
    print("\n12. Cerrando conexión a base de datos...")
    db.close()
    print("   ✓ Conexión cerrada")
    
    print("\n" + "="*60)
    print("  ¡EJEMPLO COMPLETADO CON ÉXITO!")
    print("="*60)
    print("\nAhora puede:")
    print("1. Ejecutar 'python src/agenda.py' para usar la aplicación interactiva")
    print("2. Abrir 'data/agenda_export.xlsx' para ver los datos en Excel")
    print("3. Usar 'templates/agenda_template.xlsx' como plantilla para importar datos")
    print("="*60)


if __name__ == "__main__":
    example_usage()
