ingreso_mensual = 72000
gasto_mensual = 8000

if ingreso_mensual > 100000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        print("pa, estas gastando una banda, hay que ver si te alcanza")
    
elif ingreso_mensual > 500:
    print("estas bien en Venezuela")
    
elif ingreso_mensual > 200:
    print("estas bien en paises pobres")
    
else:
    print("eres pobre")