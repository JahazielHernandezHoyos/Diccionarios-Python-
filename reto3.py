Seleccion = ({
        20170136837:{
        "nombres" : "Jorge Juan",
        "apellidos" : "Moreno, López",
        "documento" : 88481595,
        "programa" : "ARQU",
        "materias" : [
        {
        "facultad" : "Arquitectura",
        "codigo" : "ARQU-2113",
        "nota" : 2.97,
        "creditos" : 2,
        "retirada" : "Si",
        },
        {
        "facultad" : "Arquitectura",
        "codigo" : "ARQU-5048",
        "nota" : 4.26,
        "creditos" : 0,
        "retirada" : "No",
        },
        ]
        },
        20130225137:{
        "nombres" : "Sara Carolina",
        "apellidos" : "Gómez, Fernández",
        "documento" : 58770043,
        "programa" : "ARQD",
        "materias" : [
        {
        "facultad" : "Arquitectura",
        "codigo" : "ARQD-7738",
        "nota" : 3.36,
        "creditos" : 3,
        "retirada" : "No",
        },
        {
        "facultad" : "Arquitectura",
        "codigo" : "ARQD-7698",
        "nota" : 1.59,
        "creditos":4,
        "retirada": "Si",},
        ]
        } })


#[20130225137, 'Sara Carolina', 'Gómez, Fernández', 58770043, 'ARQD', 4.375, 'sc.gomez43']
    
    
    
def Seleccion(info:dict):  
    respuesta =[]
    masAlto = 0
    listaCodigos = []
    for a in info:
        listaCodigos.append(a)

    for i in range(0,len(listaCodigos)):
        #print(info[listaCodigos[i]]["nombres"])
        #print(info[listaCodigos[i]]["apellidos"])
        #print(info[listaCodigos[i]]["documento"])
        #print(info[listaCodigos[i]]["programa"])
        sumatoria = 0
        sumatoriaCreditos = 0

        for m in info[listaCodigos[i]]["materias"]:
            #print(m)
            #print(m["nota"])
            #print(m["creditos"])
            #print(m["retirada"])
            sumatoria = sumatoria + (m["nota"]*m["creditos"])
            sumatoriaCreditos = sumatoriaCreditos+m["creditos"]

        promedio = sumatoria/sumatoriaCreditos
        if promedio > masAlto:
            masAlto = promedio
            codigoMasAlto = listaCodigos[i]
            estudianteMasAlto = info[listaCodigos[i]]
    #print("el promedio mas alto es: ", masAlto)
    #print(codigoMasAlto)
    #print(estudianteMasAlto)
    
    respuesta.append(codigoMasAlto)
    respuesta.append(estudianteMasAlto["nombres"])
    respuesta.append(estudianteMasAlto["apellidos"])
    respuesta.append(estudianteMasAlto["documento"])
    respuesta.append(estudianteMasAlto["programa"])
    respuesta.append(estudianteMasAlto["nombres"[0]])

    print(len(estudianteMasAlto["nombres"]))

    #estudianteGanador=listaCodigos[i]
    
    return respuesta
