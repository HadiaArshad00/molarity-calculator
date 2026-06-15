def molarity_calculator():
    print("Molarity Calculator\n")
    print("Molarity (M) = Moles of Solute / Volume of Solution (L)\n")

    moles = float(input("Enter moles of solute (mol): "))
    volume = float(input("Enter volume of solution (L): "))

    if volume <= 0:
        print("Volume must be greater than zero.")
        return

    molarity = moles / volume
    print(f"\nMolarity = {round(molarity, 4)} mol/L")

    if molarity < 0.1:
        print("Dilute solution")
    elif molarity < 1:
        print("Moderately concentrated solution")
    else:
        print("Concentrated solution")

molarity_calculator()
