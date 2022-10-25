"""Testes para cálculo do digito verificador do CPF"""
from validaCPF import dv1_bruto, dv1, dv2_bruto, dv2, dv


def test_dv1_bruto():
    """Obtem o resultado da soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro)."""
    assert dv1_bruto("398136146") == 258
    assert dv1_bruto("123456789") == 210


def test_dv1():
    """Calcula o DV1 do CPF"""
    assert dv1("398136146") == 6
    assert dv1("123456789") == 0


def test_dv2_bruto():
    """Obtem o resultado da soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa."""
    assert dv2_bruto("398136146") == 299
    assert dv2_bruto("123456789") == 255


def test_dv2():
    """Calcula o DV2 do CPF"""
    assert dv2("398136146") == 8
    assert dv2("123456789") == 9


def test_dv():
    """Calcula o DV final do CPF"""
    assert dv("398136146") == "68"
    assert dv("123456789") == "09"
