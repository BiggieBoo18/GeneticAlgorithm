#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Mainプログラム

Create: 2016/11/27
Update: 2016/11/27
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

    def RemoveIndividual(self, num):
        del self.population[num]

    def PrintPopulation(self):
        print("population: {0}".format(self.population))

class Individual(object):
    def __init__(self):
        self.ind = []   # individual
        self.fit = 0.0  # fittness

    def CreateIndividual(self, life, fit):
        self.ind = life
        self.fit = fit
        
    def DeleteIndividual(self):
        del self.ind[:]
        self.fit = 0.0

    def SetIndividual(self, life):
        self.ind = life
    
    def RemoveIndividual(self):
        del self.ind[:]

    def SetFitness(self, fit):
        self.fit = fit

    def RemoveFitness(self):
        self.fit = 0

    def CalcFitness(self, calc):
        return calc(self.ind)

    def PrintIndividual(self):
        print("individual: {0}".format(self.ind))
        print("fittness  : {0}".format(self.fit))
