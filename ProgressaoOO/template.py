#Filmes e Series tem as seguintes características

# Filme: Nome, ano, duração, curtir
# Série: Nome, ano, temporadas, curtir

# Criamos a classe Filme
class Filme:
    def __init__ (self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtir = 0

    def curtida(self):
        self.__curtir += 1
    
    @property
    def valorCurtir(self):
        return self.__curtir

    @property
    def valorTitulo(self):
        return self.__nome



avatar = Filme('Avatar', 2009, 177)
avatar.curtida()
print(f"Nome: {avatar.__nome}\nAno: {avatar.ano}\nDuracao: {avatar.duracao}m\nCurtidas: {avatar.__curtir}\n")


class Series:
    def __init__ (self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__curtir = 0

    def curtida(self):
        self.__curtir += 1

    @property
    def valorCurtir(self):
        return self.__curtir

    @property
    def valorTitulo(self):
        return self.__nome

invincible = Series('Invincible', 2021, 4)
print(f"Nome: {invincible.__nome}\nAno: {invincible.ano}\nNº de Temporadas: {invincible.temporadas}\nCurtidas: {invincible.__curtir}\n")