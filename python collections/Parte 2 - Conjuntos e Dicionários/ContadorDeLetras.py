from collections import Counter

texto1 = '''
Café pode reduzir volume da massa cinzenta cerebral: as regiões do cérebro envolvidas no controle muscular, percepção sensorial, tomada de decisões e autocontrole, podem ser alteradas pelo consumo regular de cafeína de acordo com um novo estudo realizado pela Universidade de Basileia em um grupo de 20 jovens saudáveis e disponível na página da instituição. A diferença foi particularmente notável na região do cérebro que é essencial para a consolidação da memória. Os pesquisadores também ficaram surpreendidos que o sono dos participantes não foi afetado durante o período do estudo. Segundo a doutora Carolin Reichert, apesar de o consumo diário de cafeína evidentemente afetar o hardware cognitivo, os resultados não significam necessariamente que o consumo de cafeína tenha um impacto negativo no cérebro, o que deve dar origem a novos estudos. Além disso, após 10 dias de abstinência do café, a massa cinzenta se regenerou significativamente nos participantes. Nota: depois de intensa discussão, nós decidimos apresentar este estudo por vir de uma universidade respeitada e ter sido publicado em uma revista científica relevante. No entanto, gostaríamos de saber a sua opinião: um estudo com 20 pessoas é relevante para um estudo dessa natureza? Responda para nós neste email. Obrigado!
'''
texto2 = '''
Telebras e Viasat apresentam antena com tecnologia inédita para conexão de veículos móveis: os painéis da antena KaLMA (Ka band Land Mobile Antenna) são produzidos por meio de impressão 3D, para garantir a precisão dos micro pontos de recepção de sinal, e possui conexão híbrida, permitindo a troca entre o acesso a satélites ou por celular para veículos em velocidades de até 185 Km/h. A tecnologia permite conexão à Internet a uma velocidade de 20 Mbps de download e 2 Mbps de upload de qualquer lugar do Brasil. A tecnologia poderá ser utilizada na prestação de serviços públicos itinerantes, em missões críticas das forças de segurança ou da defesa civil, na indústria de infraestrutura de base, no agronegócio e em ônibus de passageiros. As informações estão na página da Telebras.
'''

texto3 = '''
Firefox 86 lança “Proteção Total de Cookies”: o recurso complementa a eliminação dos supercookies lançada na versão passada, confinando-os aos sites onde foram criados e impedindo o uso por empresas de rastreamento. O recurso é inteligente e abre uma exceção quando os cookies são necessários para fins de não rastreamento, como os usados por provedores de login como Google e Facebook. As informações são do blog da Mozilla.
'''

def analisa_frequencia_de_letras(texto):
    print("----------------------------------------------")
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns =  proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        proporcao = "%.1f" % (proporcao*100)
        print(f'{caractere} -> {proporcao}%')


analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
analisa_frequencia_de_letras(texto3)




