def validar_afiliado(estado):
    if estado == "Activo":
        return "Puede acceder al servicio"
    return "Afiliado inactivo"

print(validar_afiliado("Activo"))