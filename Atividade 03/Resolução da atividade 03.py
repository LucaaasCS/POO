# ATIVIDADE 03

from abc import ABC, abstractmethod


class Escola:
    def _init_(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def _init_(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.__diretor = None
        self.__monitor = None

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_diretor(self):
        return self.__diretor

    def get_monitor(self):
        return self.__monitor


class Disciplina:
    def _init_(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa


class Pessoa(ABC):
    def _init_(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    @abstractmethod
    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Professor(Pessoa):
    def _init_(self, nome, nascimento):
        super()._init_(nome, nascimento)

    def incluir_disciplina(self, disciplina):
        return super().incluir_disciplina(disciplina)


class Aluno(Pessoa):
    def _init_(self, nome, nascimento, tipo):
        super()._init_(nome, nascimento)
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    def incluir_disciplina(self, disciplina):
        return super().incluir_disciplina(disciplina)

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, quantidade):
        self.__triunfos = quantidade

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos = quantidade

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feito(self):
        return self.__mau_feitos


class Torneio:
    def _init_(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0

    def get_pontos_casa1(self):
        self.__pontos_casa1

    def get_pontos_casa2(self):
        self.__pontos_casa2
