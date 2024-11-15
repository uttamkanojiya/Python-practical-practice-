#program to click whether the given number is divible by 7 and multiple by 5 form 1500 and 2700
n=[]
for i in range(1500,2700):
    if(i%7==0) and (i*5):
        n.append(str(i))
print(','.join(n))
