from genetic.individual import Individual
from genetic.population import Population
from genetic.select     import Select
from genetic.crossover  import Crossover

print("Start TestCrossover\n")

print("-initialize Crossover")
cross = Crossover(1)
print(cross)

def calcFit(ind):
    return sum(ind)
life = [[1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1]]

population = []
for i in range(len(life)):
    ind  = Individual(0)
    ind.CreateIndividual(life[i], 0)
    fit  = ind.CalcFitness(calcFit, ind.ind)
    ind.SetFitness(fit)
    population.append(ind)

ppl = Population()
ppl.CreatePopulation(population)
ppl.SortInFitness("max")
ppl.Print()

print("\n-onePoint")
print("Before")
select    = Select(1, 2)
offspring = select.SelectTornament(ppl)
for i in offspring:
    i.Print()
print("After")
cross_offspring = cross.onePoint(offspring)
for i in cross_offspring:
    i.Print()

print("\n-twoPoints")
print("Before")
for i in offspring:
    i.Print()
print("After")
cross_offspring = cross.twoPoints(offspring)
for i in cross_offspring:
    i.Print()

print("\n-randomPoints")
print("Before")
for i in offspring:
    i.Print()
print("After")
cross_offspring = cross.randomPoints(offspring)
for i in cross_offspring:
    i.Print()

print("\nDone!")
