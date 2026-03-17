class Presenter:
    """Actúa como puente entre la lógica y la interfaz."""

    def __init__(self, view, model):
        # Agregación: recibe instancias externas
        self.vista = view
        self.modelo = model

        # Suscripción a las señales de la vista
        self.vista.btnsuma.connect(self.fsuma)
        self.vista.btnresta.connect(self.fresta)
        self.vista.btnmultiplicacion.connect(self.fmult)
        self.vista.btndivision.connect(self.fdiv)

    def fsuma(self):
        """Flujo de la operación suma."""
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.suma(v1, v2)
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))

    def fresta(self):
        """Flujo de la operación resta."""
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.resta(v1, v2)
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))

    def fmult(self):
        """Flujo de la operación multiplicación."""
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.mult(v1, v2)   
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))

    def fdiv(self):
        """Flujo de la operación división."""
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.divi(v1, v2)   
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))