from genetic.individual import Individual
from genetic.population import Population
from genetic.select     import Select
from genetic.crossover  import Crossover
from genetic.mutation   import Mutation

print("Start TestMutation\n")

print("-initialize Mutation")
mut = Mutation([0,1], 1)
mut.Print()

print("\n-Mutation")
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

print("Before")
select    = Select(1, 2)
offspring = select.SelectTornament(ppl)
for i in offspring:
    i.Print()
print("After")
cross = Crossover(0.4)
cross_offspring = cross.onePoint(offspring)
for i in offspring:
    i.Print()

for c in range(100):
    print("\n-Mutation")
    print("Before")
    for i in offspring:
        i.Print()
    mutation_offspring = mut.Mutation(cross_offspring)
    print("After")
    for i in mutation_offspring:
        i.Print()
print("\nDone!")
