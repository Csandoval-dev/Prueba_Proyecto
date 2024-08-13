import tkinter as tk
from tkinter import ttk
from algoritmos import Proceso

# Lista global para almacenar procesos
procesos_configurados = []

def open_process_configuration(parent):
    # Crear una ventana emergente para la configuración de procesos
    config_window = tk.Toplevel(parent)
    config_window.title("Configuración de Procesos")
    config_window.geometry("400x300")

    # Crear campos de entrada para el proceso
    tk.Label(config_window, text="Nombre del Proceso:").pack(pady=5)
    process_name = tk.Entry(config_window)
    process_name.pack(pady=5)

    tk.Label(config_window, text="Tiempo de CPU:").pack(pady=5)
    cpu_time = tk.Entry(config_window)
    cpu_time.pack(pady=5)

    tk.Label(config_window, text="Prioridad:").pack(pady=5)
    priority = tk.Entry(config_window)
    priority.pack(pady=5)

    tk.Label(config_window, text="Orden de Llegada:").pack(pady=5)
    arrival_order = tk.Entry(config_window)
    arrival_order.pack(pady=5)

    tk.Label(config_window, text="Quantum (si aplica):").pack(pady=5)
    quantum = tk.Entry(config_window)
    quantum.pack(pady=5)

    # Botón para agregar proceso
    tk.Button(config_window, text="Agregar Proceso", command=lambda: add_process(
        process_name.get(), cpu_time.get(), priority.get(), arrival_order.get(), quantum.get())).pack(pady=10)

    # Lista de procesos configurados
    process_list = ttk.Treeview(config_window, columns=("Nombre", "CPU", "Prioridad", "Orden", "Quantum"), show='headings')
    process_list.heading("Nombre", text="Nombre")
    process_list.heading("CPU", text="Tiempo CPU")
    process_list.heading("Prioridad", text="Prioridad")
    process_list.heading("Orden", text="Orden Llegada")
    process_list.heading("Quantum", text="Quantum")
    process_list.pack(pady=10, fill=tk.BOTH, expand=True)

    # Función para agregar un proceso a la lista y la lista global
    def add_process(name, cpu, priority, order, quantum):
        try:
            # Validar y convertir los datos de entrada
            cpu = int(cpu)
            priority = int(priority)
            order = int(order)
            quantum = int(quantum) if quantum else 0  # Usar 0 si quantum no se proporciona

            # Agregar proceso a la lista de la interfaz
            process_list.insert("", "end", values=(name, cpu, priority, order, quantum))

            # Almacenar el proceso configurado en la lista global
            proceso = Proceso(name, cpu, order, priority, quantum)
            procesos_configurados.append(proceso)
        except ValueError as e:
            # Mostrar un mensaje de error si los datos no son válidos
            tk.messagebox.showerror("Error", "Todos los campos deben ser numéricos. Verifique sus entradas.")
