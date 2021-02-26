from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_formata()

    def mes_cadastro(self):
        meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril",
                        "Maio", "Junho", "Julho", "Agosto",
                        "Setembro", "Outubro", "Novembro", "Dezembro")
        mes_cadastro = meses_do_ano[self.momento_cadastro.month]
        return mes_cadastro

    def dia_cadastro(self):
        dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
        dia_cadastro = dias_da_semana[self.momento_cadastro.weekday()]
        return dia_cadastro

    def data_formata(self):
        data_formatada = self.momento_cadastro.strftime(("%d/%m/%Y %H:%M"))
        return data_formatada

    def tempo_cadastro(self):
        #tempo_cadastro = datetime.today() -  self.momento_cadastro
        tempo_cadastro = (datetime.today() + timedelta(days=30, hours=15)) - self.momento_cadastro
        return tempo_cadastro