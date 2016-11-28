#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Crossover Class

Create: 2016/11/28
Update: 2016/11/28
"""

import random

class Crossover(object):
    def __init__(self, probability=0.4):
        self.probability = probability
        
    def onePoint(self, offspring):
        parent1 = offspring[0].ind
        parent2 = offspring[1].ind
        if (random.random()<self.probability):
            point   = 0
            if (len(parent1)<len(parent2)):
                point = random.randint(0, len(parent1)-1)
            else:
                point = random.randint(0, len(parent2)-1)
            #print("point:", point)
            tmp             = parent1[point:]
            parent1[point:] = parent2[point:]
            parent2[point:] = tmp

        return [parent1, parent2]

    def twoPoints(self, offspring):
        parent1 = offspring[0].ind
        parent2 = offspring[1].ind
        if (random.random()<self.probability):
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

        return [parent1, parent2]

    def randomPoints(self, offspring, randnum):
        parent1 = offspring[0].ind
        parent2 = offspring[1].ind
        if (random.random()<self.probability):
            point  = 0
            for i in range(randnum):
                if (len(parent1)<len(parent2)):
                    point = random.randint(0, len(parent1)-1)
                else:
                    point = random.randint(0, len(parent2)-1)
                #print("point:", point)
                tmp            = parent1[point]
                parent1[point] = parent2[point]
                parent2[point] = tmp

        return [parent1, parent2]

    def Print(self):
        print("probability: {0}".format(self.probability))
