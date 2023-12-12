#recieving input data
lenth = int(input("how long? \n"))
updowns = input("Ups And Downs: \n")
#turn into a list of numbers
climb = list(map(int, updowns.split()))
print(climb)
# counting ones and twos
twos = climb.count(2)
ones = climb.count(1)

print(f'there are {ones} one and {twos} Two and {lenth-(ones+twos)} zeros \n')

odd1 = True if (ones % 2) == 1 else False
odd2 = True if twos % 2 == 1 else False
if not ((sum(climb)) / 2)%2 :
    print("distance is 0")
else:
    if ones ==0 and odd2 :
        print("distance is 2")
    else:
        print("distance is 1")