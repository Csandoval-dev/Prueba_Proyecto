class Proceso:
    def __init__(self, nombre, tiempo_cpu, llegada, prioridad=0, quantum=0):
        # Constructor de la clase Proceso, inicializa los atributos del proceso
        self.nombre = nombre  # Nombre del proceso
        self.tiempo_cpu = tiempo_cpu  # Tiempo total de CPU requerido
        self.llegada = llegada  # Tiempo de llegada del proceso
        self.prioridad = prioridad  # Prioridad del proceso, valor opcional
        self.quantum = quantum  # Quantum asignado al proceso, valor opcional
        self.tiempo_restante = tiempo_cpu  # Tiempo de CPU restante para completar el proceso
        self.completado = False  # Estado del proceso, False indica que no está completado

class RoundRobin:
    def __init__(self, quantum):
        # Constructor de la clase RoundRobin, inicializa el quantum
        self.quantum = quantum  # Quantum asignado para cada proceso en el algoritmo Round Robin
    
    def planificar(self, procesos):
        # Método para planificar los procesos según el algoritmo Round Robin
        tiempo = 0  # Variable para llevar la cuenta del tiempo transcurrido
        cola = procesos.copy()  # Se crea una copia de la lista de procesos para trabajar
        procesos_finalizados = []  # Lista para almacenar los procesos completados

        while cola:  # Mientras haya procesos en la cola
            proceso = cola.pop(0)  # Se obtiene el primer proceso de la cola
            if proceso.tiempo_restante > self.quantum:
                # Si el tiempo restante del proceso es mayor que el quantum
                proceso.tiempo_restante -= self.quantum  # Se reduce el tiempo restante en el valor del quantum
                tiempo += self.quantum  # Se incrementa el tiempo total transcurrido
                cola.append(proceso)  # El proceso se vuelve a añadir al final de la cola
            else:
                # Si el tiempo restante del proceso es menor o igual al quantum
                tiempo += proceso.tiempo_restante  # Se añade el tiempo restante al tiempo total transcurrido
                proceso.tiempo_restante = 0  # El tiempo restante se establece en 0
                proceso.completado = True  # Se marca el proceso como completado
                procesos_finalizados.append(proceso)  # El proceso se añade a la lista de procesos completados
        
        # Añadir los procesos completados al final de la lista para mantener el orden
        cola.extend(procesos_finalizados)
        
        return cola  # Se devuelve la lista de procesos con su estado actualizado
