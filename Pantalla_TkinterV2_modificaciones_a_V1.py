import tkinter as tk
import tkinter.messagebox

from Event import Event  # Clase agnóstica de la Sesión 12


class TkView:

    def setup_ui(self):
        # --- SECCIÓN DE ENTRADAS ---
        # Creamos un contenedor para las etiquetas y los campos de texto
        frame_entradas = tk.Frame(self.ventana)
        frame_entradas.pack(side=tk.LEFT)

        tk.Label(frame_entradas, text="Número 1:").pack()
        self.entrada1 = tk.Entry(frame_entradas)
        self.entrada1.pack()

        # --- SECCIÓN DE BOTONES ---
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(side=tk.RIGHT)

        self.btn_suma = tk.Button(frame_botones, text="+", width=5, command=lambda: self.opera('+'))
        self.btn_suma.pack()
