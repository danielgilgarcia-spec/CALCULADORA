@import sys
from PySide6 import QtWidgets
# Importamos tu clase Vista y el Modelo (aunque el Mock no use el modelo real)
from PantallaCalculadora import Pantalla


class MockPresenter:
    """
    Objeto simulado que sustituye al Presenter real.
    Su función es verificar que la Vista emite las señales del contrato [5], [3].
    """

    def __init__(self, view):
        self.view = view
        # Nos conectamos a la señal de la vista según el contrato [6]
        self.view.btnsuma.connect(self.al_recibir_suma)
        print("MOCK: Presenter conectado a la señal 'btnsuma' de la Vista.")

    def al_recibir_suma(self):
        """Este método se ejecuta cuando la Vista emite la señal btnsuma"""
        print("\n[OK] MOCK: El Presenter ha recibido la señal de SUMA desde la interfaz.")

        # Para probar el flujo completo, el Mock puede "ordenar" a la vista
        # que muestre un valor ficticio [7]
        print("MOCK: Ordenando a la vista mostrar el resultado de prueba '99.999'...")
        self.view.salida(99.999)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Instanciamos la vista real que el estudiante B ha diseñado
    vista = Pantalla()

    # Instanciamos el Mock en lugar del Presenter real
    tester = MockPresenter(vista)

    vista.show()
    print("Iniciando prueba de interfaz... Pulsa el botón '+' en la calculadora.")
    sys.exit(app.exec())