arr = [3, 5, 4, 2, 6, 7, 4, 7, 9, 11]
K = 18

def existe_par_hash_con_par(arr, K):
    diccionario = {}
    for elemento in arr:
        complemento = K - elemento
        if complemento in diccionario:
            return True, (elemento, complemento)
        diccionario[elemento] = True
    return False, None

print(existe_par_hash_con_par(arr, K))  # Debería imprimir True
