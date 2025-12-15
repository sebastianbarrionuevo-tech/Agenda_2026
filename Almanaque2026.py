'''
    Nombre: Calendario2026.py
    Autor: Sebastián Barrionuevo
    Fecha: 2025-12-15
    Descripción: Este script genera y muestra el calendario completo del año 2026. Dividido por meses, cada mes se presenta con su respectivo nombre y los días correctamente alineados según el día de la semana en que comienzan.
    Los fines de Semana (sábados y domingos) están resaltados para facilitar su identificación(con colorama). Tambien necesito que marque en rojo los feriados nacionales de Argentina en 2026.
    Dependencias: Utiliza el módulo 'calendar' de Python para generar el calendario.    
'''
## Importar módulos necesarios
import calendar
from colorama import Fore, Style, init
init(autoreset=True)

# Definir los feriados nacionales de Argentina en 2026
feriados_argentina_2026 = [ (1, 1),   # Año Nuevo
                            (2, 23),  # Carnaval
                            (2, 24),  # Carnaval
                            (3, 24),  # Día de la Memoria por la Verdad y la Justicia
                            (4, 2),   # Día del Veterano y de los Caídos en la Guerra de Malvinas
                            (4, 9),   # Jueves Santo
                            (4, 10),  # Viernes Santo
                            (5, 1),   # Día del Trabajador
                            (5, 25),  # Día de la Revolución de Mayo
                            (6, 20),  # Día de la Bandera
                            (7, 9),   # Día de la Independencia
                            (8, 17),  # Paso a la Inmortalidad del General José de San Martín
                            (10, 12), # Día del Respeto a la Diversidad Cultural
                            (11, 2),  # Día de los Fieles Difuntos
                            (12, 8),  # Inmaculada Concepción de María
                            (12, 25)] # Navidad

# Función para verificar si un día es feriado
def es_feriado(mes, dia):
    return (mes, dia) in feriados_argentina_2026

# Función para imprimir el calendario del año 2026
def imprimir_calendario_2026():
    año = 2026
    meses = [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" ]
    
    for mes in range(1, 13):
        print(f"\n{meses[mes-1]} {año}")
        print("Lu Ma Mi Ju Vi Sá Do")
        
        # Obtener el calendario del mes
        cal = calendar.monthcalendar(año, mes)
        
        for semana in cal:
            for dia in semana:
                if dia == 0:
                    # Día vacío
                    print("   ", end="")
                else:
                    if es_feriado(mes, dia):
                        # Día feriado en rojo
                        print(Fore.RED + f"{dia:2d} " + Style.RESET_ALL, end="")
                    elif semana.index(dia) >= 5:
                        # Fin de semana en azul
                        print(Fore.BLUE + f"{dia:2d} " + Style.RESET_ALL, end="")
                    else:
                        # Día normal
                        print(f"{dia:2d} ", end="")
            print()  
            
            # Nueva línea al final de la semana

        print()  # Nueva línea al final del mes

# Ejecutar la función para imprimir el calendario
imprimir_calendario_2026()
