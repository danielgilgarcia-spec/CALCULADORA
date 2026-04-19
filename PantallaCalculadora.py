import sys
from PySide6 import QtWidgets
from Event import Event
from ui_calculadora import Ui_Calculadora as form_class


class Pantalla(QtWidgets.QMainWindow, form_class):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # ❌ tenías self.setupUi(self) dos veces, solo una

        # Eventos patrón Observer (igual que TkView)
        self.btnsuma = Event()
        self.btnresta = Event()
        self.btnmult = Event()
        self.btndiv = Event()

        # Conectar botones de la UI a opera()
        self.btsuma.clicked.connect(lambda: self.opera('+'))
        self.btresta.clicked.connect(lambda: self.opera('-'))
        self.btmulti.clicked.connect(lambda: self.opera('*'))
        self.btdivi.clicked.connect(lambda: self.opera('/'))
        self.btsalida.clicked.connect(self.close)

    def entrada(self):
        try:
            return float(self.entrada1.text()), float(self.entrada2.text())
        except ValueError:
            raise ValueError("Introduce números válidos en ambos campos.")

    def salida(self, valor):
        self.resultado.setText(f"{valor:.3f}")

    def mensaje(self, titulo, texto):
        QtWidgets.QMessageBox.critical(self, titulo, texto)

    def opera(self, op):
        if not self.verifica():
            return
        if op == '+':
            self.btnsuma.emit()
        if op == '-':
            self.btnresta.emit()
        if op == '*':
            self.btnmult.emit()
        if op == '/':
            self.btndiv.emit()

    def verifica(self):
        val1 = self.entrada1.text()
        val2 = self.entrada2.text()
        if not val1 or not val2:
            self.mensaje('Error', 'Ambos campos deben ser llenados.')
            return False
        try:
            float(val1)
            float(val2)
        except ValueError:
            self.mensaje('Error', 'Ambos campos deben ser numéricos.')
            return False
        return True


if __name__ == "__main__":
    from presenter import Presenter
    from Calculadora import Calculadora as Model

    app = QtWidgets.QApplication(sys.argv)
    modelo = Model()
    vista = Pantalla()
    presentador = Presenter(vista, modelo)
    vista.show()
    sys.exit(app.exec())