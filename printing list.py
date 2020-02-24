#list of numbers

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 74]

print(a)


#user imputs number 

num=int(input("please enter number from list above: "))

#new list creation
newlist = []

#list printed with elements printed under 5

for x in a:
    if x < num:
        newlist.append(x)
        print(newlist)
