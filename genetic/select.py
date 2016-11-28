#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Select Class <Elite&Tournament>

Create: 2016/11/28
Update: 2016/11/28
"""

import random

class Select(object):
    def __init__(self, eliteSize=1, tornSize=2):
        self.eliteSize = eliteSize
        self.tornSize  = tornSize
        
    def SetEliteSize(self, eliteSize):
        self.eliteSize = eliteSize

    def SetTornSize(self, tornSize):
        self.tornSize = tornSize

    def SelectElite(self, population):
        elite = population.population[0:self.eliteSize+1]
        return elite

    def SelectTornament(self, population):
        offspring = []
        for i in range(2):
            sample    = random.sample(population.population[self.eliteSize+1:], self.tornSize)
            offspring.append(max(sample, key=sample.index))
        return offspring

    def Print(self):
        print("elite size: {0}".format(self.eliteSize))
        print("torn  size: {0}".format(self.tornSize))
