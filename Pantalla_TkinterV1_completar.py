import tkinter as tk
import tkinter.messagebox

from Event import Event  # Aplicación del patrón Observer


class TkView:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        # Eventos: patrón Observer
        self.btnsuma = Event()
        # TODO: Añadir eventos para resta, multiplicación y división

        self.setup_ui()

    def setup_ui(self):
        # --- INTERFAZ MUY MUY SIMPLE ---
        # TODO: completar todo lo necesario
        tk.Label(self.ventana, text="Número 1:").pack()
        self.entrada1 = tk.Entry(self.ventana)
        # .pack apila una cosa sobre la otra
        self.entrada1.pack()

        self.lbl_resultado = tk.Label(self.ventana, text="0.000")
        self.lbl_resultado.pack()

        # Cambio: Los botones llaman a 'opera' con la operación como parámetro
        # lambda: funciones anónimas
        self.btn_suma = tk.Button(self.ventana, text="+", command=lambda: self.opera('+'))
        self.btn_suma.pack()

        self.btn_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.quit, bg="red", fg="white")
        self.btn_salir.pack()

    def entrada(self):
        """Retorna (float, float) según el contrato"""
        # para obtener el contenido de un campo usamos .get() en lugar de .text()
        return float(self.entrada1.get()), float(self.entrada2.get())

    def salida(self, valor):
        """Muestra el resultado"""
        # cambiamos el label con config
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
        # TODO: completar
        pass


    def verifica(self):
        """Verifica que los campos de entrada de Tkinter sean válidos."""
        # TODO: completar
        pass

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

    # 4. Instanciar el Presenter
    # (No se debe modificar respecto, es independiente tras aplicar el patrón Observer)
    # El Presenter se conectará a los Event() de TkView automáticamente
    presentador = Presenter(vista, modelo)

    # 5. Iniciar el bucle de eventos de la interfaz
    ventana.mainloop()
