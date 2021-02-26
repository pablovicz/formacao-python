
## try /  except

def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve receber apenas argumentos inteiros")
    try:
        return dividendo // divisor
    except:
        print(f'Não foi possível dividir {dividendo} por {divisor}')
        raise

def testa_divisao(divisor):
    resultado = ""
    try:
        #teste = 'teste'
        #teste.ola()
        resultado = dividir(10, divisor)
        if resultado != "":
            print(f'O resultado da divisão de 10 por {divisor} é {resultado}')

    except ZeroDivisionError as E:
        print(E.__class__.__bases__) ## printa classe pai da exception
        raise ZeroDivisionError('Erro de divisão por 0 tratado')
    except AttributeError as E:
        print(E.__class__.__bases__)
        raise AttributeError('Erro de atributo tratado')
#    except Exception:
#        raise Exception('Erro genérico') # caso nenhum dos anteriores seja indenficado, faz o traatamento generico de erros

## https://docs.python.org/3/library/exceptions.html

testa_divisao(5.8)






