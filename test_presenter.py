from PySide6.QtCore import QObject, Signal
from presenter import Presenter

from CALCULADORA import Calculadora

# Objeto simulado (Mock) que cumple el contrato de la Vista [14]
class MockView(QObject):
    btnsuma = Signal()  # Solo suma soportada para el esqueleto
    btnresta = Signal()
    btnmultiplicacion = Signal()
    btndivision = Signal()

    def entrada(self):
        print("MOCK: Presenter solicita entradas. Enviando (10, 5)...")
        return 10.0, 5.0

    def salida(self, valor):
        print(f"MOCK: La vista recibió el resultado: {valor}")

    def mensaje(self, titulo, texto):
        print(f"MOCK ERROR: {titulo}: {texto}")




if __name__ == "__main__":
    print("Iniciando prueba de Mocking del Presenter...")

    # Instanciamos los componentes (Vista simulada y Modelo real)
    vista_falsa = MockView()
    modelo_real = Calculadora()

    # El Presenter cree que está hablando con la ventana real
    p = Presenter(vista_falsa, modelo_real)

    # Simulamos que el usuario pulsó el botón de suma en la GUI
    print("Simulando click en botón suma...")
    vista_falsa.btnsuma.emit()