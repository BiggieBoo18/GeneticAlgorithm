#coding: utf-8

"""
GA(Genetic Algorithm, 遺伝的アルゴリズム)
Main Class

Create: 2016/11/27
Update: 2016/11/29
"""
import argparse
import random
from   genetic.individual import Individual
from   genetic.population import Population
from   genetic.select     import Select
from   genetic.crossover  import Crossover
from   genetic.mutation   import Mutation
from   genetic.util       import *

def calcFit(ind):
    """
    Create Calculation Fitness Function
    """
    return sum(ind)

def main():
    #引数の設定
    parser = argparse.ArgumentParser()
    parser.add_argument('--revo  '   ,  dest='revo'         , type=int,   default=300,  help='revolution count>0')
    parser.add_argument('--popcnt  ' ,  dest='popcnt'       , type=int,   default=1000, help='population count>0')
    parser.add_argument('--gene ' ,     dest='gene'         , type=int,   default=10,   help='number of gene>0')
    parser.add_argument('--maxormin  ', dest='maxormin'     , type=str,   default="max",help='max or min')
    parser.add_argument('--esize  '  ,  dest='eliteSize'    , type=int,   default=1,    help='elite size>=0')
    parser.add_argument('--tsize  '  ,  dest='tornSize'     , type=int,   default=2,    help='tornament size>=2')
    parser.add_argument('--ctype  '  ,  dest='cross_type'   , type=str,   default="one",help='crossover type one or two or random')
    parser.add_argument('--cprob  '  ,  dest='cross_prob'   , type=float, default=0.4,  help='crossover probability>=0.0')
    parser.add_argument('--random  ' ,  dest='randnum'      , type=int,   default=3,    help='crossover randomPoints random number>=0')
    parser.add_argument('--mprob  '  ,  dest='mutation_prob', type=float, default=0.05, help='mutation probability>=0.0')
    parser.add_argument('--dataset  ',  dest='dataset'      , type=str,   default="",   help='dataset file path')
    parser.add_argument('--dtype  '  ,  dest='dtype'        , type=str,   default="int",help='dataset type string or integer or float')
    args = parser.parse_args()
    if (args.revo         <0   or 
        args.popcnt       <0   or 
        args.gene         <0   or
        args.maxormin    ==""  or
        args.eliteSize    <0   or 
        args.tornSize     <2   or 
        args.cross_prob   <0.0 or 
        args.randnum      <0   or 
        args.mutation_prob<0.0 or 
        args.dataset== ""      or
        args.dtype  == ""):
        print("argment parse Error!")
        exit()

    revo          = args.revo
    popcnt        = args.popcnt
    gene          = args.gene
    maxormin      = args.maxormin
    eliteSize     = args.eliteSize
    tornSize      = args.tornSize
    cross_prob    = args.cross_prob
    randnum       = args.randnum
    mutation_prob = args.mutation_prob
    
    fd      = open(args.dataset, "r")
    rawdata = fd.readlines()
    fd.close()
    dataset = []
    if   (args.dtype == "int"):
        dtype = int
    elif (args.dtype == "str"):
        dtype = str
    else:
        dtype = float
    for i in rawdata:
        tmp = i.strip("\n")
        dataset.append(dtype(tmp.strip("\r")))

    life = []
    for i in range(popcnt):
        g = []
        for j in range(gene):
            g.append(random.choice(dataset))
        life.append(g)
    
    population = []
    for i in range(popcnt):
        ind = Individual(i+1)
        ind.CreateIndividual(life[i], 0)
        fit = ind.CalcFitness(calcFit)
        ind.SetFitness(fit)
        population.append(ind)

    ppl = Population()
    ppl.CreatePopulation(population)
    ppl.SortInFitness(maxormin)

    select    = Select(eliteSize, tornSize)
    cross     = Crossover(cross_prob)
    mut       = Mutation(dataset, mutation_prob)
    if   (args.cross_type == "two"):
        cross_type = cross.twoPoints
    elif (args.cross_type == "random"):
        cross_type = cross.randomPoints
    else:
        cross_type = cross.onePoint
    
    for i in range(revo):
        print("revolution: {0}".format(i))
        elite     = select.SelectElite(ppl)
        next_gene = elite
        while (len(next_gene)<popcnt):
            offspring = select.SelectTornament(ppl)
            if (args.cross_type == "random"):
                cross_offspring    = cross_type(offspring, randnum)
            else:
                cross_offspring    = cross_type(offspring)
            mutation_offspring = mut.Mutation(cross_offspring)
            for j in range(len(mutation_offspring)):
                fit = mutation_offspring[j].CalcFitness(calcFit)
                mutation_offspring[j].SetFitness(fit)
                next_gene.append(mutation_offspring[j])
            
        ppl.CreatePopulation(next_gene)
        ppl.SortInFitness(maxormin)

    PrintIndOfPopulation(ppl)
    print "BestFit   :", GetBestFitnessOfPopulation(ppl)
    print "WorstFit  :", GetWorstFitnessOfPopulation(ppl)
    print "AverageFit:", GetAverageFitnessOfPopulation(ppl)

if __name__ == "__main__":
    main()
