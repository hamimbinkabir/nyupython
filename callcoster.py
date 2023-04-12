import math

rate = .40
print("Enter the day the call started at: ")
data = input()
day = data
print("Enter the time the call started at (hhmm): ")
data = input()
start = int(data)
if day == "Sat" or day == "Sun":
    rate = .15
elif start <= 600 or start >= 1800:
    rate = .25

print("Enter the duration of the call (in minutes): ")
data = input()
minutes = int(data)
cost = rate * minutes

print("This call will cost $%2.2f" % cost)