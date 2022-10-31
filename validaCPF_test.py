"""Testes para cálculo do digito verificador do CPF"""
from validaCPF import (
    dv1_bruto,
    dv1,
    dv2_bruto,
    dv2,
    dv_calculado,
    tira_mascara_cpf,
    dv_original,
    cpf_sem_dv,
    valida_tamanho_cpf,
    valida_cpf,
    gera_cpf,
    gera_lista_cpfs,
)


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
    assert dv_calculado("398136146") == "68"
    assert dv_calculado("123456789") == "09"


def test_tira_mascara_cpf_mascara_ok():
    """Se a máscara estiver correta, deve remover a máscara e deixar apenas os algarismos"""
    assert tira_mascara_cpf("123.456.789-09") == "12345678909"
    assert tira_mascara_cpf("398.136.146-68") == "39813614668"
    assert tira_mascara_cpf("936.827.869-53") == "93682786953"


def test_tira_mascara_cpf_sem_mascara():
    """Se estiver sem máscara, deve retornar o próprio CPF"""
    assert tira_mascara_cpf("12345678909") == "12345678909"
    assert tira_mascara_cpf("39813614668") == "39813614668"
    assert tira_mascara_cpf("93682786953") == "93682786953"


def test_tira_mascara_cpf_mascara_errada():
    """Se a máscara estiver errada, deve retornar apenas os algarismos"""
    assert tira_mascara_cpf("123456789-09") == "12345678909"
    assert tira_mascara_cpf("123-456-789-09") == "12345678909"
    assert tira_mascara_cpf("123456789.09") == "12345678909"


def test_pega_dv():
    """Pega o DV do CPF"""
    assert dv_original("12345678909") == "09"
    assert dv_original("39813614668") == "68"
    assert dv_original("93682786953") == "53"


def test_cpf_sem_dv():
    """Retorna o CPF sem o DV"""
    assert cpf_sem_dv("12345678909") == "123456789"
    assert cpf_sem_dv("39813614668") == "398136146"
    assert cpf_sem_dv("93682786953") == "936827869"


def test_valida_tamanho_cpf_com_cpf_valido():
    """Se o CPF tiver 11 dígitos, deve retornar True"""
    assert valida_tamanho_cpf("12345678909") == True
    assert valida_tamanho_cpf("39813614668") == True
    assert valida_tamanho_cpf("93682786953") == True


def test_valida_tamanho_cpf_com_cpf_invalido():
    """Se o CPF tiver menos de 11 dígitos, deve retornar False"""
    assert valida_tamanho_cpf("1234567890") == False
    assert valida_tamanho_cpf("3981361466") == False
    assert valida_tamanho_cpf("9368278695") == False
    assert valida_tamanho_cpf("936827869") == False
    assert valida_tamanho_cpf("93682786") == False
    assert valida_tamanho_cpf("9368278") == False
    assert valida_tamanho_cpf("936827") == False
    assert valida_tamanho_cpf("93682") == False
    assert valida_tamanho_cpf("9368") == False
    assert valida_tamanho_cpf("936") == False
    assert valida_tamanho_cpf("93") == False
    assert valida_tamanho_cpf("9") == False
    assert valida_tamanho_cpf("") == False


def test_valida_cpf_com_cpf_valido():
    """Se o CPF for válido, deve retornar True"""
    assert valida_cpf("12345678909") == True
    assert valida_cpf("39813614668") == True
    assert valida_cpf("93682786953") == True


def test_valida_cpf_com_cpf_invalido():
    """Se o CPF for inválido, deve retornar False"""
    assert valida_cpf("12345678900") == False
    assert valida_cpf("39813614600") == False
    assert valida_cpf("93682786900") == False


def test_gera_cpf():
    """Gera um CPF válido"""
    assert valida_cpf(gera_cpf()) == True


def test_gera_cpf_com_formato_testa_tamanho():
    """Gera um CPF válido com formato e testa o tamanho"""
    assert len(gera_cpf(formatado=True)) == 14
    assert len(gera_cpf(formatado=False)) == 11


def test_gera_lista_cpf_testa_tamanho_lista():
    """Gera uma lista de CPFs válidos"""
    assert len(gera_lista_cpfs(0)) == 0
    assert len(gera_lista_cpfs(1)) == 1
    assert len(gera_lista_cpfs(10)) == 10
    assert len(gera_lista_cpfs(100)) == 100


def test_gera_lista_cpf_testa_validade():
    """Gera uma lista de CPFs válidos e testa a validade"""
    for cpf in gera_lista_cpfs(100):
        assert valida_cpf(cpf) == True


def test_gera_lista_cpf_com_formato_testa_tamanho():
    """Gera uma lista de CPFs válidos com formato e testa o tamanho"""
    for cpf in gera_lista_cpfs(100, formatado=True):
        assert len(cpf) == 14
    for cpf in gera_lista_cpfs(100, formatado=False):
        assert len(cpf) == 11
