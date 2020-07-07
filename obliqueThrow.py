import random
import math

class obliqueThrow:
    def __init__(self):
        self.__setDist()
        self.setGravity()

    def __setDist(self):
        self.dist = random.randint(10, 100)

    def __setVel(self):
        self.vel = input("Qual a sua velocidade inicial? (m/s): ")

        try:
            self.vel = self.vel.replace(',', '.', 1)
            self.vel = float(self.vel)
        except ValueError:
            print("Velocidade ajustada para 5")
            self.vel = 5

    def __setAngle(self):
        ang = input("Qual será o ângulo do pulo? (º) : ")

        try:
            ang = ang.replace(',', '.', 1)
            ang = float(ang)
            if ang > 90:
                print("Ângulo ajustado para 45º")
                ang = 45
        except ValueError:
            print("Ângulo ajustado para 45º")
            ang = 45
        self.__grausToRad(ang)

    def __grausToRad(self, ang):
        self.ang = (ang/180)*math.pi

    def setGravity(self):
        self.g = 10

    def startGame(self):
        print("Sua tarefa: chegar do outro lado sem cair")
        i = 1
        while i <= 2:
            self.__showProblem(i)
            self.__askAnswer()

            if not self.__reviseAnswer(i):
                print("Caiu :(")
            else:
                print("Passou :)")
                self.__setDist()
                i+=1

        print("Parabéns, você passou para a próxima fase!")

    def __showProblem(self, hole):
        print(" - Largura do {}º buraco: {}m".format(hole, self.dist))
        if hole == 1:
            print(" - Largura da base: 5m")

    def __askAnswer(self):
        self.__setVel()
        self.__setAngle()

    def __reviseAnswer(self, hole):
        #A = V².Sen2Θ/g
        Alcance = (math.pow(self.vel, 2) * math.sin(2*self.ang))/self.g

        if Alcance >= self.dist:
            if (hole == 1 and Alcance <= self.dist+5.0) or (hole == 2):
                return True
        else:
            return False


    def __str__(self):
        return f'Dist: {self.dist} __ Velo: {self.vel} __ Ang: {self.ang} __ G: {self.g}'