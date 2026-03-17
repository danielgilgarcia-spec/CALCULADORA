from PySide6 import QtWidgets
from PySide6.QtCore import Signal

# Se importa la clase generada por el comando pyside6-uic
from ui_calculadora import Ui_Calculadora as form_class


class Pantalla(QtWidgets.QMainWindow, form_class):
    """
    Vista de la calculadora. Implementa el contrato MVP:
      - Señales: btnsuma, btnresta, btnmultiplicacion, btndivision
      - Métodos: entrada() → (float, float), salida(valor), mensaje(titulo, texto)
    """

    btnsuma = Signal()
    btnresta = Signal()
    btnmultiplicacion = Signal()
    btndivision = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._conectar_botones()

    def _conectar_botones(self):
        """Conecta los botones de la UI con las señales del contrato."""
        self.btsuma.clicked.connect(self.btnsuma)
        self.btresta.clicked.connect(self.btnresta)
        self.btmulti.clicked.connect(self.btnmultiplicacion)
        self.btdivi.clicked.connect(self.btndivision)
        self.btsalida.clicked.connect(self.close)

    # --- Métodos del contrato ---

    def entrada(self):
        """
        Lee y devuelve los dos valores introducidos por el usuario.

        Returns
        -------
        tuple[float, float]

        Raises
        ------
        ValueError
            Si alguno de los campos no contiene un número válido.
        """
        try:
            v1 = float(self.entrada1.text())
            v2 = float(self.entrada2.text())
            return v1, v2
        except ValueError:
            raise ValueError("Introduce números válidos en ambos campos.")

    def salida(self, valor):
        """
        Muestra el resultado en la etiqueta de resultado.

        Parameters
        ----------
        valor : int | float
        """
        self.resultado.setText(str(valor))

    def mensaje(self, titulo, texto):
        """
        Muestra un cuadro de diálogo de error.

        Parameters
        ----------
        titulo : str
        texto  : str
        """
        QtWidgets.QMessageBox.critical(self, titulo, texto)

    def opera(self):
        # Método que se llamará al hacer clic en el botón de operar
        pass

    def verifica(self):
        # Método que se llamará al hacer clic en el botón de verificar
        pass

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    pantalla = Pantalla()
    pantalla.show()
    sys.exit(app.exec())