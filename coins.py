import math

print("Please enter the amount of money to convert:")
print("# of dollars:")
data = input()
dollars = int(data)

print("# of cents:")
data = input()
cents = int(data)

total = (100*dollars) + cents
q = total // 25
total = total - (q*25)
d = total // 10
total = total - (d*10)
n = total // 5
total = total - (n*5)
p = total

dollars = cents // 100
cents = cents % 100
print("The coins are ", q, " quarters, ", d, " dimes, ", n, " nickels and ", p, " pennies", sep="")