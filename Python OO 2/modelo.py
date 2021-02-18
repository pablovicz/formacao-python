class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)




vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
tmep = Filme("todo mundo em pânico", 1999, 100)
tmep.dar_like()
tmep.dar_like()
atlanta = Serie("Atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor = Serie("Demolidor", 2016, 2)
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]




playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tá ou nao tá? {demolidor in playlist_fim_de_semana}')






