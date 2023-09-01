import random
from colorama import Fore, Style

regiao_fiscal = str(input("Digite a sigla de seu estado natal, exemplo: DF, GO, MT...: ")).upper().strip()
quantidade = int(input("Quantos cpfs a ser gerados? "))

REGIOES = {
    "1": ["GO", "DF", "MS", "MT", "TO"],
    "2": ["AC", "AM", "PA", "RO", "RR"],
    "3": ["CE", "MA", "PI"],
    "4": ["AL", "PB", "PE", "RN"], 
    "5": ["BA", "SE"],
    "6": ["MG"],
    "7": ["ES", "RJ"],
    "8": ["SP"],
    "9": ["PR", "SC"],
    "0": ["RS"],
}

def numero_por_estado(estado):
    for numero, estados in REGIOES.items():
        if estado in estados:
            return numero
    return None

def gerar_d1ad9():
    digitos = []
    for i in range(8):
        digitos.append(str(random.randint(0, 9)))

    _regiao = numero_por_estado(regiao_fiscal)
    if not _regiao:
        print("Não existe regiao chamada: ", regiao_fiscal)
        exit()
    digitos.append(str(_regiao))
    return " ".join(digitos)

def gerar_d10(numbers):
    l, n = 0, 10
    d10 = 0
    for d in numbers:
        d = int(d)
        l += n*d
        n -= 1

    r = l%11
    if r == 0 or r == 1:
        d10 = 0
    else:
        d10 = 11-r
    return d10

def gerar_d11(number, d10):
    number = number.copy()
    number.append(d10)
    number.pop(0)
    m, n = 0, 10
    d11 = 0
    for d in number:
        d = int(d)
        m += n*d
        n -= 1
    r = m%11
    if r == 0 or r == 1:
        d11 = 0
    else:
        d11 = 11-r
    return d11

def gerar_base():
    base = gerar_d1ad9()
    numeros = base.split(" ")
    return numeros

def formatar_cpf(cpf_numeros):
    cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
    return cpf_formatado

def gerar_cpf():
    base = gerar_base()

    d10 = gerar_d10(base)
    d11 = gerar_d11(base, d10)

    base.append(d10)
    base.append(d11)

    base = list(map(str, base))

    return formatar_cpf("".join(base))

for i in range(quantidade):
    cpf = gerar_cpf()
    print(f"{Fore.BLUE}{Style.BRIGHT}{cpf}")