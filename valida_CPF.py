"""
Validaçao do CPF

Os dois dígitos de verificação do CPF (constituído de 9 dígitos) são calculados através de um complicado algoritmo:

Etapa 1: cálculo de DV1
    Soma 1: soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro).
    Multiplique a soma 1 por 10 e calcule o resto da divisão do resultado por 11. Se der 10, DV1 é zero,caso contrário o DV1 é o próprio resto.

Etapa 2: cálculo de DV2
    Soma 2: soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa.
    Adicione a Soma 2 ao dobro do DV1, multiplique por 10 e calcule o resto da divisão do resultado por 11.
    Se der 10, DV2 é zero, caso contrário o DV2 é o próprio resto.

Etapa 3: Multiplique DV1 por 10, some com DV2 e você tem o número de controle do CPF.

Exemplo: para o CPF 398 136 146, temos:

Etapa 1: 2x6 + 3x4 + 4x1 + 5x6 + 6x3 + 7x1 + 8x8 + 9x9 + 10x3 = 258
258 * 10 mod 11 = 6, portanto, DV1 = 6

Etapa 2: 3x6 + 4x4 + 5x1 + 6x6 + 7x3 + 8x1 + 9x8 + 10x9 + 11x3 = 299
(299 + 6x2)x10 mod 11 = 3150 mod 11 = 8, portanto DV2 = 8

Etapa 3: DV1x10 + DV2 = 6x10 + 8 = 68, que é o número procurado.
"""
from random import randint


def _dv1_bruto(cpf):
    """Calcula o DV1 do CPF"""

    return sum(((i + 2) * int(d) for i, d in enumerate(cpf[::-1])))


def _dv1(cpf):
    """Calcula o DV1 do CPF"""

    resultado = _dv1_bruto(cpf) * 10 % 11
    return resultado if resultado < 10 else 0


def _dv2_bruto(cpf):
    """Calcula o DV2 do CPF"""

    return sum(((i + 3) * int(d) for i, d in enumerate(cpf[::-1])))


def _dv2(cpf):
    """Calcula o DV2 do CPF"""

    resultado = (_dv2_bruto(cpf) + _dv1(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0


def _dv_calculado(cpf):
    """Calcula o DV final do CPF"""

    return str(_dv1(cpf)) + str(_dv2(cpf))


def _tira_mascara_cpf(cpf):
    """Remove a máscara, deixando apenas os algarismos"""
    return "".join([c for c in cpf if c.isdigit()])


def _dv_original(cpf):
    """Pega os dois últimos dígitos do CPF"""
    return cpf[-2:]


def _tira_dv(cpf):
    """Retorna o CPF sem os dois últimos dígitos"""
    return cpf[:-2]


def _valida_tamanho_cpf(cpf):
    """Valida o tamanho do CPF"""

    cpf = _tira_mascara_cpf(cpf)
    return len(cpf) == 11


def cpf_valido(cpf):
    """Valida o CPF"""

    cpf = _tira_mascara_cpf(cpf)
    return _dv_original(cpf) == _dv_calculado(_tira_dv(cpf)) and _valida_tamanho_cpf(
        cpf
    )


def coloca_mascara_cpf(cpf):
    """Coloca a máscara no CPF"""
    cpf = _tira_mascara_cpf(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def gera_cpf(formatado=False):
    """Gera um CPF válido"""

    cpf = "".join([str(randint(0, 9)) for i in range(9)])
    cpf += _dv_calculado(cpf)
    return cpf if not formatado else coloca_mascara_cpf(cpf)


def gera_cpf_2():
    """Gera um CPF válido"""
    from random import random

    cpf = str(random())[2:11]
    return cpf


def gera_lista_cpfs(qtd=10, formatado=False):
    """Gera uma lista de CPFs válidos"""

    return [gera_cpf(formatado) for i in range(qtd)]


# teste de desempenho
if __name__ == "__main__":
    from timeit import timeit

    print(timeit(gera_cpf(), number=10000))
    print(timeit(gera_cpf_2(), number=10000))
