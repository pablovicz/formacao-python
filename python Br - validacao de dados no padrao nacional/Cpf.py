from validate_docbr import CPF

class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.cpf_formatado()

    def cpf_eh_valido(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def cpf_formatado(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
