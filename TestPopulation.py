from genetic.individual import Individual
from genetic.population import Population

print("Start TestPopulationl\n")

print("-initialize Population")
ppl  = Population()
ppl.Print()

print("\n-create Population")
def calcFit(ind):
    return sum(ind)
life = [[1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0]]
population = []
for i in range(len(life)):
    ind  = Individual(i+1)
    ind.CreateIndividual(life[i], 0)
    fit  = ind.CalcFitness(calcFit, ind.ind)
    ind.SetFitness(fit)
    population.append(ind)

ppl = Population()
ppl.CreatePopulation(population)
ppl.Print()

print("\n-sort Population")
ppl.SortInFitness("max")
ppl.Print()
ppl.SortInFitness("min")
ppl.Print()

print("\n-delete Population")
ppl.DeletePopulation()
ppl.Print()

print("\n-add Individual")
life = [1, 0, 1, 0, 0]
ind = Individual(0)
ind.CreateIndividual(life, 0)
ppl = Population()
ppl.AddIndividual(ind)
ppl.Print()

print("\n-remove Individual in num")
ppl.RemoveIndividualByNum(0)
ppl.Print()

print("\nDone!")
