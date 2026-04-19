import tkinter as tk
import tkinter.messagebox

from Event import Event  # Aplicación del patrón Observer


class TkView:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        # Eventos: patrón Observer
        self.btnsuma = Event()
        self.btnresta = Event()
        self.btnmult = Event()
        self.btndiv = Event()
        self.setup_ui()

    def setup_ui(self):
        # --- INTERFAZ MUY MUY SIMPLE ---
        tk.Label(self.ventana, text="Número 1:").grid(row=0, column=0)
        self.entrada1 = tk.Entry(self.ventana)
        self.entrada1.grid(row=0, column=1)
        tk.Label(self.ventana, text="Número 2:").grid(row=1, column=0)
        self.entrada2 = tk.Entry(self.ventana)
        self.entrada2.grid(row=1, column=1)

        # TODO: completar los elementos situándolos a vuestro gusto

    def entrada(self):
        """Retorna (float, float) según el contrato"""
        # para obtener el contenido de un campo usamos .get() en lugar de .text()
        return float(self.entrada1.get()), float(self.entrada2.get())

    def salida(self, valor):
        """Muestra el resultado"""
        self.lbl_resultado.config(text=f"{valor:0.3f}")

    def mensaje(self, prompt, txt):
        """Muestra error con messagebox"""
        tk.messagebox.showerror(prompt, txt)

    def opera(self, op):
        """

        Parameters
        ----------
        op: str
            Operación a realizar: '+', '-', '*', '/'

        """
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
        """Verifica que los campos de entrada de Tkinter sean válidos."""
        # En Tkinter usamos .get() en lugar de .text()
        val1 = self.entrada1.get()
        val2 = self.entrada2.get()

        # Validación de campos vacíos
        if not val1 or not val2:
            self.mensaje('Error', 'Ambos campos de entrada deben ser llenados.')
            return False

        # Validación de formato numérico
        if not val1.isnumeric() or not val2.isnumeric():
            self.mensaje('Error', 'Ambos campos de entrada deben ser numéricos.')
            return False

        return True


if __name__ == "__main__":
    from presenter import Presenter
    from Calculadora import Calculadora as Model

    # 1. Crear la ventana raíz de Tkinter
    ventana = tk.Tk()

    # 2. Instanciar el Modelo (Lógica pura e independiente de la UI)
    # Asegúrate de que el nombre coincida con tu clase (Model o Calculadora)
    modelo = Model()

    # 3. Instanciar nuestra nueva Vista de Tkinter (TkView)
    vista = TkView(ventana)

    # 4. Instanciar el Presenter agnóstico
    # (No se debe modificar respecto a la Sesión 12)
    # El Presenter se conectará a los Event() de TkView automáticamente
    presentador = Presenter(vista, modelo)

    # 5. Iniciar el bucle de eventos de la interfaz
    ventana.mainloop()
