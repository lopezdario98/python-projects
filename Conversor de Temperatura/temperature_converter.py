
def fahrenheit_celsius():
    fahrenheit = int(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit -32) / 1.8
    return "{} grados Fahrenheit son {} grados Celsius" .format(fahrenheit, celsius)

def celsius_fahrenheit():
    celsius = int(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit =  (celsius * 1.8) + 32 
    return "{} grados Celsius son {} grados Fahrenheit" .format(celsius, fahrenheit)

while True:
    print("1) Convertir Fahrenheit a Celsius")
    print("2) Convertir Celsius a Fahrenheit")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            print(fahrenheit_celsius())
        elif opcion == 2:
            print(celsius_fahrenheit())
        elif opcion > 2:
            print("Solo podes elegir entre 1 o 2.")
        else:
            raise ValueError
    except ValueError:
        print("Ingrese solo números (1 o 2).")