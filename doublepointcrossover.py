import random
            

p1 = [1,2,3,4,5,6,7,8,9,0]
p2 = [9,7,8,6,5,3,4,1,2,0]
        

rand_1=random.randint(0, 9)
rand_2=random.randint(0,9)
if(rand_2>=rand_1):
    x=rand_1
    y=rand_2
else:
    x=rand_2
    y=rand_1


child_1=[-1 for k in range(10)]
child_2=[-1 for k in range(10)] 
for i in range(x,y):

    child_1[i]=p1[i]
    child_2[i]=p2[i]

print(x," ", y)

for i in range(10):

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
        

print(p1)
print("   ")
print(p2)
print("   ")
print(child_1)
print("   ")
print(child_2)
print("   ")


def main():
    doublepoinrcrossover();