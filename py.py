
auta = {
    "Toyota Camry": 2020,
    "Honda Accord": 2019,
    "Ford Mustang": 2021,
    "Chevrolet Malibu": 2018,
    "Volkswagen Golf": 2022
}


print("1) Modely aut a roky výroby:")
for model, rok in auta.items():
    print(f"{model}: {rok}")


delka_slovniku = len(auta)
print(f"\n2) Délka slovníku: {delka_slovniku}")


auta["Toyota Camry"] = 2021
auta["Chevrolet Malibu"] = 2019


print("\n3) Modely aut a nové roky výroby:")
for model, rok in auta.items():
    print(f"{model}: {rok}")
