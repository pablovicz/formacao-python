
## try /  except

def dividir(dividendo, divisor):
    return dividendo / divisor

def testa_divisao(divisor):
    resultado = ""
    try:
        #teste = 'teste'
        #teste.ola()
        resultado = dividir(10, divisor)
        if resultado != "":
            print(f'O resultado da divisão de 10 por {divisor} é {resultado}')

    except ZeroDivisionError:
        raise ZeroDivisionError('Erro de divisão por 0 tratado')
    except AttributeError:
        raise AttributeError('Erro de atributo tratado')




testa_divisao(0)






