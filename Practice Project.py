# part 1
for i in range(1, 101):
    if i**2<200:
        print("i: " + str(i) + ". i^2: " + str(i**2))


# part 2     
user_number=int(input("please enter a number from 1-100: "))
for i in range(1, 101):
    if i**2<user_number:
        print("i: " + str(i) + ". i^2: " + str(i**2))
