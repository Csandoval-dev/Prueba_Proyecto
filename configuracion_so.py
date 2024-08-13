import tkinter as tk
from tkinter import messagebox, ttk

# Variable global para almacenar la configuración del sistema operativo
configuracion_so = {}

def open_system_configuration(parent):
    # Función para abrir una nueva ventana de configuración del sistema operativo

    config_window = tk.Toplevel(parent)  # Crear una nueva ventana secundaria
    config_window.title("Configuración del SO")  # Título de la ventana
    config_window.geometry("400x200")  # Dimensiones de la ventana

    # Etiqueta y campo de entrada para la memoria virtual
    tk.Label(config_window, text="Memoria Virtual (MB):").pack(pady=5)
    memory = tk.Entry(config_window)  # Campo de entrada para la memoria
    memory.pack(pady=5)

    # Etiqueta y campo de entrada para el espacio en disco duro
    tk.Label(config_window, text="Espacio en Disco Duro (GB):").pack(pady=5)
    disk_space = tk.Entry(config_window)  # Campo de entrada para el espacio en disco
    disk_space.pack(pady=5)

    # Etiqueta y menú desplegable para seleccionar el método de ejecución
    tk.Label(config_window, text="Método de Ejecución:").pack(pady=5)
    method = ttk.Combobox(config_window, values=[
        "Prioridad", 
        "Tiempo de CPU", 
        "Orden de Llegada", 
        "Múltiples Colas", 
        "Round Robin", 
        "Planificación Garantizada", 
        "Planificación de Sorteo", 
        "Partes Equitativas"
    ])  # Menú desplegable con diferentes métodos de ejecución
    method.pack(pady=5)

    # Botón para guardar la configuración del sistema operativo
    tk.Button(config_window, text="Guardar Configuración", command=lambda: save_system_configuration(
        memory.get(), disk_space.get(), method.get())).pack(pady=10)

def save_system_configuration(memory, disk_space, method):
    # Función para guardar la configuración del sistema operativo

    global configuracion_so  # Utilizar la variable global para almacenar la configuración

    # Validar que todos los campos estén completos
    if not memory or not disk_space or not method:
        messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
        return

    # Actualizar la variable global con los valores introducidos por el usuario
    configuracion_so = {
        "memoria": memory,
        "disco": disk_space,
        "metodo": method
    }

    # Mostrar un mensaje de confirmación al usuario
    messagebox.showinfo("Configuración SO", f"Configuración Guardada:\nMemoria: {memory} MB\nDisco: {disk_space} GB\nMétodo: {method}")

    # Debugging: Imprimir la configuración guardada en la consola
    print("Configuración guardada:", configuracion_so)
