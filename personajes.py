from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    # Nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")

        self.__nombre = valor.strip()

    # Vida

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if type(valor) is not int or not 0 <= valor <= 100:
            raise ValueError(
                "La vida debe ser un entero entre 0 y 100."
            )

        self.__vida = valor

    # Ataque

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, valor):
        if type(valor) is not int or valor <= 0:
            raise ValueError(
                "El ataque debe ser un entero positivo."
            )

        self.__ataque = valor

    # Defensa

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self, valor):
        if type(valor) is not int or valor < 0:
            raise ValueError(
                "La defensa debe ser un entero no negativo."
            )

        self.__defensa = valor

    # Métodos comunes

    def recibir_danio(self, cantidad):
        if type(cantidad) is not int or cantidad < 0:
            raise ValueError(
                "El daño debe ser un entero no negativo."
            )

        danio_real = min(self.vida, cantidad)
        self.vida -= danio_real

        return danio_real

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_estado(self):
        estado = "Vivo" if self.esta_vivo() else "Derrotado"

        print(f"--- Estado de {self.nombre} ---")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Estado: {estado}")

    def _puede_atacar(self, objetivo):
        if not isinstance(objetivo, Personaje):
            raise TypeError(
                "El objetivo debe ser un objeto Personaje."
            )

        if objetivo is self:
            raise ValueError(
                "Un personaje no puede atacarse a sí mismo."
            )

        return self.esta_vivo() and objetivo.esta_vivo()

    @abstractmethod
    def atacar(self, objetivo):
        """Calcula y aplica el daño según la clase del personaje."""
        pass

class Guerrero(Personaje):
    def atacar(self, objetivo):
        if not self._puede_atacar(objetivo):
            return 0

        danio = max(
            0,
            int(self.ataque * 1.20 - objetivo.defensa)
        )

        return objetivo.recibir_danio(danio)

class Mago(Personaje):
    def atacar(self, objetivo):
        if not self._puede_atacar(objetivo):
            return 0

        danio = self.ataque

        return objetivo.recibir_danio(danio)

class Arquero(Personaje):
    def atacar(self, objetivo):
        if not self._puede_atacar(objetivo):
            return 0

        if self.ataque > objetivo.defensa:
            danio = (self.ataque - objetivo.defensa) * 2
        else:
            danio = 0

        return objetivo.recibir_danio(danio)

class Combate:
    MAX_RONDAS = 50

    def __init__(self, personaje1, personaje2):
        if not isinstance(personaje1, Personaje):
            raise TypeError(
                "El primer participante debe ser un Personaje."
            )

        if not isinstance(personaje2, Personaje):
            raise TypeError(
                "El segundo participante debe ser un Personaje."
            )

        if personaje1 is personaje2:
            raise ValueError(
                "Un personaje no puede combatir contra sí mismo."
            )

        self.personaje1 = personaje1
        self.personaje2 = personaje2
        self.turno_actual = personaje1
        self.ganador = None
        self.empate = False
        self.rondas = 0
        self.__finalizado = False

    def iniciar(self):
        if self.__finalizado:
            return self.ganador

        self.turno_actual = self.personaje1

        if self.verificar_ganador():
            self.__finalizado = True
            self.mostrar_resultado()
            return self.ganador

        for ronda in range(1, self.MAX_RONDAS + 1):
            self.rondas = ronda
            danio_en_ronda = 0

            for _ in range(2):
                atacante = self.turno_actual

                objetivo = (
                    self.personaje2
                    if atacante is self.personaje1
                    else self.personaje1
                )

                if atacante.esta_vivo() and objetivo.esta_vivo():
                    danio = atacante.atacar(objetivo)
                    danio_en_ronda += danio

                    print(
                        f"Ronda {ronda}: {atacante.nombre} "
                        f"causa {danio} de daño a {objetivo.nombre}."
                    )

                    self.personaje1.mostrar_estado()
                    self.personaje2.mostrar_estado()

                if self.verificar_ganador():
                    self.__finalizado = True
                    self.mostrar_resultado()
                    return self.ganador

                self.cambiar_turno()

            if danio_en_ronda == 0:
                self.empate = True
                self.__finalizado = True

                self.mostrar_resultado(
                    "Empate técnico: ambos personajes "
                    "completaron la ronda sin causar daño."
                )

                return None

        self.empate = True
        self.__finalizado = True

        self.mostrar_resultado(
            f"Empate: se completaron {self.MAX_RONDAS} "
            "rondas sin un ganador."
        )

        return None

    def cambiar_turno(self):
        self.turno_actual = (
            self.personaje2
            if self.turno_actual is self.personaje1
            else self.personaje1
        )

        return self.turno_actual

    def verificar_ganador(self):
        vivo1 = self.personaje1.esta_vivo()
        vivo2 = self.personaje2.esta_vivo()

        if not vivo1 and not vivo2:
            self.ganador = None
            self.empate = True

        elif not vivo1:
            self.ganador = self.personaje2
            self.empate = False

        elif not vivo2:
            self.ganador = self.personaje1
            self.empate = False

        else:
            self.ganador = None
            return False

        return True

    def mostrar_resultado(self, mensaje=None):
        if mensaje is not None:
            print(mensaje)

        elif self.ganador is not None:
            print(f"Ganador: {self.ganador.nombre}")

        elif self.empate:
            print("El combate terminó en empate.")

        else:
            print("El combate todavía no tiene un resultado.")
