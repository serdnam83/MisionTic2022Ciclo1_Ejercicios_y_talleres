def CDT(usuario:str, monto:int, tiempo:int):
    
    if(tiempo <= 2):
        valorTotal = monto - ((monto * 0.02))
        mensaje = "Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(monto) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valorTotal)
        
    else:
        valorTotal = ((monto * 0.03 * tiempo)/12)+monto
        mensaje = "Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(monto) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valorTotal)
    
    return mensaje;
    
print (CDT("pepito", 2000000, 1));   

