from Event import Event # Importamos la nueva clase agnóstica

class MockView:
    """
    Objeto simulado (Mock) que sustituye a la PantallaCalculadora real.
    No hereda de QMainWindow ni usa PySide6.
    """
    def __init__(self):
        # Usamos la clase Event en lugar de pyqtSignal
        self.btnsuma = Event()
        self.btnresta = Event()
        self.btnmult = Event()
        self.btndiv = Event()


    def entrada(self):
        """Simula que el usuario ha introducido los valores 10 y 5."""
        print("MOCK: El Presenter solicita datos de entrada...")
        return 10.0, 5.0

    def salida(self, valor):
        """Simula la recepción del resultado desde el Presenter."""
        print(f"MOCK: La vista ha recibido el resultado para mostrar: {valor}")

    def mensaje(self, titulo, texto):
        """Simula la visualización de un error."""
        print(f"MOCK ERROR: [{titulo}] -> {texto}")