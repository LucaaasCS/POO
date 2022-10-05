# ATIVIDADE 02

class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria


class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, superpoder):
        while len(self.__poderes) < 4:
            poderes = self.__poderes.append([superpoder])
            return poderes
        else:
            raise ValueError

    def get_poder_total(self):
        personagem_poderes = self.__poderes
        poder_total = 0

        # poder personagems
        for poder in personagem_poderes:
            # poder categoria
            for x in poder:
                categoria = SuperPoder.get_categoria(x)
                poder_total += categoria

        return poder_total


class SuperHeroi(Personagem):

    def get_poder_total(self):
        acrescimo = super().get_poder_total() * 10/100
        total = super().get_poder_total() + acrescimo
        return total


class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao


class Confronto:

    def lutar(self, superheroi, vilao):
        do_bem = SuperHeroi.get_poder_total(superheroi)
        do_mal = Vilao.get_poder_total(vilao)
        if do_bem > do_mal:
            return 1
        elif do_bem < do_mal:
            return 2
        else:
            return 0
