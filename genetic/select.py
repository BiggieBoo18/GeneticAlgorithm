#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Select Class <Elite&Tournament>

Create: 2016/11/28
Update: 2016/12/18
"""

import random
from   individual import Individual
from   util       import *

class Select(object):
    def __init__(self, eliteSize=1, tornSize=2):
        self.eliteSize = eliteSize
        self.tornSize  = tornSize
        
    def SetEliteSize(self, eliteSize):
        self.eliteSize = eliteSize

    def SetTornSize(self, tornSize):
        self.tornSize = tornSize

    def SelectElite(self, population):
        elite = []
        elite_gene = population.population[0:self.eliteSize]
        for i in elite_gene:
            ind = Individual(i.GetIndid())
            ind.CreateIndividual(i.GetIndividual(), i.GetFitness())
            elite.append(ind)
        return elite

    def SelectTornament(self, population):
        offspring      = []
        offspring_gene = []
        for i in range(2):
            sample = random.sample(population.population[self.eliteSize:], self.tornSize)
            #print("<DEBUG> sample is")
            #PrintIndOfList(sample)
            offspring_gene.append(max(sample, key=(lambda x:x.fit)))

        for i in offspring_gene:
            ind = Individual(i.GetIndid())
            ind.CreateIndividual(i.GetIndividual(), 0)
            offspring.append(ind)
        return offspring

    def Print(self):
        print("elite size: {0}".format(self.eliteSize))
        print("torn  size: {0}".format(self.tornSize))
