import pprint
import soko

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

def verificar_estado(desc, grilla):
    x = None
    y = None
    try:
        w, h = soko.dimensiones(grilla)
        assert (w, h) == (len(desc[0]), len(desc))
        for y in range(h):
            for x in range(w):
                c = desc[y][x]
                if c == '#':
                    assert soko.hay_pared(grilla, x, y)
                    assert not soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
                elif c == '.':
                    assert not soko.hay_pared(grilla, x, y)
                    assert soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
                elif c == '$':
                    assert not soko.hay_pared(grilla, x, y)
                    assert not soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert soko.hay_caja(grilla, x, y)
                elif c == '@':
                    assert not soko.hay_pared(grilla, x, y)
                    assert not soko.hay_objetivo(grilla, x, y)
                    assert soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
                elif c == '*':
                    assert not soko.hay_pared(grilla, x, y)
                    assert soko.hay_objetivo(grilla, x, y)
                    assert not soko.hay_jugador(grilla, x, y)
                    assert soko.hay_caja(grilla, x, y)
                elif c == '+':
                    assert not soko.hay_pared(grilla, x, y)
                    assert soko.hay_objetivo(grilla, x, y)
                    assert soko.hay_jugador(grilla, x, y)
                    assert not soko.hay_caja(grilla, x, y)
    except AssertionError as e:
        print('Estado esperado:')
        print('\n'.join(desc))
        print()
        print('Estado actual:')
        pprint.pprint(grilla)
        print()
        if x is not None and y is not None:
            print(f'Error en columna = {x}, fila = {y}:')
            print()
        raise

def test1():
    desc = [
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

def test2():
    desc = [
        '#####',
        '#+$ #',
        '#   #',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

def test3():
    desc = [
        '#####',
        '# * #',
        '#@  #',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert soko.juego_ganado(grilla)

def test4():
    desc = [
        '#####',
        '# *.#',
        '#@ $#',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

def test5():
    desc = [
        '#####',
        '# * #',
        '#@ *#',
        '#####',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert soko.juego_ganado(grilla)

def test6():
    desc1 = [
        '######',
        '#@ $.#',
        '######',
    ]
    desc2 = [
        '######',
        '# @$.#',
        '######',
    ]

    grilla1 = soko.crear_grilla(desc1)
    grilla2 = soko.mover(grilla1, ESTE)

    # Si el movimiento es vÃ¡lido, la funciÃ³n mover() debe devolver una grilla nueva
    # y NO modificar la grilla recibida.
    verificar_estado(desc1, grilla1)
    verificar_estado(desc2, grilla2)

def test7():
    desc = [
        '    ###   ',
        '    #.#   ',
        '    #$#   ',
        '   ##$####',
        '####@ $$.#',
        '#.$$  ####',
        '####$##   ',
        '   #$#    ',
        '   #.#    ',
        '   ###    ',
    ]
    grilla = soko.crear_grilla(desc)

    assert soko.mover(grilla, OESTE) == grilla
    assert soko.mover(grilla, NORTE) == grilla

    grilla = soko.mover(grilla, ESTE)

    assert soko.mover(grilla, ESTE) == grilla
    assert soko.mover(grilla, NORTE) == grilla

    grilla = soko.mover(grilla, SUR)

    assert soko.mover(grilla, ESTE) == grilla
    assert soko.mover(grilla, SUR) == grilla

    grilla = soko.mover(grilla, OESTE)

    assert soko.mover(grilla, OESTE) == grilla
    assert soko.mover(grilla, SUR) == grilla

def test8():
    desc = [
        '########',
        '#@ $ . #',
        '########',
    ]
    grilla = soko.crear_grilla(desc)
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

    for direction in (OESTE, NORTE, SUR):
        grilla = soko.mover(grilla, direction)
        verificar_estado(desc, grilla)
        assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, ESTE)
    desc = [
        '########',
        '# @$ . #',
        '########',
    ]
    verificar_estado(desc, grilla)
    assert not soko.juego_ganado(grilla)

    for direction in (NORTE, SUR):
        grilla = soko.mover(grilla, direction)
        verificar_estado(desc, grilla)
        assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, ESTE)
    verificar_estado([
        '########',
        '#  @$. #',
        '########',
    ], grilla)
    assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, OESTE)
    verificar_estado([
        '########',
        '# @ $. #',
        '########',
    ], grilla)
    assert not soko.juego_ganado(grilla)

    grilla = soko.mover(grilla, ESTE)
    grilla = soko.mover(grilla, ESTE)
    verificar_estado([
        '########',
        '#   @* #',
        '########',
    ], grilla)
    assert soko.juego_ganado(grilla)

def test9():
    desc = [
        '#####',
        '# * #',
        '#+ *#',
        '#####',
    ]
    desc2 = [
        '#####',
        '# * #',
        '#.@*#',
        '#####',
    ]
    grilla1 = soko.crear_grilla(desc)
    grilla1 = soko.mover(grilla1,ESTE)
    verificar_estado(desc2, grilla1)

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    print("Todo OK :)")

main()
