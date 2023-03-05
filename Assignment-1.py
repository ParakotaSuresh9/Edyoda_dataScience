#solution for question1
c=0
a=0
b=1
while(c<50):
    c=a+b
    a=b
    b=c
    print(a,end=' ')


#solution for question2
s=input("Enter string to be reversed")
print(s[::-1])


# solution for question3
series=(1,2,3,4,5,6,7,8,9)
evencount=0
oddcount=0
for num in series:
    if num%2==0:
        evencount+=1
    else:
        oddcount+=1
print("Number of even numbers :",evencount)
print("Number of odd numbers :",oddcount)