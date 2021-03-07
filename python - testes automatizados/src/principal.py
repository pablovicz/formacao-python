from src.leilao.dominio import Usuario, Leilao, Lance, Avaliador


gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_gui = Lance(gui, 100.0)
lance_do_yuri = Lance(yuri, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')


avaliador = Avaliador()

avaliador.avalia(leilao)

print(f'o menor lance do leilao é {avaliador.menor_lance} e o maior lance é {avaliador.maior_lance}' )