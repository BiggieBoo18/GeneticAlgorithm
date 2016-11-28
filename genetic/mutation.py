#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Mutation Class

Create: 2016/11/28
Update: 2016/11/28
"""

import random

class Mutation(object):
    def __init__(self, dataset, probability=0.05):
        self.dataset     = dataset
        self.probability = probability
        
    def Mutation(self, offspring):
        mutate_offspring = offspring
        for i in range(len(mutate_offspring)):
            if (random.random()<self.probability):
                for j in range(len(mutate_offspring[i])):
                    if (random.random()<self.probability):
                        mutate_offspring[i][j] = random.choice(self.dataset)
                        print("mutation!ind:{0}".format(i))
        return (mutate_offspring)

    def Print(self):
        print("dataset    : {0}".format(self.dataset))
        print("probability: {0}".format(self.probability))
