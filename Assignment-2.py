# solution for question1
l=[]
for i in range(5):
    n=[]
    a=int(input())
    b=int(input())
    n.append(a)
    n.append(b)
    l.append(tuple(n))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i][1]>l[j][1]):            
            l[i],l[j]=l[j],l[i]
print(l)



# solution for question2
sample=dict()
for i in range(97,123):
    sample[chr(i)]=i
print(sample)