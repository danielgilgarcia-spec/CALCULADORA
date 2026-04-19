from PySide6.QtCore import QObject, Signal
from presenter import Presenter
from MockView import MockView
from Calculadora import Calculadora


if __name__ == "__main__":
    print("Iniciando prueba de Mocking del Presenter...")

    vista_falsa = MockView()
    modelo_real = Calculadora()

    p = Presenter(vista_falsa, modelo_real)

    print("Simulando click en botón suma...")
    vista_falsa.btnsuma.emit()