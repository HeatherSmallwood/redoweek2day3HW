from math import pi 


def squareFoot(length, width):
    return length * width


lengthOfHouse = float(input('Enter length of the house in feet: '))
widthOfHouse = float(input('Enter width of the house in feet: '))

house_sqft = squareFoot(lengthOfHouse, widthOfHouse)
print(f'The square footage of the house is {house_sqft:.2f} square feet.')






def calculate_circumference(radius):
    return 2 * pi * radius
radiusOfCircle = float(input('Enter radius of the circle in feet: '))
circleCircumference = calculate_circumference(radiusOfCircle)
print(f'The circumference of the circle is {circleCircumference:.2f} square feet')