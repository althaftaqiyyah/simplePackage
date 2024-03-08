from homework.calculator import Calculator


def test_penjumlahan():
    calc = Calculator()
    assert calc.penjumlahan(3, 5) == 8


def test_pengurangan():
    calc = Calculator()
    assert calc.pengurangan(5, 3) == 2


def test_perkalian():
    calc = Calculator()
    assert calc.perkalian(7, 2) == 14


def test_pembagian():
    calc = Calculator()
    assert calc.pembagian(10, 2) == 5


def test_bagi_nol():
    calc = Calculator()
    assert calc.pembagian(10, 0) == 0
