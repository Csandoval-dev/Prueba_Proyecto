import tkinter as tk
from tkinter import ttk

class ListaEjecucion:
    def __init__(self, parent):
        # Constructor de la clase ListaEjecucion
        # Inicializa una lista vacía para almacenar los procesos y guarda una referencia al objeto padre (ventana o aplicación)

        self.lista = []  # Lista que contendrá los procesos en ejecución
        self.parent = parent  # Referencia al objeto padre (puede ser la ventana principal o una subventana)

    def add_proceso(self, proceso):
        # Método para agregar un proceso a la lista de ejecución

        self.lista.append(proceso)  # Añade el proceso pasado como argumento a la lista

    def remove_proceso(self, nombre):
        # Método para eliminar un proceso de la lista de ejecución basado en su nombre

        # Crea una nueva lista que excluye el proceso cuyo nombre coincide con el pasado como argumento
        self.lista = [p for p in self.lista if p.nombre != nombre]

    def get_lista(self):
        # Método para obtener la lista completa de procesos en ejecución

        return self.lista  # Retorna la lista de procesos
