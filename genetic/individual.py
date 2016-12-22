#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Individual Class

Create: 2016/11/27
Update: 2016/11/28
"""

class Individual(object):
    def __init__(self, indid):
        self.indid = indid # individual id
        self.ind   = []    # individual
        self.fit   = 0.0   # fittness

    def CreateIndividual(self, life, fit):
        self.ind   = life
        self.fit   = fit
        
    def DeleteIndividual(self):
        del self.ind[:]
        self.fit   = 0.0
        self.indid = 0

    def SetIndid(self, indid):
        self.indid = indid

    def GetIndid(self):
        return self.indid

    def RemoveIndid(self):
        self.indid = 0

    def SetIndividual(self, life):
        self.ind = life
    
    def GetIndividual(self):
        return self.ind

    def RemoveIndividual(self):
        del self.ind[:]

    def SetFitness(self, fit):
        self.fit = fit

    def GetFitness(self):
        return self.fit

    def RemoveFitness(self):
        self.fit = 0

    def CalcFitness(self, calc, args):
        return calc(args)

    def Print(self):
        print("--individual id: <{0}>".format(self.indid))
        print("  individual   :  {0}".format(self.ind))
        print("  fittness     :  {0}".format(self.fit))
