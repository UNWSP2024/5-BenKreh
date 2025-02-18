#Ben Krehbiel
#2/17/2025
#global this global that

def get_km():
    return float(input("Kilometer to miles converter: "))

def conversion(km):
    return km * 0.6214  


user_input = get_km()  
result = conversion(user_input)  
print(user_input, "kilometers is", result, "miles")
