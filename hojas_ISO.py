def medidas_hoja_A(N):
    if N == 0:
        res = (841, 1189)
    else:
       res = medidas_hoja_A(N-1)
       a, b = res
       if a > b:
            res = (a // 2, b)
       else:
            res = (b // 2, a)
    return res




print(medidas_hoja_A(5))