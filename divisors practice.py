#user enters number
num=int(input("Please enter a number: "))

#works out the intigers from 1 to the entered number
listrange = list(range(1,num+1))


#list of divisors
divisors = []

#for loop to work out divisors
for i in listrange:
    #divides the entered number by  the list range integers and if they have a modulas of 0 they are divisers
    if num % i == 0:
        divisors.append(i)

print(divisors)