#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Crossover Class

Create: 2016/11/28
Update: 2016/11/28
"""

import random
from   util   import *

class Crossover(object):
    def __init__(self, probability=0.4):
        self.probability = probability
        
    def onePoint(self, offspring):
        parent1 = offspring[0].ind
        parent2 = offspring[1].ind
        if (random.random()<self.probability):
            #print("<DEBUG> crossover")
            point   = 0
            if (len(parent1)<len(parent2)):
                point = random.randint(0, len(parent1)-1)
            else:
                point = random.randint(0, len(parent2)-1)
            #print("point:", point)
            tmp             = parent1[point:]
            parent1[point:] = parent2[point:]
            parent2[point:] = tmp

            offspring[0].SetIndividual(parent1)
            offspring[1].SetIndividual(parent2)
            
        return offspring

    def twoPoints(self, offspring):
        parent1 = offspring[0].ind
        parent2 = offspring[1].ind
        if (random.random()<self.probability):
            #print("<DEBUG> crossover")
            #PrintIndOfList(offspring)
            point1  = 0
            point2  = 0
            if (len(parent1)<len(parent2)):
                point1 = random.randint(0, (len(parent1)-1)/2)
                point2 = random.randint((len(parent1)-1)/2, len(parent1)-1)
            else:
                point1 = random.randint(0, (len(parent2)-1)/2)
                point2 = random.randint((len(parent2)-1)/2, len(parent2)-1)
            #print("point1:", point1)
            #print("point2:", point2)
            tmp                    = parent1[point1:point2]
            parent1[point1:point2] = parent2[point1:point2]
            parent2[point1:point2] = tmp

            offspring[0].SetIndividual(parent1)
            offspring[1].SetIndividual(parent2)
            #PrintIndOfList(offspring)
            
        return offspring

    def randomPoints(self, offspring):
        parent1 = offspring[0].ind
        parent2 = offspring[1].ind
        if (random.random()<self.probability):
            #print("<DEBUG> crossover")
            #PrintIndOfList(offspring)
            point  = 0
            if (len(parent1)<len(parent2)):
                for point in range(len(parent1)):
                    if (random.random()<0.5):
                        #print("point:", point)
                        tmp            = parent1[point]
                        parent1[point] = parent2[point]
                        parent2[point] = tmp
            else:
                for point in range(len(parent2)):
                    if (random.random()<0.5):
                        #print("point:", point)
                        tmp            = parent1[point]
                        parent1[point] = parent2[point]
                        parent2[point] = tmp

            offspring[0].SetIndividual(parent1)
            offspring[1].SetIndividual(parent2)
            
        return offspring

    def Print(self):
        print("probability: {0}".format(self.probability))
