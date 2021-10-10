#!/usr/bin/env python
# coding: utf-8

# In[1]:


def separa(nombre_archivo_entrada,nombre_archivo_salida):
    with open("../osm/"+nombre_archivo_entrada,"r") as file:
        file = file.read().splitlines()  #LEEMOS EL ARCHIVO
        nf = [i for i in range(len(file)) if file[i].rstrip("\n")=="OS:Material,"]  #SE GENERA UNA LISTA DE LOS ÍNDICES DONDE 
                                                                          # SE ENCUENTRA LA PALABRA "OS:Material". POR LO QUE 
                                                                          # IDENTIFICA LA LÍNEA DONDE COMIENZA EL OBJETO 
    
        inb = [j+1 for j in range(len(file)) if file[j].rstrip("\n")==""]  #SE GENERA UNA LISTA DONDE SE ENCUENTRAN LOS
                                                                      # ESPACIOS VACÍOS
    
    # ESTAS LINEAS DE CÓDIGO COMPARAN AMBAS LISTAS ANTES GENERADAS Y ENCUENTRAN LOS ÍNDICES, LOS CUALES QUEDAN GUARDADOS 
    # EN lista_final, QUE DETERMIAN DONDE TERMINA EL OBJETO. CON LO CUAL YA TENEMOS LA LISTA QUE INDICA DONDE EMPIEZA CADA
    # OBJETO DE "OS:Materiales," (la lista nf) Y LA LISTA DONDE TERMINA CADA UNO DE DICHOS OBJETOS (la lista lista_final)
    lista = []  
    for k in range(len(nf)):
        for h in range(len(inb)):
            if nf[k] == inb[h]:
                lista.append(inb[h+1])
    lista_final = []
    for x in lista:
        lista_final.append(x-1)
        
    # SE CREA UNA LISTA DE LISTAS DONDE SE ALMACENA LA INFORMACIÓN    
    resultados = []
    for s in range(len(nf)):
        resultado = file[nf[s]:lista_final[s]]
        resultados.append(resultado)
    
    # SE GUARDA EL ARCHIVO
    with open("../resultados/"+nombre_archivo_salida,"w") as result:
        for s in range(len(resultados)):
            for r in range(len(resultados[s])):
                result.write(resultados[s][r] + "\n")


# In[2]:


separa("materiales.osm","resultado.osm")

