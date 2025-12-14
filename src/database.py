"""
Database module for Agenda 2026
Manages SQLite database operations for contacts, events, and tasks
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
import os


class AgendaDatabase:
    """Main database class for the electronic agenda"""
    
    def __init__(self, db_path: str = "data/agenda.db"):
        """Initialize database connection"""
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = None
        self.create_tables()
    
    def get_connection(self):
        """Get or create database connection"""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
        return self.conn
    
    def create_tables(self):
        """Create all necessary tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Contacts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT,
                telefono TEXT,
                email TEXT,
                direccion TEXT,
                notas TEXT,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Events/Appointments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                fecha_inicio TIMESTAMP NOT NULL,
                fecha_fin TIMESTAMP,
                ubicacion TEXT,
                contacto_id INTEGER,
                recordatorio INTEGER DEFAULT 0,
                completado INTEGER DEFAULT 0,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (contacto_id) REFERENCES contactos (id)
            )
        ''')
        
        # Tasks/To-do table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                prioridad TEXT DEFAULT 'Media',
                fecha_vencimiento TIMESTAMP,
                completado INTEGER DEFAULT 0,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_completado TIMESTAMP
            )
        ''')
        
        conn.commit()
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    # Contact operations
    def add_contact(self, nombre: str, apellido: str = "", telefono: str = "",
                   email: str = "", direccion: str = "", notas: str = "") -> int:
        """Add a new contact"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contactos (nombre, apellido, telefono, email, direccion, notas)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, apellido, telefono, email, direccion, notas))
        conn.commit()
        return cursor.lastrowid
    
    def get_contacts(self, search: str = "") -> List[Dict]:
        """Get all contacts or search by name"""
        conn = self.get_connection()
        cursor = conn.cursor()
        if search:
            cursor.execute('''
                SELECT * FROM contactos 
                WHERE nombre LIKE ? OR apellido LIKE ? OR email LIKE ?
                ORDER BY nombre, apellido
            ''', (f'%{search}%', f'%{search}%', f'%{search}%'))
        else:
            cursor.execute('SELECT * FROM contactos ORDER BY nombre, apellido')
        return [dict(row) for row in cursor.fetchall()]
    
    def update_contact(self, contact_id: int, **kwargs):
        """Update contact information"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        fields = []
        values = []
        for key, value in kwargs.items():
            if key in ['nombre', 'apellido', 'telefono', 'email', 'direccion', 'notas']:
                fields.append(f"{key} = ?")
                values.append(value)
        
        if fields:
            fields.append("fecha_actualizacion = ?")
            values.append(datetime.now().isoformat())
            values.append(contact_id)
            
            query = f"UPDATE contactos SET {', '.join(fields)} WHERE id = ?"
            cursor.execute(query, values)
            conn.commit()
    
    def delete_contact(self, contact_id: int):
        """Delete a contact"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contactos WHERE id = ?', (contact_id,))
        conn.commit()
    
    # Event operations
    def add_event(self, titulo: str, fecha_inicio: str, descripcion: str = "",
                 fecha_fin: str = "", ubicacion: str = "", contacto_id: int = None,
                 recordatorio: int = 0) -> int:
        """Add a new event"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO eventos (titulo, descripcion, fecha_inicio, fecha_fin, 
                               ubicacion, contacto_id, recordatorio)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (titulo, descripcion, fecha_inicio, fecha_fin, ubicacion, contacto_id, recordatorio))
        conn.commit()
        return cursor.lastrowid
    
    def get_events(self, fecha_inicio: str = "", fecha_fin: str = "") -> List[Dict]:
        """Get events, optionally filtered by date range"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if fecha_inicio and fecha_fin:
            cursor.execute('''
                SELECT e.*, c.nombre as contacto_nombre, c.apellido as contacto_apellido
                FROM eventos e
                LEFT JOIN contactos c ON e.contacto_id = c.id
                WHERE e.fecha_inicio BETWEEN ? AND ?
                ORDER BY e.fecha_inicio
            ''', (fecha_inicio, fecha_fin))
        else:
            cursor.execute('''
                SELECT e.*, c.nombre as contacto_nombre, c.apellido as contacto_apellido
                FROM eventos e
                LEFT JOIN contactos c ON e.contacto_id = c.id
                ORDER BY e.fecha_inicio
            ''')
        return [dict(row) for row in cursor.fetchall()]
    
    def mark_event_complete(self, event_id: int, completado: int = 1):
        """Mark event as complete or incomplete"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE eventos SET completado = ? WHERE id = ?', (completado, event_id))
        conn.commit()
    
    def delete_event(self, event_id: int):
        """Delete an event"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM eventos WHERE id = ?', (event_id,))
        conn.commit()
    
    # Task operations
    def add_task(self, titulo: str, descripcion: str = "", prioridad: str = "Media",
                fecha_vencimiento: str = "") -> int:
        """Add a new task"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tareas (titulo, descripcion, prioridad, fecha_vencimiento)
            VALUES (?, ?, ?, ?)
        ''', (titulo, descripcion, prioridad, fecha_vencimiento))
        conn.commit()
        return cursor.lastrowid
    
    def get_tasks(self, completado: Optional[int] = None) -> List[Dict]:
        """Get tasks, optionally filtered by completion status"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if completado is not None:
            cursor.execute('''
                SELECT * FROM tareas WHERE completado = ? 
                ORDER BY 
                    CASE prioridad 
                        WHEN 'Alta' THEN 1 
                        WHEN 'Media' THEN 2 
                        WHEN 'Baja' THEN 3 
                    END,
                    fecha_vencimiento
            ''', (completado,))
        else:
            cursor.execute('''
                SELECT * FROM tareas 
                ORDER BY 
                    completado,
                    CASE prioridad 
                        WHEN 'Alta' THEN 1 
                        WHEN 'Media' THEN 2 
                        WHEN 'Baja' THEN 3 
                    END,
                    fecha_vencimiento
            ''')
        return [dict(row) for row in cursor.fetchall()]
    
    def mark_task_complete(self, task_id: int, completado: int = 1):
        """Mark task as complete or incomplete"""
        conn = self.get_connection()
        cursor = conn.cursor()
        fecha_completado = datetime.now().isoformat() if completado else None
        cursor.execute('''
            UPDATE tareas 
            SET completado = ?, fecha_completado = ? 
            WHERE id = ?
        ''', (completado, fecha_completado, task_id))
        conn.commit()
    
    def delete_task(self, task_id: int):
        """Delete a task"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tareas WHERE id = ?', (task_id,))
        conn.commit()
