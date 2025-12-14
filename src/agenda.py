"""
Main Agenda Application
Electronic Personalized Agenda with Excel, Python, and Database
"""

import argparse
import sys
from datetime import datetime
from database import AgendaDatabase
from excel_manager import ExcelManager


class Agenda:
    """Main agenda application class"""
    
    def __init__(self):
        """Initialize the agenda application"""
        self.db = AgendaDatabase()
        self.excel = ExcelManager(self.db)
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("           AGENDA ELECTRÓNICA PERSONALIZADA 2026")
        print("="*60)
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión de Contactos")
        print("2. Gestión de Eventos")
        print("3. Gestión de Tareas")
        print("4. Exportar a Excel")
        print("5. Importar desde Excel")
        print("6. Crear plantilla Excel")
        print("0. Salir")
        print("-"*60)
    
    def contact_menu(self):
        """Display contacts menu"""
        while True:
            print("\n--- GESTIÓN DE CONTACTOS ---")
            print("1. Ver todos los contactos")
            print("2. Buscar contacto")
            print("3. Agregar contacto")
            print("4. Actualizar contacto")
            print("5. Eliminar contacto")
            print("0. Volver al menú principal")
            
            choice = input("\nSeleccione una opción: ").strip()
            
            if choice == "1":
                self.list_contacts()
            elif choice == "2":
                self.search_contacts()
            elif choice == "3":
                self.add_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "0":
                break
            else:
                print("Opción inválida")
    
    def event_menu(self):
        """Display events menu"""
        while True:
            print("\n--- GESTIÓN DE EVENTOS ---")
            print("1. Ver todos los eventos")
            print("2. Ver eventos por fecha")
            print("3. Agregar evento")
            print("4. Marcar evento como completado")
            print("5. Eliminar evento")
            print("0. Volver al menú principal")
            
            choice = input("\nSeleccione una opción: ").strip()
            
            if choice == "1":
                self.list_events()
            elif choice == "2":
                self.list_events_by_date()
            elif choice == "3":
                self.add_event()
            elif choice == "4":
                self.complete_event()
            elif choice == "5":
                self.delete_event()
            elif choice == "0":
                break
            else:
                print("Opción inválida")
    
    def task_menu(self):
        """Display tasks menu"""
        while True:
            print("\n--- GESTIÓN DE TAREAS ---")
            print("1. Ver todas las tareas")
            print("2. Ver tareas pendientes")
            print("3. Ver tareas completadas")
            print("4. Agregar tarea")
            print("5. Marcar tarea como completada")
            print("6. Eliminar tarea")
            print("0. Volver al menú principal")
            
            choice = input("\nSeleccione una opción: ").strip()
            
            if choice == "1":
                self.list_tasks()
            elif choice == "2":
                self.list_tasks(completado=0)
            elif choice == "3":
                self.list_tasks(completado=1)
            elif choice == "4":
                self.add_task()
            elif choice == "5":
                self.complete_task()
            elif choice == "6":
                self.delete_task()
            elif choice == "0":
                break
            else:
                print("Opción inválida")
    
    # Contact methods
    def list_contacts(self):
        """List all contacts"""
        contacts = self.db.get_contacts()
        if not contacts:
            print("\nNo hay contactos registrados.")
            return
        
        print(f"\n{'ID':<5} {'Nombre':<20} {'Apellido':<20} {'Teléfono':<15} {'Email':<30}")
        print("-" * 90)
        for c in contacts:
            print(f"{c['id']:<5} {c['nombre']:<20} {c['apellido']:<20} {c['telefono']:<15} {c['email']:<30}")
    
    def search_contacts(self):
        """Search contacts by name or email"""
        search = input("Ingrese nombre o email a buscar: ").strip()
        contacts = self.db.get_contacts(search)
        
        if not contacts:
            print(f"\nNo se encontraron contactos con '{search}'")
            return
        
        print(f"\n{'ID':<5} {'Nombre':<20} {'Apellido':<20} {'Teléfono':<15} {'Email':<30}")
        print("-" * 90)
        for c in contacts:
            print(f"{c['id']:<5} {c['nombre']:<20} {c['apellido']:<20} {c['telefono']:<15} {c['email']:<30}")
    
    def add_contact(self):
        """Add a new contact"""
        print("\n--- Agregar Nuevo Contacto ---")
        nombre = input("Nombre (*): ").strip()
        if not nombre:
            print("El nombre es obligatorio.")
            return
        
        apellido = input("Apellido: ").strip()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        direccion = input("Dirección: ").strip()
        notas = input("Notas: ").strip()
        
        contact_id = self.db.add_contact(nombre, apellido, telefono, email, direccion, notas)
        print(f"\n✓ Contacto agregado exitosamente con ID: {contact_id}")
    
    def update_contact(self):
        """Update an existing contact"""
        self.list_contacts()
        contact_id = input("\nIngrese ID del contacto a actualizar: ").strip()
        
        if not contact_id.isdigit():
            print("ID inválido")
            return
        
        print("\nDeje en blanco para mantener el valor actual")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        direccion = input("Dirección: ").strip()
        notas = input("Notas: ").strip()
        
        updates = {}
        if nombre: updates['nombre'] = nombre
        if apellido: updates['apellido'] = apellido
        if telefono: updates['telefono'] = telefono
        if email: updates['email'] = email
        if direccion: updates['direccion'] = direccion
        if notas: updates['notas'] = notas
        
        if updates:
            self.db.update_contact(int(contact_id), **updates)
            print("\n✓ Contacto actualizado exitosamente")
        else:
            print("\nNo se realizaron cambios")
    
    def delete_contact(self):
        """Delete a contact"""
        self.list_contacts()
        contact_id = input("\nIngrese ID del contacto a eliminar: ").strip()
        
        if not contact_id.isdigit():
            print("ID inválido")
            return
        
        confirm = input("¿Está seguro? (s/n): ").strip().lower()
        if confirm == 's':
            self.db.delete_contact(int(contact_id))
            print("\n✓ Contacto eliminado exitosamente")
    
    # Event methods
    def list_events(self):
        """List all events"""
        events = self.db.get_events()
        if not events:
            print("\nNo hay eventos registrados.")
            return
        
        print(f"\n{'ID':<5} {'Título':<25} {'Fecha Inicio':<20} {'Ubicación':<20} {'Completado':<12}")
        print("-" * 82)
        for e in events:
            completado = "✓" if e['completado'] else "✗"
            print(f"{e['id']:<5} {e['titulo']:<25} {e['fecha_inicio']:<20} {str(e['ubicacion'] or ''):<20} {completado:<12}")
    
    def list_events_by_date(self):
        """List events by date range"""
        fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ").strip()
        fecha_fin = input("Fecha fin (YYYY-MM-DD): ").strip()
        
        events = self.db.get_events(fecha_inicio, fecha_fin)
        if not events:
            print("\nNo hay eventos en ese rango de fechas.")
            return
        
        print(f"\n{'ID':<5} {'Título':<25} {'Fecha Inicio':<20} {'Ubicación':<20} {'Completado':<12}")
        print("-" * 82)
        for e in events:
            completado = "✓" if e['completado'] else "✗"
            print(f"{e['id']:<5} {e['titulo']:<25} {e['fecha_inicio']:<20} {str(e['ubicacion'] or ''):<20} {completado:<12}")
    
    def add_event(self):
        """Add a new event"""
        print("\n--- Agregar Nuevo Evento ---")
        titulo = input("Título (*): ").strip()
        if not titulo:
            print("El título es obligatorio.")
            return
        
        descripcion = input("Descripción: ").strip()
        fecha_inicio = input("Fecha inicio (YYYY-MM-DD HH:MM) (*): ").strip()
        if not fecha_inicio:
            print("La fecha de inicio es obligatoria.")
            return
        
        fecha_fin = input("Fecha fin (YYYY-MM-DD HH:MM): ").strip()
        ubicacion = input("Ubicación: ").strip()
        contacto_id = input("ID del contacto (opcional): ").strip()
        recordatorio = input("Recordatorio en minutos (0 para sin recordatorio): ").strip()
        
        event_id = self.db.add_event(
            titulo=titulo,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            ubicacion=ubicacion,
            contacto_id=int(contacto_id) if contacto_id.isdigit() else None,
            recordatorio=int(recordatorio) if recordatorio.isdigit() else 0
        )
        print(f"\n✓ Evento agregado exitosamente con ID: {event_id}")
    
    def complete_event(self):
        """Mark event as complete"""
        self.list_events()
        event_id = input("\nIngrese ID del evento a marcar como completado: ").strip()
        
        if not event_id.isdigit():
            print("ID inválido")
            return
        
        self.db.mark_event_complete(int(event_id), 1)
        print("\n✓ Evento marcado como completado")
    
    def delete_event(self):
        """Delete an event"""
        self.list_events()
        event_id = input("\nIngrese ID del evento a eliminar: ").strip()
        
        if not event_id.isdigit():
            print("ID inválido")
            return
        
        confirm = input("¿Está seguro? (s/n): ").strip().lower()
        if confirm == 's':
            self.db.delete_event(int(event_id))
            print("\n✓ Evento eliminado exitosamente")
    
    # Task methods
    def list_tasks(self, completado=None):
        """List tasks"""
        tasks = self.db.get_tasks(completado)
        if not tasks:
            print("\nNo hay tareas registradas.")
            return
        
        print(f"\n{'ID':<5} {'Título':<30} {'Prioridad':<12} {'Vencimiento':<20} {'Completado':<12}")
        print("-" * 79)
        for t in tasks:
            completado_str = "✓" if t['completado'] else "✗"
            vencimiento = t['fecha_vencimiento'] or 'N/A'
            print(f"{t['id']:<5} {t['titulo']:<30} {t['prioridad']:<12} {str(vencimiento):<20} {completado_str:<12}")
    
    def add_task(self):
        """Add a new task"""
        print("\n--- Agregar Nueva Tarea ---")
        titulo = input("Título (*): ").strip()
        if not titulo:
            print("El título es obligatorio.")
            return
        
        descripcion = input("Descripción: ").strip()
        print("Prioridad: Alta, Media, Baja")
        prioridad = input("Prioridad (default: Media): ").strip() or "Media"
        fecha_vencimiento = input("Fecha vencimiento (YYYY-MM-DD): ").strip()
        
        task_id = self.db.add_task(titulo, descripcion, prioridad, fecha_vencimiento)
        print(f"\n✓ Tarea agregada exitosamente con ID: {task_id}")
    
    def complete_task(self):
        """Mark task as complete"""
        self.list_tasks(completado=0)
        task_id = input("\nIngrese ID de la tarea a marcar como completada: ").strip()
        
        if not task_id.isdigit():
            print("ID inválido")
            return
        
        self.db.mark_task_complete(int(task_id), 1)
        print("\n✓ Tarea marcada como completada")
    
    def delete_task(self):
        """Delete a task"""
        self.list_tasks()
        task_id = input("\nIngrese ID de la tarea a eliminar: ").strip()
        
        if not task_id.isdigit():
            print("ID inválido")
            return
        
        confirm = input("¿Está seguro? (s/n): ").strip().lower()
        if confirm == 's':
            self.db.delete_task(int(task_id))
            print("\n✓ Tarea eliminada exitosamente")
    
    def run(self):
        """Run the main application loop"""
        while True:
            self.show_menu()
            choice = input("\nSeleccione una opción: ").strip()
            
            if choice == "1":
                self.contact_menu()
            elif choice == "2":
                self.event_menu()
            elif choice == "3":
                self.task_menu()
            elif choice == "4":
                filename = input("Nombre del archivo (default: data/agenda_export.xlsx): ").strip()
                filename = filename or "data/agenda_export.xlsx"
                self.excel.export_to_excel(filename)
            elif choice == "5":
                filename = input("Nombre del archivo: ").strip()
                if filename:
                    self.excel.import_from_excel(filename)
            elif choice == "6":
                filename = input("Nombre del archivo (default: templates/agenda_template.xlsx): ").strip()
                filename = filename or "templates/agenda_template.xlsx"
                self.excel.create_template(filename)
            elif choice == "0":
                print("\n¡Hasta luego!")
                self.db.close()
                sys.exit(0)
            else:
                print("\nOpción inválida. Por favor intente de nuevo.")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Agenda Electrónica Personalizada 2026'
    )
    parser.add_argument(
        '--export',
        help='Export data to Excel file',
        metavar='FILE'
    )
    parser.add_argument(
        '--import',
        dest='import_file',
        help='Import data from Excel file',
        metavar='FILE'
    )
    parser.add_argument(
        '--template',
        help='Create Excel template',
        metavar='FILE'
    )
    
    args = parser.parse_args()
    
    agenda = Agenda()
    
    # Handle command line arguments
    if args.export:
        agenda.excel.export_to_excel(args.export)
    elif args.import_file:
        agenda.excel.import_from_excel(args.import_file)
    elif args.template:
        agenda.excel.create_template(args.template)
    else:
        # Run interactive mode
        agenda.run()


if __name__ == "__main__":
    main()
