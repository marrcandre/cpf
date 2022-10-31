from valida_CPF import coloca_mascara_cpf, cpf_valido

# cpf = "936.827.869-53"
# cpf = "398.136.146-00"
# cpf = "016.762.399-01"


while True:
    cpf = input("Informe o CPF a ser verificado: ")
    if not cpf:
        break
    if cpf_valido(cpf):
        print("CPF Válido:", coloca_mascara_cpf(cpf))
    else:
        print("CPF Inválido:", cpf)
