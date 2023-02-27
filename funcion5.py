def imprimirdiassemana(*todos):
    count=1
    for i in todos:# i irá cogiendo cada día de la semana
        print(f"El {i} es el {count} de la semana")
        count +=1


if __name__== "__main__":
    
    imprimirdiassemana("lunes", "martes", "miercoles", "jueves", "viernes")
    print("-"*10)
    imprimirdiassemana("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
   