c = 299792458 

def main():

    mass_in_kg = float(input("Enter kilos of mass: "))

    energy_in_joules = mass_in_kg * (c ** 2)


    print(f"e = m * c^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"c = {c} m/s")
    print(f"{energy_in_joules} joules of energy!")

if __name__ == "__main__":
    main()    