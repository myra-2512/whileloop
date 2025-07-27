n=int(input("Enter the value of terms:"))

sum=0
i=1

while i<=n:
    sum += i
    i +=1

print("/nSum =",sum)

#activity 2

#i=0

#while i<=0:
#    print("I WILL RUN FOREVER")

#activity 3

num=int(input("Enter a number:"))

sum=0

temp=num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")


#activity 4

fruits=["pear","litchi","banana"]

j=0

while j <=2:
    print(fruits[j])
    j += 1