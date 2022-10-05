# ATIVIDADE 01

class Socio:
    def __init__(self, nome, cpf, nascimento, mes, ano):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.mes = mes
        self.ano = ano


class Clube:
    def __init__(self):
        self.socios = []                    # lista de sócios começa vazia

    def associar(self, socio):
        self.socios.append(socio)           # insere sócio na lista de sócios

    def numero_de_socios(self):
        return len(self.socios)             # retorna a quantidade de sócios

    def mes_associacao(self, mes, ano):
        if mes < 1 or mes > 12:             # valida o mês
            raise TypeError
        if len(str(ano)) != 4:              # valida o ano
            raise ValueError

        quantidade = 0
        for socio in self.socios:           # percorre a lista de sócios
            if socio.mes == mes and socio.ano == ano:
                quantidade += 1
        return quantidade                   # retorna a quantidade de sócios

    def expulsar(self, mes, ano):
        if mes < 1 or mes > 12:             # valida o mês
            raise TypeError
        if len(str(ano)) != 4:              # valida o ano
            raise ValueError

        nomes = []                          # lista de nomes
        socios_aux = []                     # lista auxiliar

        for socio in self.socios:           # percorre lista de sócios
            if socio.mes == mes and socio.ano == ano:
                nomes.append(socio.nome)    # insere o nome na lista de nomes
            else:
                socios_aux.append(socio)    # insere objeto na lista auxiliar

        self.socios = socios_aux            # atualiza lista de sócios do clube

        nomes.sort()                        # ordena a lista de nomes
        return nomes                        # retorna a lista de nomes
