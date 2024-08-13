import tkinter as tk
from tkinter import ttk
from algoritmos import RoundRobin, Proceso

# Variable global para almacenar los procesos y la configuración
procesos_configurados = []  # Lista que almacenará los procesos configurados
configuracion = {"quantum": 4}  # Configuración por defecto para el quantum

def open_task_emulation(parent):
    # Función que abre la ventana de emulación del administrador de tareas
    emulation_window = tk.Toplevel(parent)
    emulation_window.title("Emulación del Administrador de Tareas")
    emulation_window.geometry("800x600")

    # Configuración para que la ventana sea responsive
    emulation_window.grid_rowconfigure(0, weight=1)
    emulation_window.grid_columnconfigure(0, weight=1)

    # Frame para la selección de algoritmo y botones
    control_frame = tk.Frame(emulation_window)
    control_frame.grid(row=0, column=0, sticky="ew")
    control_frame.grid_columnconfigure(1, weight=1)

    # Etiqueta y menú desplegable para seleccionar el algoritmo
    tk.Label(control_frame, text="Selecciona el Algoritmo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    algorithm_var = tk.StringVar(value="Round Robin")
    algorithm_menu = ttk.Combobox(control_frame, textvariable=algorithm_var, values=[
        "Round Robin", "Prioridad", "Tiempo de CPU", "Orden de Llegada", 
        "Múltiples Colas", "Planificación Garantizada", "Planificación de Sorteo", 
        "Partes Equitativas"
    ])
    algorithm_menu.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Tabla para mostrar los procesos en ejecución
    execution_list = ttk.Treeview(emulation_window, columns=("Nombre", "Estado", "CPU Restante", "Prioridad"), show='headings')
    execution_list.heading("Nombre", text="Nombre")
    execution_list.heading("Estado", text="Estado")
    execution_list.heading("CPU Restante", text="CPU Restante")
    execution_list.heading("Prioridad", text="Prioridad")
    execution_list.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    # Configuración para que la tabla de procesos sea expansible
    emulation_window.grid_rowconfigure(1, weight=1)
    emulation_window.grid_columnconfigure(0, weight=1)

    # Frame para los botones de control
    button_frame = tk.Frame(emulation_window)
    button_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)

    # Botones de control: Iniciar, Pausar/Resumir, Matar proceso
    tk.Button(button_frame, text="Iniciar Ejecución", command=lambda: start_execution(algorithm_var.get(), execution_list)).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(button_frame, text="Pausar/Resumir", command=pause_resume_process).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    tk.Button(button_frame, text="Matar Proceso", command=kill_process).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

def start_execution(algorithm_name, execution_list):
    # Función para iniciar la ejecución del algoritmo seleccionado
    global procesos_configurados
    quantum = configuracion.get("quantum", 4)  # Obtener el valor del quantum desde la configuración
    
    if algorithm_name == "Round Robin":
        algoritmo = RoundRobin(quantum)
        procesos = algoritmo.planificar(procesos_configurados)
    else:
        # Placeholder para implementar otros algoritmos de planificación
        procesos = procesos_configurados

    # Actualizar la tabla con el estado de los procesos
    execution_list.delete(*execution_list.get_children())  # Eliminar filas actuales en la tabla
    for proceso in procesos:
        estado = "Completado" if proceso.completado else "En Ejecución"
        execution_list.insert("", "end", values=(proceso.nombre, estado, proceso.tiempo_restante, proceso.prioridad))

def pause_resume_process():
    # Función placeholder para pausar o resumir un proceso
    pass

def kill_process():
    # Función placeholder para matar un proceso
    pass
