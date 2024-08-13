import tkinter as tk
from tkinter import ttk
from configuracion_so import open_system_configuration
from Procesos import open_process_configuration
from Emulacion import open_task_emulation

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Manejador de Procesos - Administrador de Tareas")
        self.geometry("800x600")

        # Crear el menú principal
        self.create_main_menu()

    def create_main_menu(self):
        # Crear una barra de menú
        menu_bar = tk.Menu(self)
        
        # Menú "Procesos"
        process_menu = tk.Menu(menu_bar, tearoff=0)
        process_menu.add_command(label="Configuración de Procesos", command=self.open_process_configuration)
        process_menu.add_command(label="Lista de Ejecución", command=self.open_task_emulation)  # Agregado
        menu_bar.add_cascade(label="Procesos", menu=process_menu)

        # Menú "Configuración SO"
        config_menu = tk.Menu(menu_bar, tearoff=0)
        config_menu.add_command(label="Configuración del SO", command=self.open_system_configuration)
        menu_bar.add_cascade(label="Configuración SO", menu=config_menu)

        # Menú "Emulación"
        emulation_menu = tk.Menu(menu_bar, tearoff=0)
        emulation_menu.add_command(label="Emulación del Administrador de Tareas", command=self.open_task_emulation)
        menu_bar.add_cascade(label="Emulación", menu=emulation_menu)

        # Opción para salir de la aplicación
        menu_bar.add_command(label="Salir", command=self.quit)

        # Configurar la barra de menú en la ventana principal
        self.config(menu=menu_bar)

    # Métodos para abrir las ventanas específicas
    def open_process_configuration(self):
        open_process_configuration(self)

    def open_system_configuration(self):
        open_system_configuration(self)

    def open_task_emulation(self):
        open_task_emulation(self)

# Crear una instancia de la aplicación y ejecutar el bucle principal de Tkinter
if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()
