from main import Individual

print("Start TestIndividual\n")

print("-initialize Individual")
ind  = Individual()
ind.PrintIndividual()

print("\n-create Individual")
life = [1, 0, 1, 0, 0]
fit  = 0
ind.CreateIndividual(life, fit)
ind.PrintIndividual()

print("\n-delete Individual")
ind.DeleteIndividual()
ind.PrintIndividual()

print("\n-set Individual")
life = [1, 0, 1, 0, 0]
ind.SetIndividual(life)
ind.PrintIndividual()

print("\n-remove Individual")
ind.RemoveIndividual()
ind.PrintIndividual()

print("\n-set Fitness")
fit  = 5
ind.SetFitness(fit)
ind.PrintIndividual()

print("\n-remove Fitness")
ind.RemoveFitness()
ind.PrintIndividual()

print("\n-calc Fitness")
life = [1, 0, 1, 0, 0]
fit  = 0
ind.CreateIndividual(life, fit)
ind.PrintIndividual()
def calcFit(ind):
    return sum(ind)
fit  = ind.CalcFitness(calcFit)
ind.SetFitness(fit)
ind.PrintIndividual()

print("\nDone!")
