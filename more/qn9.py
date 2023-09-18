'''
A car needs 10 times more fuel than the distance it covers. But the car always has a minimum of 100 ltr of fuel in
stock.(Fuel the car)
This means that if the car needs to travel 15 km, it would need 150 ltr of fuel.
But if a car needs to travel just 5 km, the car would need just 50 ltr of fuel. In this case, the car
doesn't need extra fuel since it always has 100 ltr of fuel in stock.
Now, create a Python program that calculates the total fuel needed and the extra fuel supplied to
the car when the distance is given.
Note: Display the result in a tuple as (total_required_fuel, extra_fuel).
Example Test Input:310 Expected Output:(3100, 3000)
'''

def fuel_cal(x):
    stock_fuel = 100
    needed_fuel = x * 10
    
    if needed_fuel < stock_fuel:
        print ("The total fuel needed is",needed_fuel,
               "which is less than the fuel in stock no extra fuel is needed")
        
    elif needed_fuel > stock_fuel:
        extra_fuel = needed_fuel - stock_fuel
        extras_fuel=needed_fuel,extra_fuel
        tuple(extras_fuel)
        # extras_fuel = tuple(extra_fuel)
        # print ("The total fuel needed is",needed_fuel,extra_fuel)
        print ("The total fuel needed, extra fuel is",extras_fuel)
        
    else:
        print(needed_fuel)
    
userinput= int(input("what is the distance to be covered: "))
fuel_cal(userinput)    