def sumatoria_cubica(n):
    suma=0
    for i in range(1, n+1):
        for j in range(1, i+1):
            for k in range(j,i+j+1):
                suma+=1
    return suma
    raise NotImplementedError()

def sumatoria_constante(n):
    k= n*(n+1)
    suma=((n+2)/3)*k
    return suma
    raise NotImplementedError()



