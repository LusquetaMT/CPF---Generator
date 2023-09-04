import random
import os
from colorama import Fore, Style

d9ad12 = [0, 0, 0, 1]
w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
w2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

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

def gerar_d1ad9_cpf(regiao):
    digitos = []
    for i in range(8):
        digitos.append(str(random.randint(0, 9)))

    digitos.append(str(regiao))
    return " ".join(digitos)

def gerar_d10_cpf(numbers):
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

def gerar_d11_cpf(number, d10):
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

def gerar_base_cpf(regiao):
    base = gerar_d1ad9_cpf(regiao)
    numeros = base.split(" ")
    return numeros

def formatar_cpf(cpf_numeros):
    cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
    return cpf_formatado

def gerar_cpf(regiao):
    base = gerar_base_cpf(regiao)

    d10 = gerar_d10_cpf(base)
    d11 = gerar_d11_cpf(base, d10)

    base.append(d10)
    base.append(d11)

    base = list(map(str, base))

    return formatar_cpf("".join(base))

def d1ad8_cnpj():
    numbers = []
    for i in range(8):
        numbers.append(random.randint(0, 9))
    return numbers

def generate_d13_cnpj(numbers):
    sum = 0
    for i, w in enumerate(w1):
        sum += numbers[i] * w
    r = sum % 11
    if r < 2: d = 0
    else: d = 11 - r 
    return d

def generate_d14_cnpj(numbers, d13):
    numbers = numbers.copy()
    numbers.append(d13)
    sum = 0
    for i, w in enumerate(w2):
        sum += numbers[i] * w
    r = sum % 11
    if r < 2: d = 0
    else: d = 11 - r 
    return d

def formatar_cnpj(cnpj):
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/0001-{cnpj[12:14]}"

def gerar_cnpj():
    base = d1ad8_cnpj(); base.extend(d9ad12)
    d13 = generate_d13_cnpj(base)
    d14 = generate_d14_cnpj(base, d13)

    cnpj_incompleto = base.copy()
    cnpj_incompleto.append(d13); cnpj_incompleto.append(d14)
    cnpj_incompleto = [str(element) for element in cnpj_incompleto]

    return formatar_cnpj("".join(cnpj_incompleto))

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

try:
    while True:
        clear()
        comando = int(input(
            f"""\nO que deseja gerar?

{Fore.BLUE}{Style.BRIGHT}[1] CPF
{Fore.GREEN}{Style.BRIGHT}[2] CNPJ
{Fore.RESET}{Style.RESET_ALL}
"""
        ))
        quantidade = int(input("Quantos a ser gerado? "))
        regiao_fiscal = input("Digite seu UF: ").upper()

        print("\n")
        for i in range(quantidade):
            if comando == 1:
                _regiao = numero_por_estado(regiao_fiscal)
                if not _regiao:
                    print("UF inválido!")
                    continue
                else:
                    cpf = gerar_cpf(_regiao)
                    print(f"{Fore.BLUE}{Style.BRIGHT}{cpf}{Fore.RESET}{Style.RESET_ALL}")
            elif comando == 2:
                cnpj = gerar_cnpj()
                print(f"{Fore.BLUE}{Style.BRIGHT}{cnpj}{Fore.RESET}{Style.RESET_ALL}")
            else:
                print("Comando errado, tente novamente!")
        print("\n")
        repetir = input("Repetir? y/n ").lower().strip()
        if repetir == "y":
            continue
        else:
            break

except KeyboardInterrupt:
    print("Programa fechado")
    exit(1)
