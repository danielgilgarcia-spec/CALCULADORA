class Calculadora:
    """
    Realiza las operaciones matemáticas básicas de la calculadora
    """

    def suma(self, v1, v2):
        """
        Parameters
        ----------
        v1: int | float
        v2: int | float

        Returns
        -------
        int | float

        >>> c = Calculadora()
        >>> c.suma(2, 3)
        5
        """
        return v1 + v2

    def resta(self, v1, v2):
        """
        Parameters
        ----------
        v1: int | float
        v2: int | float

        Returns
        -------
        int | float

        >>> c = Calculadora()
        >>> c.resta(5, 3)
        2
        """
        return v1 - v2

    def mult(self, v1, v2):
        """
        Parameters
        ----------
        v1: int | float
        v2: int | float

        Returns
        -------
        int | float

        >>> c = Calculadora()
        >>> c.mult(4, 3)
        12
        """
        return v1 * v2

    def div(self, v1, v2):
        """
        Parameters
        ----------
        v1: int | float
            Dividendo
        v2: int | float
            Divisor. Debe ser != 0.

        Returns
        -------
        int | float

        >>> c = Calculadora()
        >>> c.div(6, 3)
        2
        >>> c.div(6, 3.0)
        2.0
        >>> c.div(5, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> c.div(5, 0.0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: float division by zero
        """
        # Gestiona el error de denominador cero mediante excepciones
        try:
            if type(v1) == float or type(v2) == float:
                return v1 / v2
            return v1 // v2
        except ZeroDivisionError as err:
            raise err


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
