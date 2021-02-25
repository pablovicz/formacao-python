from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!!")


class DocCpf:

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


class DocCnpj:

    def __init__(self, documento):

        documento = str(documento)

        if self.cnpj_eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.cnpj_formatado()

    def cnpj_eh_valido(self, cnpj):
        validator = CNPJ()
        return validator.validate(cnpj)

    def cnpj_formatado(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

