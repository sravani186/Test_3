# Example 4: Python program to calculate the sum of all the odd numbers within the given range.

z=int(input("enter the number :"))
sum=0
for x in range(1,z+1):
    if x % 2 !=0:
        sum=sum+x
print(sum)
    
