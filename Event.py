class Event:

    def __init__(self):
        self.suscriptores = []

    def add_listener(self, funcion_a_conectar):
        self.suscriptores.append(funcion_a_conectar)

    def connect(self, funcion_a_conectar):  # <-- añade esto
        self.add_listener(funcion_a_conectar)

    def emit(self):
        for funcion in self.suscriptores:
            funcion()