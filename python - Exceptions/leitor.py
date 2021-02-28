class LeitorDeArquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo

        #raise FileNotFoundError
        print(f'Abrindo arquivo: {self.arquivo}')


    def ler_proxima_linha(self):
        print("lendo linha...")

    def fechar(self):
        raise IOError()
        print("Fechando arquivo...")


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando arquivo")

'''
try:
    leitor = LeitorDeArquivo("meu-arquivo.txt")
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()

#except IOError:
#    print("Execução do tipo IOError capturada e tratada")

## atua como um liberador de recursos, sempre será executado indepedente das excecoes lancadas anterior a ele
finally:
    if 'leitor' in locals():
        leitor.fechar()
'''
        
        
print("usando with ---------------------")
with LeitorDeArquivo("meu-arquivo.txt") as leitor:
    leitor.ler_proxima_linha()



