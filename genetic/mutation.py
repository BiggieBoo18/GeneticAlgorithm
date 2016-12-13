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
                for j in range(len(mutate_offspring[i].ind)):
                    if (random.random()<self.probability):
                        #print("<DEBUG> mutation")
                        m = random.choice(self.dataset)
                        if (mutate_offspring[i].ind[j]!=m):
                            mutate_offspring[i].ind[j] = m
        return (mutate_offspring)

    def Print(self):
        print("dataset    : {0}".format(self.dataset))
        print("probability: {0}".format(self.probability))
