def PrintIndOfPopulation(ppl):
    for i in ppl.population:
    	i.Print()

def PrintIndOfList(ind):
    for i in ind:
    	i.Print()

def GetBestFitnessOfPopulation(ppl):
    return ppl.population[0].fit

def GetWorstFitnessOfPopulation(ppl):
    return ppl.population[-1].fit

def GetAverageFitnessOfPopulation(ppl):
    totalfit = 0
    for i in ppl.population:
        totalfit += i.fit
    return totalfit/len(ppl.population)

def GetAllFitnessAsList(ppl):
    fitlist = []
    for i in ppl.population:
        fitlist.append(i.fit)
    return fitlist
