convert_from = input("Enter Starting Unit of Measure (inches, feet, yards): ").lower()
convert_to = input("Enter Unit of Measure to Convert to (inches, feet, yards): ").lower()

if convert_from in ["inches", "inch", "in"]:
    num_of_inches = int(input("Enter Number of Inches: "))

    if convert_to in ["feet", "foot", "ft"]:
        print("Result: " + str(num_of_inches) + " Inches = " + str(num_of_inches / 12) + " feet")
    elif convert_to in ["yards", "yard", "yd"]:
        print("Result: " + str(num_of_inches) + " Inches = " + str(num_of_inches / 36) + " yards")
    else:
        print("Please enter inches, feet or yards")

elif convert_from in ["feet", "foot", "ft"]:
    num_of_feet = int(input("Enter Number of Feet: "))

    if convert_to in ["inches", "inch", "in"]:
        print("Result: " + str(num_of_feet) + " Feet = " + str(num_of_feet * 12) + " inches")
    elif convert_to in ["yards", "yard", "yd"]:
        print("Result: " + str(num_of_feet) + " Feet = " + str(num_of_feet / 3) + " yards")
    else:
        print("Please enter inches, feet or yards")

elif convert_from in ["yards", "yard", "yd"]:
    num_of_yards = int(input("Enter Number of Yards: "))

    if convert_to in ["inches", "inch", "in"]:
        print("Result: " + str(num_of_yards) + " Yards = " + str(num_of_yards * 36) + " inches")
    elif convert_to in ["feet", "foot", "ft"]:
        print("Result: " + str(num_of_yards) + " Yards = " + str(num_of_yards * 3) + " feet")
    else:
        print("Please enter inches, feet or yards")

else:
    print("Please enter inches, feet or yards")
