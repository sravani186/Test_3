# Example 5: Python program to calculate the sum of all the even numbers within the given range.

c=int(input("enter the even number :"))
sum=0
for x in range(1,c+1):
    if x % 2 ==0:
        sum=sum+x
print(sum)
