
def main():
    #Escribe tu código debajo de esta línea
    
    edad = int(input("Ingresa tu edad: "))
    
    if edad >= 18:
        per=str(input("¿Tienes identificación oficial? (s/n): "))
        if per == "s":
            print("Trámite de licencia concedido")
        elif per=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
            
    elif 0 < edad < 18 :
        print("No cumples requisitos")

    else :
        print("Respuesta incorrecta") 
        
if __name__ == '__main__':
    main()
