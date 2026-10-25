from personajes import Personaje, Guerrero, Mago, Arquero, Combate

# Validación

def probar_validaciones():
    print("\n=== PRUEBAS DE VALIDACION ===")

    # Creacion correcta de los tres tipos de personajes.
    personajes = [
        Guerrero("Arthas", 100, 30, 20),
        Mago("Gandalf", 80, 40, 10),
        Arquero("Legolas", 90, 35, 15),
    ]

    assert len(personajes) == 3
    assert all(isinstance(p, Personaje) for p in personajes)

    print("[OK] Creacion de personajes.")

    # Nombre vacio
    try:
        Guerrero("   ", 100, 30, 20)
        assert False, "Se acepto un nombre vacio."
    except ValueError:
        print("[OK] Se rechazan los nombres vacios.")

    # Vida fuera del rango permitido.
    for vida in (-1, 101):
        try:
            Guerrero("Prueba", vida, 30, 20)
            assert False, f"Se acepto una vida invalida: {vida}"
        except ValueError:
            pass

    print("[OK] Se rechaza la vida fuera del rango 0-100.")

    # Ataque invalido
    for ataque in (0, -5, 2.5, True):
        try:
            Guerrero("Prueba", 100, ataque, 20)
            assert False, f"Se acepto un ataque invalido: {ataque}"
        except ValueError:
            pass

    print("[OK] Se rechazan los ataques invalidos.")

    # Defensa invalida
    for defensa in (-1, 2.5, True):
        try:
            Guerrero("Prueba", 100, 30, defensa)
            assert False, f"Se acepto una defensa invalida: {defensa}"
        except ValueError:
            pass

    print("[OK] Se rechazan las defensas invalidas.")

    # Modificacion de atributos mediante propiedades
    guerrero = personajes[0]
    guerrero.vida = 75
    guerrero.nombre = "Arthas el Valiente"

    assert guerrero.vida == 75
    assert guerrero.nombre == "Arthas el Valiente"

    try:
        guerrero.vida = 150
        assert False, "Se acepto una vida invalida."
    except ValueError:
        pass

    print("[OK] Getters, setters y encapsulamiento.")

# Habilidades

def probar_habilidades():
    print("\n=== PRUEBAS DE HABILIDADES ===")

    # Guerrero
    guerrero = Guerrero("Arthas", 100, 30, 20)
    objetivo = Mago("Objetivo", 100, 10, 10)

    danio = guerrero.atacar(objetivo)

    assert danio == 26
    assert objetivo.vida == 74

    print("[OK] Guerrero: dano correcto de 26.")

    # Mago
    mago = Mago("Gandalf", 80, 40, 10)
    objetivo = Guerrero("Defensor", 100, 10, 90)

    danio = mago.atacar(objetivo)

    assert danio == 40
    assert objetivo.vida == 60

    print("[OK] Mago: ignora la defensa.")

    # Arquero
    arquero = Arquero("Legolas", 90, 35, 15)
    objetivo = Guerrero("Objetivo", 100, 10, 15)

    danio = arquero.atacar(objetivo)

    assert danio == 40
    assert objetivo.vida == 60

    print("[OK] Arquero: disparo critico de 40.")

    arquero = Arquero("Legolas", 90, 15, 10)
    objetivo = Guerrero("Defensor", 100, 10, 15)

    danio = arquero.atacar(objetivo)

    assert danio == 0
    assert objetivo.vida == 100

    print("[OK] Arquero: no causa dano si no supera la defensa.")

    # La vida nunca queda por debajo de cero
    objetivo = Guerrero("Victima", 5, 10, 0)
    danio_recibido = objetivo.recibir_danio(50)

    assert danio_recibido == 5
    assert objetivo.vida == 0
    assert not objetivo.esta_vivo()

    print("[OK] La vida nunca queda por debajo de cero.")

    # No se permite recibir danio negativo
    try:
        objetivo.recibir_danio(-10)
        assert False, "Se acepto dano negativo."
    except ValueError:
        pass

    print("[OK] Se rechaza el dano negativo.")

    # Un personaje derrotado no puede atacar
    atacante = Guerrero("Derrotado", 0, 30, 10)
    objetivo = Mago("Objetivo", 80, 10, 5)

    danio = atacante.atacar(objetivo)

    assert danio == 0
    assert objetivo.vida == 80

    print("[OK] Un personaje derrotado no puede atacar.")

    # El objetivo derrotado tampoco puede recibir un ataque
    atacante = Mago("Gandalf", 80, 40, 10)
    objetivo = Guerrero("Derrotado", 0, 10, 5)

    assert atacante.atacar(objetivo) == 0
    assert objetivo.vida == 0

    print("[OK] No se ataca a un personaje derrotado.")

    # Un objetivo de tipo incorrecto debe producir una excepcion
    try:
        atacante.atacar("Objetivo invalido")
        assert False, "Se acepto un objetivo incorrecto."
    except TypeError:
        pass

    print("[OK] Se rechazan objetivos invalidos.")

    # No se permite atacarse a si mismo
    try:
        atacante.atacar(atacante)
        assert False, "Se permitio atacar al mismo personaje."
    except ValueError:
        pass

    print("[OK] Un personaje no puede atacarse a si mismo.")

