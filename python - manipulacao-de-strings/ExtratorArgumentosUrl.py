class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!!")

    @staticmethod
    def url_eh_valida(url):
        if url:
            return True
        else:
            return False

    def extrai_argumentos(self):

        moeda_origem = self.cut_string("moedadestino=")
        moeda_destino = self.cut_string("moedaorigem=")
        valor = self.split_string("valor=")

        return moeda_origem, moeda_destino, valor

    def split_string(self, moeda_buscada):
        return self.url.split(moeda_buscada)[1]

    def cut_string(self, moeda_buscada):

        moeda = self.split_string(moeda_buscada)

        return moeda[:moeda.find("&")]