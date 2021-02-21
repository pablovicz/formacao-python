class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url Inválida!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        valor = self.split_string("valor=")
        moeda_origem = self.extrai_moeda("moedadestino=")
        moeda_destino = self.extrai_moeda("moedaorigem=")
        representacao_string = f'Valor: {valor} \nMoeda de Origem: {moeda_origem} \nMoeda de Destino: {moeda_destino}'
        return representacao_string

    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url

    @staticmethod
    def url_eh_valida(url):
        if url and url.startswith("https://bytebank.com/"):
            return True
        else:
            return False

    def extrai_argumentos(self):

        moeda_origem = self.extrai_moeda("moedadestino=")

        moeda_destino = self.extrai_moeda("moedaorigem=")

        if moeda_origem == moeda_destino:
            self.troca_moeda_origem(self)

        valor = self.split_string("valor=")

        return moeda_origem, moeda_destino, valor

    def split_string(self, moeda_buscada):
        return self.url.split(moeda_buscada)[1]

    def extrai_moeda(self, moeda_buscada):

        moeda = self.split_string(moeda_buscada)

        return moeda[:moeda.find("&")]

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real")
        print(self.url)


