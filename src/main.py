motors = int(input("How many motors are carrying the packages? "))
weight = int(input("How many kg of packages do we expect? "))

if weight / motors <= 12:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No. The conveyor belt cannot carry the packages.")
