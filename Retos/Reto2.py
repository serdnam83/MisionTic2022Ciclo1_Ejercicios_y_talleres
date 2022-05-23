from curses import termname


informacion = {"id_cliente":"1","nombre":"Johana Fernandez","edad":20,"primer_ingreso":True};
xTreme = {"Valor de boleta":20000,"Edad":18,"Descuento":0.05};
carrosChocones = {"Valor de boleta":5000,"Edad":15-18,"Descuento":0.07};
sillasVoladoras = {"Valor de boleta":10000,"Edad":7-15,"Descuento":0.05};

def cliente(informacion,atraccion):

    resultado = {informacion["nombre"],informacion["edad"]};

    if(informacion["edad"] > atraccion["Edad"] ):
        resultado.append["atraccion":atraccion,"apto":True];
    else:
        resultado.append["atraccion":"N/A","apto":False,"primer_ingreso":informacion["primer_ingreso"],"total_boleta":"N/A"];

    

    return resultado;



cliente(informacion,xTreme);
    

    


        


