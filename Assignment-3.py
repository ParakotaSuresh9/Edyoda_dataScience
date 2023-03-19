#solution for question1
def sum_elements(l):
    s=0
    for i in l:
        s+=i
    return s
print(sum_elements([8,2,3,0,7]))



#solution for question2
def str_reverse(s):
    print(s[::-1])
str_reverse("1234abcd")



#solution for question3
def cal_upper_lower(s):
    upper_count=0
    lower_count=0
    for i in s:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    print('No. of Upper case characters :',upper_count)
    print('No. of Lower case characters :',lower_count)
cal_upper_lower('The quick Brow Fox')


