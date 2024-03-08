from homework.genapganjil import CekBilangan


def test_cek_bilangan_genap():
    cek_bilangan = CekBilangan()
    assert cek_bilangan.cekBilangan(4) == "Genap"


def test_cek_bilangan_ganjil():
    cek_bilangan = CekBilangan()
    assert cek_bilangan.cekBilangan(3) == "Ganjil"


def test_cek_bilangan_negatif():
    cek_bilangan = CekBilangan()
    assert cek_bilangan.cekBilangan(-2) == "Genap"


def test_cek_bilangan_nol():
    cek_bilangan = CekBilangan()
    assert cek_bilangan.cekBilangan(0) == "Genap"
