import population
import random
def find_best(list1):
    best_fintness_value=max(list1)
    best_fintness_index=list1.index(best_fintness_value)
    return best_fintness_index,best_fintness_value



def find_worst(list1):
    worst_fintness_value=min(list1)
    worst_fintness_index=list1.index(worst_fintness_value)
    return worst_fintness_index,worst_fintness_value


def selection(pop):
    select_i=0
    newfit_value=[]
    total_fit = sum(pop.fitness)
    for i in range(len(pop.fitness)):
        if i==0:
            newfit_value.append(pop.fitness[i] / total_fit)
        else:
            newfit_value.append(pop.fitness[i] / total_fit+newfit_value[i-1])

    a=random.random()
    for i in range(len(pop.fitness)):
        if a<newfit_value[i]:
            select_i= i
            break
    return select_i