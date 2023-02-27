def calcularcuenta(cuenta, propina=10):#por defecto propina tendrá el valor de 100
    total=cuenta * (1 + 0.01 * propina)
    total = round(total,2)
    return(total)



if __name__ == "__main__":
    total=calcularcuenta(100)# aquí cuenta cogerá el valor de 100 y propina será 10
    print(f"hay que pagar un total de {total}")
    total=calcularcuenta(100,11)# aquí la cuenta tendrá un valor de 100 y propina de 11
    print(f"hay que pagar un total de {total}")

