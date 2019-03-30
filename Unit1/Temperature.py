"""

The purpose of this program is to convert degrees Fahrenheit to degrees Celsius
The formula to calculate this temperature conversion is equal to:
tc= (tf - 32) * 5/9

tf = temperature in Fahrenheit
tc = temperature in Celsius

"""

tc = float(input("Please submit the temperature in Celsius"))
tf = ((tc*9/5) + 32)

print("The current temperature is", round(tf,0), "Fahrenheit")
