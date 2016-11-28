from genetic.individual import Individual
from genetic.population import Population
from genetic.select     import Select
from genetic.crossover  import Crossover

print("Start TestCrossover\n")

print("-initialize Crossover")
cross = Crossover(0.4)
print(cross)

print("\n-onePoint")
def calcFit(ind):
    return sum(ind)
life = [[1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1]]

population = []
for i in range(len(life)):
    ind  = Individual()
    ind.CreateIndividual(life[i], 0)
    fit  = ind.CalcFitness(calcFit)
    ind.SetFitness(fit)
    population.append(ind)

ppl = Population()
ppl.CreatePopulation(population)
ppl.SortInFitness("max")
ppl.Print()

print("Before")
select    = Select(1, 2)
offspring = select.SelectTornament(ppl)
for i in offspring:
    i.Print()
print("After")
cross_offspring = cross.onePoint(offspring)
for i in offspring:
    i.Print()

print("\n-twoPoints")
print("Before")
for i in offspring:
    i.Print()
print("After")
cross_offspring = cross.twoPoints(offspring)
for i in offspring:
    i.Print()

print("\n-randomPoints")
print("Before")
for i in offspring:
    i.Print()
print("After")
cross_offspring = cross.randomPoints(offspring, 3)
for i in offspring:
    i.Print()

print("\nDone!")
