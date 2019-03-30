"""

The purpose of this program is to convert degrees Fahrenheit to degrees Celsius
The formula to calculate this temperature conversion is equal to:
tc= (tf - 32) * 5/9

tf = temperature in Fahrenheit
tc = temperature in Celsius


"""

tf = float(input("Please submit the temperature in Fahrenheit"))
tc = (tf - 32)*(5/9)

print("The current temperature is", round(tc,0), "Celsius")


