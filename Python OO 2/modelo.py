class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
       return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes: {self._likes}'



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} temporadas - Likes: {self._likes}'




vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()



filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)