# Combate

def probar_combate():
    print("\n=== PRUEBAS DEL COMBATE ===")

    # Se comprueba la relacion entre Combate y Personaje
    guerrero = Guerrero("Arthas", 100, 30, 20)
    mago = Mago("Gandalf", 80, 40, 10)

    combate = Combate(guerrero, mago)

    assert combate.personaje1 is guerrero
    assert combate.personaje2 is mago

    print("[OK] Combate recibe personajes existentes.")

    # No se aceptan objetos que no sean Personaje
    try:
        Combate(guerrero, "No soy un personaje")
        assert False, "Se acepto un participante invalido."
    except TypeError:
        pass

    print("[OK] Se rechazan participantes invalidos.")

    # Un personaje no puede combatir contra si mismo
    try:
        Combate(guerrero, guerrero)
        assert False, "Se permitio combatir contra si mismo."
    except ValueError:
        pass

    print("[OK] Se rechaza el combate contra uno mismo.")

    # Combate completo con resultado conocido
    # Arthas causa 26 de dano por ataque
    # Gandalf causa hasta 40 de dano por ataque
    ganador = combate.iniciar()

    assert ganador is mago
    assert combate.ganador is mago
    assert combate.empate is False
    assert combate.rondas == 3
    assert guerrero.vida == 0
    assert mago.vida == 2

    print("[OK] Se identifica al ganador correctamente.")
    print("[OK] El combate termina al derrotar a un personaje.")

    # Un combate sin dano debe terminar en empate tecnico
    arquero1 = Arquero("Arquero A", 100, 10, 15)
    arquero2 = Arquero("Arquero B", 100, 10, 15)

    empate = Combate(arquero1, arquero2)
    ganador = empate.iniciar()

    assert ganador is None
    assert empate.empate is True
    assert empate.rondas == 1
    assert arquero1.vida == 100
    assert arquero2.vida == 100

    print("[OK] Se detecta el empate tecnico.")

    # Si un personaje ya esta derrotado al iniciar, el combate identifica al otro como ganador
    derrotado = Guerrero("Derrotado", 0, 10, 5)
    superviviente = Mago("Superviviente", 50, 20, 5)

    combate_inicial = Combate(derrotado, superviviente)
    ganador = combate_inicial.iniciar()

    assert ganador is superviviente
    assert combate_inicial.rondas == 0

    print("[OK] Se detecta un ganador desde el inicio.")


# Ejecución

def main():
    print("=" * 45)
    print("GUARDIANS OF THE ANCIENT KINGDOM")
    print("=" * 45)

    probar_validaciones()
    probar_habilidades()
    probar_combate()

    print("\nTodas las pruebas finalizaron correctamente.")


if __name__ == "__main__":
    main()

