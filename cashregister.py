import math

print("Enter price of the first item:")
data = input()
p1 = float(data)
print("Enter price of the second item:")
data = input()
p2 = float(data)
base = p1 + p2
print("Does customer have a club card? (Y/N):")
data = input()
bCard = data
discount = 0.00
print("Enter tax rate, e.g. 5.5 for 5.5% tax:")
data = input()
tax = float(data)

if p1 > p2:
    discount += round((p2 / 2), 2)
else:
    discount += round((p1 / 2), 2)
if 'y' == bCard or bCard == 'Y':
    discount += round(((base-discount)* .10) ,2)
price = base - discount
price = round(price, 2)
total = price + (price * (tax/100))
total = round(total, 2)

print("Base price = %2.2f" % base)
print("Price after discounts = %2.2f" % price)
print("Total price = %2.2f" % total)