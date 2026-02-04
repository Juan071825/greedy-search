estaciones = {}
estaciones["kone"] = set(["id", "nv", "ut"])
estaciones["ktwo"] = set(["wa", "id", "mt"])
estaciones["kthree"] = set(["or", "nv", "ca"])
estaciones["kfour"] = set(["nv", "ut"])
estaciones["kfive"] = set(["ca", "az"])
estaciones["ksix"] = set(["nm", "tx", "ok"])
estaciones["kseven"] = set(["ok", "ks", "co"])
estaciones["keight"] = set(["ks", "co", "ne"])
estaciones["knine"] = set(["ne", "sd", "wy"])
estaciones["kten"] = set(["nd", "ia"])
estaciones["keleven"] = set(["mn", "mo", "ar"])
estaciones["ktwelve"] = set(["la"])
estaciones["kthirteen"] = set(["mo", "ar"])

def mejor_estacion(estaciones):
    estaciones_seleccionadas = []
    estados_cubiertos = set()

    while len(estados_cubiertos) < len(estaciones.values()):
        
        mejor_estacion = None
        estados_mejor_estacion = set()

        for estacion, estados in estaciones.items():
            nuevos_estados_aportados = estados - estados_cubiertos

            if len(nuevos_estados_aportados) > len(estados_mejor_estacion):
                mejor_estacion = estacion
                estados_mejor_estacion = nuevos_estados_aportados
        
        estaciones_seleccionadas.append(mejor_estacion)
        estados_cubiertos |= estaciones[mejor_estacion]
    
    return estaciones_seleccionadas, estados_cubiertos
                




    




if __name__ == '__main__':

    print(mejor_estacion(estaciones))