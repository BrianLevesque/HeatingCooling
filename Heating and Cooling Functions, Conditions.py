# a function that takes in the actual temperature and the desire temperature
# and prints out either "Run A/C", "Run heat", or "Standby"

def heating_cooling(actual_temp, desired_temp):
    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    else:
        print("standby")


# extended challenge function convert temp which takes a temperature in celsius and converts it to another unit of measure
def convert_temp(temp_celsius, target_unit):
    if target_unit == "C":
        return temp_celsius
    if target_unit == "K":
        return temp_celsius + 273.15
    if target_unit == "F":
        return (9 / 5) * temp_celsius + 32


# testing function with different arguements

heating_cooling(85, 75)  # expected result is to print Run A/C
heating_cooling(65, 72)  # expected result is to print Run heat
heating_cooling(70, 70)  # expected result is to print Standby

heating_cooling(90, 74)  # expected result is to print Run A/C
heating_cooling(56, 71)  # expected result is to print Run heat
heating_cooling(69, 69)  # expected result is to print Standby

# testing convert_temp
print(convert_temp(0, "F"))  # expected output is 32
print(convert_temp(1, "K"))  # expected output is 274.15
print(convert_temp(45, "C"))  # expected output is 45

cTemp = int(
    input("Please enter the current temp:"))  # asking the user for the current temp and assigning cTemp with that value
dTemp = int(
    input("Please enter the desired temp:"))  # asking the user for the desired temp and assigning dTemp with that value
heating_cooling(cTemp, dTemp)  # running the function with the inputed values