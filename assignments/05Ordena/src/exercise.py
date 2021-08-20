def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if z<x>y:
        if y>z :
            print(z)
            print(y)
            print(x)
        else :
            print(y)
            print(z)
            print(x)
    elif x<y>z :
        if x>z :
            print(z)
            print(x)
            print(y)
        else :
            print(x)
            print(z)
            print(y)
    else :
        if x>y :
            print(y)
            print(x)
            print(z)
        else :
            print(x)
            print(y)
            print(z)

if __name__ == '__main__':
    main()
