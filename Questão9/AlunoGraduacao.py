from Pessoa import Pessoa
class AlunoGraduacao(Pessoa):
    def __init__(self, id, nome, _telefone,__matricula,presencas):
        super().__init__(id, nome, _telefone)
        self.__matricula = __matricula
        self.presencas = presencas

    def marcarPresenca(self,valor=1):
      presencas = self.presencas
      return presencas + valor


    def getMatricula(self):
        return self.__matricula

    def setMatricula(self,matricula):
        self.__matricula = matricula

    def matricular(self):
        return super().matricular()
        