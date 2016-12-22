#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Population Class

Create: 2016/11/27
Update: 2016/11/28
"""

class Population(object):
    def __init__(self):
        self.population = []
        
    def CreatePopulation(self, population):
        self.population = population

    def DeletePopulation(self):
        del self.population[:]

    def AddIndividual(self, ind):
        self.population.append(ind)

    def RemoveIndividualByNum(self, num):
        del self.population[num]

    def SortInFitness(self, maxormin="max"):
        reverse=True
        if(maxormin=="min"):
            reverse=False

        self.population = sorted(self.population, key=lambda individual: individual.fit, reverse=reverse)

    def Print(self):
        print("population: {0}".format(self.population))
        for i in self.population:
            i.Print()
