from main import Individual

print("Start TestIndividual\n")

print("-initialize Individual")
ind  = Individual(0)
ind.Print()

print("\n-create Individual")
life = [1, 0, 1, 0, 0]
fit  = 0
ind.CreateIndividual(life, fit)
ind.Print()

print("\n-delete Individual")
ind.DeleteIndividual()
ind.Print()

print("\n-set Individual")
life = [1, 0, 1, 0, 0]
ind.SetIndividual(life)
ind.Print()

print("\n-remove Individual")
ind.RemoveIndividual()
ind.Print()

print("\n-set Fitness")
fit  = 5
ind.SetFitness(fit)
ind.Print()

print("\n-remove Fitness")
ind.RemoveFitness()
ind.Print()

print("\n-calc Fitness")
life = [1, 0, 1, 0, 0]
fit  = 0
ind.CreateIndividual(life, fit)
ind.Print()
def calcFit(ind):
    return sum(ind)
fit  = ind.CalcFitness(calcFit, ind.ind)
ind.SetFitness(fit)
ind.Print()

print("\nDone!")
