from genetic.individual import Individual
from genetic.population import Population
from genetic.select     import Select

print("Start TestSelect\n")

print("-initialize Select")
select = Select(1, 2)
select.Print()

print("\n-SelectElite")
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
    fit  = ind.CalcFitness(calcFit)
    ind.SetFitness(fit)
    population.append(ind)

ppl = Population()
ppl.CreatePopulation(population)
ppl.SortInFitness("max")
ppl.Print()

elite = select.SelectElite(ppl)
print("\nElite!!!")
for i in elite:
    i.Print()

print("\n-SelectTornament")
offspring = select.SelectTornament(ppl)
for i in offspring:
    i.Print()

print("\nDone!")
