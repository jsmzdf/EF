# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:30:25 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
import numpy as np
entrada=pd.read_csv('EPnumerio.csv' )
def sacarelementosok(seleecion):
    seleccion=entrada.copy()
    for i in seleccion:    
         nopasa=seleccion[seleccion[i]>1]
         if len(nopasa)>1:
             seleccion=seleccion.drop([i],axis=1)
    return seleccion
mat=sacarelementosok(entrada)
def kr20(seleccion):
    
    seleccion['total']=seleccion.sum(axis=1)
    p=seleccion.drop(['total'], axis =1).mean(axis=0)
    p=p.copy().T
    q=1-p
    pq=p*q
    k=len(seleccion.T)-1
    print(k)
    sumatoria_pq=pq.sum()
    varT=seleccion['total'].var(ddof=0)
    result=(k/(k-1))*(1-(sumatoria_pq/varT))
    return result
kr=kr20(mat)
def corrItemTest(matriz1):
    salida=[]
    for x in matriz1.drop(['total'], axis =1):
        b=matriz1['total']
        a=matriz1[x]
        c=np.corrcoef(a,b)[0,1]
        salida.append(c)
    return salida
rCorrItemTest=corrItemTest(mat)
def indicecorrelaT(matriz1):
    salida=[]
    for x in matriz1.drop(['total'], axis =1):
        b=matriz1['total']
        a=matriz1[x]
        c=np.corrcoef(a,b-a)[0,1]
        salida.append(c)
    return salida
rIndiceHCorregido=indicecorrelaT(mat)

def sisequitaunElemto(matriz):
    vector=[]
    for i in matriz.drop(['total'], axis =1):
        matrizSin=matriz.drop([i], axis =1)
        matrizSin['total']=matrizSin.sum(axis=1)
        p=matrizSin.drop(['total'], axis =1).mean(axis=0)
        p=p.copy().T
        q=1-p
        pq=p*q
        k=len(matrizSin.T)-1
        print(k)
        sumatoria_pq=pq.sum()
        varT=matrizSin['total'].var(ddof=0)
        result=(k/(k-1))*(1-(sumatoria_pq/varT))
        vector.append(result)
    return vector
prueba=sisequitaunElemto(mat)
"""vector=[]
for i in seleccion.drop(['total'], axis =1):
    vector.append( seleccion[i][seleccion[i]==1].value_counts()/len(seleccion))
p=pd.DataFrame(vector).T
resul2t=(k/(k-1))*((varT-sumatoria_pq)/varT)
"""