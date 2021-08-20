

import random
import copy
import math


POPULATION_SIZE = 50
CITIES_SIZE = 100
TOUR_SIZE = 100
NUM_EXECUTION = 50
population = []
x=[]
y=[]
parent_1= []
parent_2= []
parent= []
tour=[]
children=[]
f_value=[]


def numberExists(path, number):
    for i in path:
        if i == number:
            return True
    return False


def generatePopulation():
    # For each position, generates a new possible path
    for _ in range(1, POPULATION_SIZE + 1):
        path=[]
        for _ in range(1, CITIES_SIZE + 1):
            
        
            randomNum = random.randint(0, 99)
            while(numberExists(path, randomNum)):
                randomNum = random.randint(0, 99)
            path.append(randomNum)
        population.append(path)





def FetchXandY():
    global x
    global y
    f = open('City_Coordinates.txt', 'r')
    for line in f.readlines():
        cordinates = line.split(',')
        x.append(int(cordinates[0]))
        y.append(int(cordinates[1]))
    f.close()




def mutate(c):  #mutation is called in crossover  
    for i in range(0, len(c)):
        for _ in range(0, len(c[i])):
            ranNum = random.uniform(0, 1)
            if  ranNum <=0.01:
                a = random.randint(0, 99)
                b = random.randint(0, 99)
                var1 = c[i][a]
                var2 = c[i][b]
                c[i][a] = var2
                c[i][b] = var1




def generatecircle():
    global tour
    global population
    tour=population
    for i in range(50):
        tour[i].append(tour[i][0])



def sec(a):
    return a[1] #returns the first key of array





def path_fitness():
    global f_value
    f_value *=0
    for i in range(50):
        k=0
        for j in range(100):
            k=k+math.sqrt((x[tour[i][j]]-x[tour[i][j+1]])**2 + (y[tour[i][j]]-y[tour[i][j+1]])**2)
        f_value.append((i, k))
    f_value.sort(key=sec)



def rouletteFunction():

    global parent
    parent *=0
    for i in range (50):
        u=random.uniform(0, 1)
        if u>0 and u<=0.95:
            parent.append(f_value[i][0])




def single_point_crossover():
    global population
    global f_value
    global parent
    global parent_1
    global parent_2
    global children
    children*=0
    
    sz=(int)(len(parent)/2)
    
    
    for i in range(sz):
        parent_1.append(parent[i])
        parent_2.append(parent[sz+i])
    
   
    if len(parent_1)> len(parent_2):
        cnt=len(parent_2)
    else:
        cnt=len(parent_1)

    for i in range(cnt):
        p1 = population[parent_1[i]]
        p2 = population[parent_2[i]]

        rand_num = random.randint(0, 99)

        childone=[]
        childtwo=[]
        
        for j in range (rand_num):
            childone.append(p1[j])
            childtwo.append(p2[j])

        for k in range(100):
            if(p1[k] not in childtwo):
                childtwo.append(p1[k])
            if(p2[k] not in childone):
                childone.append(p2[k])
                
            

        children.append(childone)
        children.append(childtwo)
        
    for i in range (POPULATION_SIZE-2*cnt):
        children.append(population[f_value[i][0]])
        
        mutate(children)

    population=children


def double_point_crossover():
    global population
    global f_value
    global parent
    global parent_1
    global parent_2
    global children
    children*=0
    sz=int((len(parent)/2))
    
    for i in range(sz):
        parent_1.append(parent[i])
        parent_2.append(parent[sz+i])
    
    
    if len(parent_1)> len(parent_2):
        cnt=len(parent_2)
    else:
        cnt=len(parent_1)

    for i in range(cnt):
        p1 = population[parent_1[i]]
        p2 = population[parent_2[i]]
        

        rand_1=random.randint(0, 99)
        rand_2=random.randint(0,99)
        if(rand_2>=rand_1):
            x=rand_1
            y=rand_2
        else:
            x=rand_2
            y=rand_1

        child_1=[-1 for k in range(CITIES_SIZE)]
        child_2=[-1 for k in range(CITIES_SIZE)] 
        for i in range(x,y):

            child_1[i]=p1[i]
            child_2[i]=p2[i]

    

        for i in range(100):

            if(child_1[i]==-1):
                j=0
                while(p2[j] in child_1):
                    j+=1
                   
                child_1[i]=p2[j]
                    
            

            if(child_2[i]==-1):
                j=0
                while(p1[j] in child_2):
                    j+=1

                child_2[i]=p1[j]

 
        children.append(child_1)
        children.append(child_2)

        for i in range (POPULATION_SIZE-2*cnt):
            children.append(population[f_value[i][0]])
    
    mutate(children)
    population=children

    
    
# def alternate_crossover():
#     global population
#     global f_value
#     global parent
#     global parent_1
#     global parent_2
#     global children
#     children*=0
    
#     sz=int((len(parent)/2))
    
#     for i in range(sz):
#         parent_1.append(parent[i])
#         parent_2.append(parent[sz+i])
    
    
#     if len(parent_1)> len(parent_2):
#         cnt=len(parent_2)
#     else:
#         cnt=len(parent_1)

#     for i in range(cnt):
#         p1 = population[parent_1[i]]
#         p2 = population[parent_2[i]]
            
#     child_1=[-1 for k in range(CITIES_SIZE)]
#     child_2=[-1 for k in range(CITIES_SIZE)]     

#     m=0
#     for i in range(100):
#         if(m==0):
#             if(p1[i] not in child1[i]):
#                 child_2[i]=p2[i]

#             m+=1

#         else(m==1):
#             if(p2[i] not in child1[i]):
                
#                  child_1[i]=p2[i]

#             m-=1   

       
# #    for child 2
    
#     n=0
#     for i in range(100):
#             if(n==0):

#                 if(p2[i] not in child2[i]):

#                     child_2[i]=p2[i]

#                 n+=1

#             else(n==1):
#                 if(p1[i] not in child2[i]):
#                     child_2[i]=p1[i]

#                 n-=1   

#     children.append(child1)
#     children.append(child2)
     
        
#     for i in range (POPULATION_SIZE-2*cnt):
#         children.append(population[f_value[i][0]])
    
#     mutate(children)
#     population=children
    
        
def main():
   
    generatePopulation()
    FetchXandY()

   
    for _ in range(NUM_EXECUTION):
        generatecircle()
        path_fitness()
        rouletteFunction()
        mutate(population)  
#         double_point_crossover()
#         single_point_crossover()
#         alternate_crossover()


    path_fitness()
    
    print("mutation probability : 0.01")
    print("selection probability : 0.95")
    print("population size ",POPULATION_SIZE)
    print("number of cities" ,CITIES_SIZE)
    print('best fitnes chromosome' , population[0])
    print("fitness value ", f_value[0][1])
    print("best path", population[f_value[0][0]])




