
def calcular_precio_final():
    try:
        base_imponible = float(input("Ingrese la base de la imponible: "))
    except ValueError:
        print("La base de la imponible no es valida")
        return


    tipo_iva = input("Ingrese la tipo de iva(general,reducido,superreducido): ").lower()
    cod_promo = input("Ingrese el codigo Promocional (sinpromo, mitad, descfijo,porcentaje): ").lower()

    tipos_iva = {
      "general": 0.21,
      "reducido": 0.10,
      "superreducido": 0.04
    }


    if tipo_iva not in tipos_iva:
        print("Error tipo de iva no es valida")
        return
    if tipo_iva == "general":
        emoji_iva = "21%"
    elif tipo_iva == "reducido":
        emoji_iva = "10%"
    elif tipo_iva == "superreducido":
        emoji_iva = "4%"
    else:
        print("Error tipo de iva no es valida")
        emoji_iva = "error"


    iva = base_imponible * tipos_iva[tipo_iva]
    precio_con_iva = base_imponible + iva

    if cod_promo == "sinpromo":
        precio_final = precio_con_iva
    elif cod_promo == "mitad":
        precio_final = precio_con_iva/2
    elif cod_promo == "descfijo":
        precio_final = precio_con_iva - 5
        if precio_final < 0:
            precio_final = 0
    elif cod_promo == "porcentaje":
        precio_final = precio_con_iva * 0.95
    else:
        print("Error de promocion no es valida")
        return
    print(f"\n Base imponible: {base_imponible:.2f} €")
    print(f"Iva Aplicado ({emoji_iva}): {iva:.2f} €")
    print(f"Precio con Iva: {precio_con_iva:.2f} €")
    print(f"Codigo Promo ({cod_promo}): -{precio_final} €")
    print(f"Precio Final: {precio_final:.2f} €")

calcular_precio_final()