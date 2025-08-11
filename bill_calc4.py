unit=int(input("Enter Electricity units consumed:"))
rate=0
tot=0
if unit>0 and unit<=100:
    rate=3
    tot=unit*3
elif unit>=101 and unit<=300:
    rate=5
    tot=unit*5
elif unit>=301 and unit<=500:
    rate=7
    tot=unit*7
elif unit>=500:
    rate=10
    tot=unit*10
print("Electricity Bill Summary")
print("------------------------")
print("Units Consumed :",unit)
print("Rate Applied :₹",rate)
print("Total Bill :₹",tot)
