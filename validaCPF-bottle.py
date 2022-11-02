#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from valida_CPF import cpf_valido
from bottle import get, post, request, run

@get('/')
@get('/cpf')
@get('/valida_cpf')
def valida_cpf_entrada():
    return '''
        <h1> Valida CPF </h1>
        <form action="/valida_cpf" method="post">
            CPF: <input id="cpf" name="cpf" type="text" placeholder="CPF" />
            <input value="Validar" type="submit" />
        </form>
    '''

@post('/valida_cpf')
def valida_cpf_saida():
    cpf = request.forms.get('cpf')
    if cpf_valido(cpf):
        return "<p>%s: CPF <strong>válido</strong>.</p>" %cpf
    else:
        return "<p>%s: CPF <strong>inválido</strong>.</p>" %cpf

run(host='localhost', reload=True, port=8080)
